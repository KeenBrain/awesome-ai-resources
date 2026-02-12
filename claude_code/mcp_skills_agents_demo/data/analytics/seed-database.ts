import Database from "better-sqlite3";
import path from "path";
import fs from "fs";

// ---------------------------------------------------------------------------
// Deterministic pseudo-random number generator (LCG)
// ---------------------------------------------------------------------------
const LCG_A = 1664525;
const LCG_C = 1013904223;
const LCG_M = 2 ** 32;
let lcgState = 42; // fixed seed for reproducibility

function rand(): number {
  lcgState = (LCG_A * lcgState + LCG_C) % LCG_M;
  return lcgState / LCG_M; // 0..1
}

function randInt(min: number, max: number): number {
  return Math.floor(rand() * (max - min + 1)) + min;
}

function pick<T>(arr: T[]): T {
  return arr[Math.floor(rand() * arr.length)];
}

function weightedPick<T>(items: T[], weights: number[]): T {
  const r = rand();
  let cumulative = 0;
  for (let i = 0; i < items.length; i++) {
    cumulative += weights[i];
    if (r < cumulative) return items[i];
  }
  return items[items.length - 1];
}

// ---------------------------------------------------------------------------
// Date helpers
// ---------------------------------------------------------------------------
const START_DATE = new Date("2024-12-15T00:00:00Z");
const END_DATE = new Date("2025-03-14T23:59:59Z");
const TOTAL_DAYS = 90;

function randomDatetime(): Date {
  const offset = rand() * (END_DATE.getTime() - START_DATE.getTime());
  return new Date(START_DATE.getTime() + offset);
}

function dateForDay(dayIndex: number): string {
  const d = new Date(START_DATE);
  d.setUTCDate(d.getUTCDate() + dayIndex);
  return d.toISOString().slice(0, 10); // YYYY-MM-DD
}

function fmtDatetime(d: Date): string {
  return d.toISOString().replace("T", " ").slice(0, 19);
}

// ---------------------------------------------------------------------------
// Database setup
// ---------------------------------------------------------------------------
const PROJECT_ROOT = path.resolve(__dirname, "../..");
const DB_PATH = path.join(PROJECT_ROOT, "data", "analytics", "product_analytics.db");

if (fs.existsSync(DB_PATH)) {
  fs.unlinkSync(DB_PATH);
  console.log("Deleted existing database.");
}

const db = new Database(DB_PATH);
db.pragma("journal_mode = WAL");

// ---------------------------------------------------------------------------
// Create tables
// ---------------------------------------------------------------------------
db.exec(`
  CREATE TABLE user_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    session_start DATETIME NOT NULL,
    session_end DATETIME NOT NULL,
    duration_seconds INTEGER NOT NULL,
    device_type TEXT NOT NULL,
    page_views INTEGER NOT NULL,
    created_at DATETIME NOT NULL
  );

  CREATE TABLE feature_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_name TEXT NOT NULL,
    action TEXT NOT NULL,
    user_id TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    metadata TEXT
  );

  CREATE TABLE funnel_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    completed BOOLEAN NOT NULL
  );

  CREATE TABLE nps_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    score INTEGER NOT NULL,
    segment TEXT NOT NULL,
    comment TEXT,
    created_at DATETIME NOT NULL
  );

  CREATE TABLE daily_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    dau INTEGER NOT NULL,
    new_signups INTEGER NOT NULL,
    churn_count INTEGER NOT NULL,
    revenue_cents INTEGER NOT NULL,
    avg_session_duration_seconds INTEGER NOT NULL
  );
`);

console.log("Tables created.");

