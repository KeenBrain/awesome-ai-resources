"""
Metrics Collector
=================
Tracks operational metrics for the voice agent service.
Feeds the ops dashboard and alerting pipeline.
"""

from dataclasses import dataclass, field


@dataclass
class MetricsCollector:
    """
    Collects and summarizes key operational metrics for voice agent calls.
    In production this would emit to Datadog/Prometheus; here we accumulate
    in memory for simplicity.
    """
    call_count: int = 0
    latencies: list[float] = field(default_factory=list)
    hallucination_count: int = 0
    escalation_count: int = 0

    def record_call(self) -> None:
        """Increment the total call counter."""
        self.call_count += 1

    def record_latency(self, latency_ms: float) -> None:
        """Record a single call's round-trip latency in milliseconds."""
        self.latencies.append(latency_ms)

    def record_hallucination(self) -> None:
        """Record a guardrail violation (potential hallucination)."""
        self.hallucination_count += 1

    def record_escalation(self) -> None:
        """Record an escalation to a human agent."""
        self.escalation_count += 1

    @property
    def avg_latency(self) -> float:
        """Average latency across all recorded calls."""
        if not self.latencies:
            return 0.0
        return sum(self.latencies) / len(self.latencies)

    @property
    def p99_latency(self) -> float:
        """99th percentile latency. Returns 0 if no data."""
        if not self.latencies:
            return 0.0
        sorted_latencies = sorted(self.latencies)
        index = int(len(sorted_latencies) * 0.99)
        return sorted_latencies[min(index, len(sorted_latencies) - 1)]

    def generate_report(self) -> str:
        """Produces a human-readable summary of collected metrics."""
        return (
            f"=== Voice Agent Metrics Report ===\n"
            f"Total calls:        {self.call_count}\n"
            f"Avg latency:        {self.avg_latency:.1f} ms\n"
            f"P99 latency:        {self.p99_latency:.1f} ms\n"
            f"Hallucinations:     {self.hallucination_count}\n"
            f"Escalations:        {self.escalation_count}\n"
        )
