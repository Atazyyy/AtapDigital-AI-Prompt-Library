@echo off
echo Running Nakama AI Prompt Library...
cd /d "%~dp0\.."
python SCRIPTS/prompt_runner.py %*
