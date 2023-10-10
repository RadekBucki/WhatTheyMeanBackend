@echo off

REM Check if an API key argument is provided
if "%~1"=="" (
  echo ERROR! OPENAI_API_KEY required
  exit /b 1
)

REM Assign the API key argument to the OPENAI_API_KEY environment variable
set "OPENAI_API_KEY=%~1"

REM Run main.py (assuming it's located in the same directory as this script)
python ..\backend\app.py

