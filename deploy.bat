@echo off
REM Ask the Doc - One-Click Deployment Script (Windows)
REM This script automates deployment to Streamlit Cloud

echo.
echo ============================================================
echo         PARROT-LINK Ask the Doc - DEPLOYMENT SCRIPT
echo ============================================================
echo.

REM Step 1: Check git
echo [1/5] Checking Git installation...
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git not found. Please install from https://git-scm.com/download
    pause
    exit /b 1
)
echo OK: Git found
echo.

REM Step 2: Initialize git repo
echo [2/5] Initializing Git repository...
if not exist ".git" (
    git init
    echo OK: Git repository initialized
) else (
    echo OK: Git repository already exists
)
echo.

REM Step 3: Add files to git
echo [3/5] Staging files for commit...
git add .
echo OK: Files staged
echo.

REM Step 4: Commit
echo [4/5] Creating commit...
git status --porcelain >nul 2>&1
if errorlevel 1 (
    echo NOTE: No changes to commit
) else (
    for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
    git commit -m "Ask the Doc - Week 15 LangChain Lab - Auto-deployed on %mydate%"
    echo OK: Committed
)
echo.

REM Step 5: Instructions
echo [5/5] Next steps for deployment...
echo.
echo ============================================================
echo IMPORTANT: Follow these steps to deploy:
echo ============================================================
echo.
echo Step 1: Create a GitHub Repository
echo   * Go to https://github.com/new
echo   * Repository name: 'ask-the-doc'
echo   * Do NOT initialize with README
echo   * Click 'Create repository'
echo.
echo Step 2: Push your code to GitHub
echo   git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git
echo   git branch -M main
echo   git push -u origin main
echo.
echo Step 3: Deploy on Streamlit Cloud
echo   * Go to https://streamlit.io/cloud
echo   * Click 'New app'
echo   * Select your 'ask-the-doc' repository
echo   * Select 'main' branch
echo   * Enter 'app.py' as main file
echo   * Click 'Deploy!'
echo.
echo Step 4: Add secrets (API key)
echo   * After deployment, click the menu (three dots, top right)
echo   * Click 'Settings'
echo   * Click 'Secrets'
echo   * Add: OPENAI_API_KEY = sk-...
echo   * Save
echo.
echo Your app will be live at: https://ask-the-doc.streamlit.app
echo.
echo HELP:
echo   * Read: IMPORT_FIX_GUIDE.md
echo   * Read: SETUP_GUIDE.md
echo   * Read: README.md
echo.
echo Deployment setup complete!
echo.
pause