// ---------------------------------------------------------------------------
// 1. user_sessions (~5000 rows)
// ---------------------------------------------------------------------------
{
  const insert = db.prepare(`
    INSERT INTO user_sessions (user_id, session_start, session_end, duration_seconds, device_type, page_views, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `);

  const insertMany = db.transaction(() => {
    for (let i = 0; i < 5000; i++) {
      const userId = `user_${randInt(1, 800)}`;
      const start = randomDatetime();
      // duration: roughly normal around 270s, clamped 30..1800
      let duration = Math.round(270 + (rand() + rand() + rand() - 1.5) * 300);
      duration = Math.max(30, Math.min(1800, duration));
      const end = new Date(start.getTime() + duration * 1000);
      const device = weightedPick(["desktop", "mobile", "tablet"], [0.6, 0.3, 0.1]);
      const pageViews = randInt(1, 25);
      insert.run(userId, fmtDatetime(start), fmtDatetime(end), duration, device, pageViews, fmtDatetime(start));
    }
  });
  insertMany();
  console.log("Inserted 5000 user_sessions.");
}

// ---------------------------------------------------------------------------
// 2. feature_usage (~3000 rows with baked-in signals)
// ---------------------------------------------------------------------------
{
  const insert = db.prepare(`
    INSERT INTO feature_usage (feature_name, action, user_id, timestamp, metadata)
    VALUES (?, ?, ?, ?, ?)
  `);

  const features = ["dashboard", "export", "filters", "charts", "user_table", "settings", "funnel", "nps"];
  const normalActions: Array<[string, number[]]> = [
    // feature -> weights for [view, click, error, abandon]
    ["dashboard", [0.55, 0.35, 0.05, 0.05]],
    ["charts",    [0.50, 0.38, 0.07, 0.05]],
    ["user_table",[0.50, 0.35, 0.08, 0.07]],
    ["settings",  [0.55, 0.30, 0.08, 0.07]],
  ];

  const insertMany = db.transaction(() => {
    let count = 0;

    // Normal features (~1800 rows)
    for (const [feat, weights] of normalActions) {
      const n = randInt(500, 560);
      for (let i = 0; i < n; i++) {
        const action = weightedPick(["view", "click", "error", "abandon"], weights);
        const userId = `user_${randInt(1, 800)}`;
        const ts = randomDatetime();
        const meta = JSON.stringify({ source: pick(["sidebar", "navbar", "shortcut", "search"]) });
        insert.run(feat, action, userId, fmtDatetime(ts), meta);
        count++;
      }
    }

    // Export feature: ~460 rows, HIGH abandon (340) and error rate
    for (let i = 0; i < 460; i++) {
      let action: string;
      if (i < 340) {
        action = "abandon";
      } else if (i < 400) {
        action = "error";
      } else if (i < 430) {
        action = "view";
      } else {
        action = "click";
      }
      const userId = `user_${randInt(1, 800)}`;
      const ts = randomDatetime();
      const meta = JSON.stringify({
        source: pick(["toolbar", "context_menu", "shortcut"]),
        format: pick(["csv", "pdf", "xlsx"]),
        error: action === "error" ? pick(["timeout", "payload_too_large", "format_error"]) : undefined,
      });
      insert.run("export", action, userId, fmtDatetime(ts), meta);
      count++;
    }

    // Filters feature: ~380 rows, HIGH error (280)
    for (let i = 0; i < 380; i++) {
      let action: string;
      if (i < 280) {
        action = "error";
      } else if (i < 340) {
        action = "view";
      } else {
        action = "click";
      }
      const userId = `user_${randInt(1, 800)}`;
      const ts = randomDatetime();
      const meta = JSON.stringify({
        filter_type: pick(["date_range", "segment", "tag", "custom"]),
        error: action === "error" ? pick(["invalid_query", "timeout", "no_results"]) : undefined,
      });
      insert.run("filters", action, userId, fmtDatetime(ts), meta);
      count++;
    }

    // Funnel feature: very few views (placeholder) ~40 rows
    for (let i = 0; i < 40; i++) {
      const action = weightedPick(["view", "click", "abandon"], [0.6, 0.15, 0.25]);
      const userId = `user_${randInt(1, 800)}`;
      const ts = randomDatetime();
      const meta = JSON.stringify({ note: "placeholder_feature", source: "analytics_page" });
      insert.run("funnel", action, userId, fmtDatetime(ts), meta);
      count++;
    }

    // NPS feature: almost no views (placeholder) ~20 rows
    for (let i = 0; i < 20; i++) {
      const action = weightedPick(["view", "abandon"], [0.7, 0.3]);
      const userId = `user_${randInt(1, 800)}`;
      const ts = randomDatetime();
      const meta = JSON.stringify({ note: "placeholder_feature" });
      insert.run("nps", action, userId, fmtDatetime(ts), meta);
      count++;
    }

    console.log(`Inserted ${count} feature_usage rows.`);
  });
  insertMany();
}

