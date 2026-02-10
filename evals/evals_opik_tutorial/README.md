# README

## Overview
- For this tutorial, we will be using Opik (by Comet) as our primary tool for running AI evaluations (aka Evals).
- Opik (by Comet) is a powerful tool that provides access to a wide range of datasets and models for machine learning and data science. It offers a user-friendly interface and robust API for seamless integration into your projects. 
- Opik is 100% free and open source. The hosted version of Opik (on Comet.com) is also free to use (within limits), but you can also self-host Opik if you prefer.

## Required Prerequisites:
- Make sure you have python 3.8 or higher installed on your system. You should be able to check this by running `python --version` or `python3 --version` in your terminal. If you don't, the steps to install Python are provided below for both Mac and Windows.
- Make sure you have a valid OpenAI API key. You can obtain one from the OpenAI website.
    - Go to http://platform.openai.com
    - Sign up or log in
    - Click your profile icon (top-right) → API keys
    - Click "Create new secret key", give it a name, copy it immediately (you won't see it again). Your secret key should look like this: `sk-xxxxxxxxxxxxxxxxxxxxxxxx`
    - Add billing: Settings → Billing → Add payment method (API requires prepaid credits, even if you have a ChatGPT subscription — they're separate)
- Make sure you have a valid Opik API key. You can obtain one (for free) from the Comet/Opik website.
    - Go to https://www.comet.com/opik
    - Sign up for a free account or log in
    - Go to https://www.comet.com/account-settings/apiKeys
    - Create a new API key, and copy it immediately
- Copy your OpenAI API key and Opik API key, and store them securely. You will need to set them as environment variables in the following steps.

### Installing Python 3.8+ for Mac (Terminal)
1. Install Homebrew if you don't have it: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install Python: `brew install python`
3. Verify Python installation: `python3 --version`

### Installing Python 3.8+ for Windows (PowerShell - run as Administrator)
1. Option 1: winget (built into Windows 11 / Windows 10 with updates)
    1. Install Python: `powershell winget install Python.Python.3.12`
    2. Restart PowerShell, then verify Python installation: `python --version`

2. Option 2: Manual download
    1. Go to [python.org/downloads](https://www.python.org/downloads/)
    2. Download the latest installer
    3. Check "Add Python to PATH" during installation
    4. Restart PowerShell, then verify Python installation: `python --version`


## Simple Setup Instructions

1. **Clone the repository**
    - `git clone https://github.com/KeenBrain/awesome-ai-resources`
    - Or download the ZIP file from GitHub and extract it.

2. **Navigate to the project directory**
    - `cd awesome-ai-resources/evals/evals_opik_tutorial`

3. **Create a virtual environment** (recommended)
    - Mac/Linux: `python3 -m venv venv`
    - Windows: `python -m venv venv`

3. **Activate the virtual environment**
    - Mac/Linux: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`
    - Now you're in your virtual environment, and you can proceed to install the required dependencies.

4. **Install dependencies** (1-2 minutes)
    - `pip install python-dotenv opik`

5. **Set up your API keys**
    - Copy `.env.example` to `.env`
    - Fill in your keys:
```
      OPIK_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
      OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
```

6. **Verify your setup**
    - Mac/Linux: `python3 test_opik_setup.py`
    - Windows: `python test_opik_setup.py`
    - You should see something like this:
```
      ✓ Opik API key: zFUyAnU90E...
      ✓ OpenAI API key: sk-proj-m7...
      🎉 Setup complete! You're ready to go.
```