// ---------------------------------------------------------------------------
// 3. funnel_events (~2000 rows with drop-off)
// ---------------------------------------------------------------------------
{
  const insert = db.prepare(`
    INSERT INTO funnel_events (user_id, stage, timestamp, completed)
    VALUES (?, ?, ?, ?)
  `);

  const stages: Array<{ name: string; total: number; completedCount: number }> = [
    { name: "signup",     total: 1000, completedCount: 1000 },
    { name: "onboarding", total: 1000, completedCount: 680 },
    { name: "activation", total: 680,  completedCount: 340 },
    { name: "active",     total: 340,  completedCount: 230 },
    { name: "paid",       total: 230,  completedCount: 110 },
  ];

  const insertMany = db.transaction(() => {
    let count = 0;
    // Each user who reaches a stage gets a row
    // For signup: 1000 users, all completed
    // For onboarding: same 1000 users attempted, 680 completed
    // etc.
    const userIds = Array.from({ length: 1000 }, (_, i) => `user_funnel_${i + 1}`);

    let pool = [...userIds]; // users still in funnel
    for (const stage of stages) {
      const attemptCount = pool.length;
      for (let i = 0; i < attemptCount; i++) {
        const completed = i < stage.completedCount ? 1 : 0;
        const ts = randomDatetime();
        insert.run(pool[i], stage.name, fmtDatetime(ts), completed);
        count++;
      }
      // Only those who completed move to next stage
      pool = pool.slice(0, stage.completedCount);
    }
    console.log(`Inserted ${count} funnel_events.`);
  });
  insertMany();
}

// ---------------------------------------------------------------------------
// 4. nps_responses (~500 rows, segment-weighted scores)
// ---------------------------------------------------------------------------
{
  const insert = db.prepare(`
    INSERT INTO nps_responses (user_id, score, segment, comment, created_at)
    VALUES (?, ?, ?, ?, ?)
  `);

  const freeComments = [
    "Too limited for my needs.",
    "Nice free tier but export is broken.",
    "Would pay if filters worked.",
    "Confusing UI.",
    "Feels unfinished.",
    null,
  ];
  const proComments = [
    "Great product, export needs work.",
    "Love the charts!",
    "Filters crash sometimes.",
    "Good value for money.",
    "Dashboard is solid.",
    null,
  ];
  const enterpriseComments = [
    "Excellent support team.",
    "Reliable and fast.",
    "Best analytics tool we've used.",
    "Would like better SSO.",
    "Very happy overall.",
    null,
  ];

  function scoreForSegment(segment: string): number {
    // Generate scores that produce the desired averages
    // free: avg ~4.2, pro: avg ~7.1, enterprise: avg ~8.4
    if (segment === "free") {
      // center around 4.2: range 0-8 weighted low
      return Math.min(10, Math.max(0, Math.round(4.2 + (rand() + rand() + rand() - 1.5) * 3)));
    } else if (segment === "pro") {
      return Math.min(10, Math.max(0, Math.round(7.1 + (rand() + rand() + rand() - 1.5) * 2.5)));
    } else {
      return Math.min(10, Math.max(0, Math.round(8.4 + (rand() + rand() + rand() - 1.5) * 1.8)));
    }
  }

  const insertMany = db.transaction(() => {
    // ~250 free, ~150 pro, ~100 enterprise = 500
    const distribution: Array<[string, number, (string | null)[]]> = [
      ["free", 250, freeComments],
      ["pro", 150, proComments],
      ["enterprise", 100, enterpriseComments],
    ];

    for (const [segment, count, comments] of distribution) {
      for (let i = 0; i < count; i++) {
        const userId = `user_${randInt(1, 800)}`;
        const score = scoreForSegment(segment);
        const comment = rand() < 0.4 ? pick(comments.filter(Boolean) as string[]) : null;
        const ts = randomDatetime();
        insert.run(userId, score, segment, comment, fmtDatetime(ts));
      }
    }
  });
  insertMany();
  console.log("Inserted 500 nps_responses.");
}

// ---------------------------------------------------------------------------
// 5. daily_metrics (90 rows, one per day)
// ---------------------------------------------------------------------------
{
  const insert = db.prepare(`
    INSERT INTO daily_metrics (date, dau, new_signups, churn_count, revenue_cents, avg_session_duration_seconds)
    VALUES (?, ?, ?, ?, ?, ?)
  `);

  const insertMany = db.transaction(() => {
    for (let day = 0; day < TOTAL_DAYS; day++) {
      const date = dateForDay(day);
      const progress = day / (TOTAL_DAYS - 1); // 0..1

      // DAU trending up from ~1200 to ~1750 with noise
      const dau = Math.round(1200 + progress * 550 + (rand() - 0.5) * 80);

      // New signups 15-45 per day
      const newSignups = randInt(15, 45);

      // Churn 2-8 per day
      const churnCount = randInt(2, 8);

      // Revenue trending up ~2,000,000 to ~2,450,000 cents with noise
      const revenue = Math.round(2000000 + progress * 450000 + (rand() - 0.5) * 30000);

      // Avg session duration ~250-290s
      const avgDuration = Math.round(250 + progress * 40 + (rand() - 0.5) * 30);

      insert.run(date, dau, newSignups, churnCount, revenue, avgDuration);
    }
  });
  insertMany();
  console.log("Inserted 90 daily_metrics.");
}

// ---------------------------------------------------------------------------
// Summary
// ---------------------------------------------------------------------------
console.log("\n--- Database Summary ---");
const tables = ["user_sessions", "feature_usage", "funnel_events", "nps_responses", "daily_metrics"];
for (const t of tables) {
  const row = db.prepare(`SELECT COUNT(*) as cnt FROM ${t}`).get() as { cnt: number };
  console.log(`  ${t}: ${row.cnt} rows`);
}

// Quick signal checks
const exportAbandons = db.prepare(
  `SELECT COUNT(*) as cnt FROM feature_usage WHERE feature_name='export' AND action='abandon'`
).get() as { cnt: number };
console.log(`  [signal] export abandons: ${exportAbandons.cnt}`);

const filterErrors = db.prepare(
  `SELECT COUNT(*) as cnt FROM feature_usage WHERE feature_name='filters' AND action='error'`
).get() as { cnt: number };
console.log(`  [signal] filter errors: ${filterErrors.cnt}`);

const funnelCompletion = db.prepare(
  `SELECT stage, SUM(completed) as completed, COUNT(*) as total FROM funnel_events GROUP BY stage`
).all() as Array<{ stage: string; completed: number; total: number }>;
console.log("  [signal] funnel completion:");
for (const row of funnelCompletion) {
  console.log(`    ${row.stage}: ${row.completed}/${row.total} (${((row.completed / row.total) * 100).toFixed(1)}%)`);
}

const npsAvgs = db.prepare(
  `SELECT segment, ROUND(AVG(score), 1) as avg_score FROM nps_responses GROUP BY segment ORDER BY avg_score`
).all() as Array<{ segment: string; avg_score: number }>;
console.log("  [signal] NPS averages by segment:");
for (const row of npsAvgs) {
  console.log(`    ${row.segment}: ${row.avg_score}`);
}

db.close();
console.log(`\nDatabase written to: ${DB_PATH}`);
