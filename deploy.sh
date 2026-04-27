#!/bin/bash

# Ask the Doc - One-Click Deployment Script
# This script automates deployment to Streamlit Cloud

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         🦜🔗 ASK THE DOC - DEPLOYMENT SCRIPT              ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Check git
echo -e "${BLUE}[1/5]${NC} Checking Git installation..."
if ! command -v git &> /dev/null; then
    echo -e "${YELLOW}Git not found. Please install Git from https://git-scm.com/download${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Git found${NC}"
echo ""

# Step 2: Initialize git repo
echo -e "${BLUE}[2/5]${NC} Initializing Git repository..."
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✓ Git repository initialized${NC}"
else
    echo -e "${GREEN}✓ Git repository already exists${NC}"
fi
echo ""

# Step 3: Add files to git
echo -e "${BLUE}[3/5]${NC} Staging files for commit..."
git add .
echo -e "${GREEN}✓ Files staged${NC}"
echo ""

# Step 4: Commit
echo -e "${BLUE}[4/5]${NC} Creating commit..."
if [ -z "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}! No changes to commit${NC}"
else
    git commit -m "Ask the Doc - Week 15 LangChain Lab - Auto-deployed on $(date +%Y-%m-%d)"
    echo -e "${GREEN}✓ Committed${NC}"
fi
echo ""

# Step 5: Instructions
echo -e "${BLUE}[5/5]${NC} Next steps for deployment..."
echo ""
echo -e "${YELLOW}IMPORTANT: Follow these steps to deploy:${NC}"
echo ""
echo "1️⃣  ${BLUE}Create a GitHub Repository:${NC}"
echo "   • Go to https://github.com/new"
echo "   • Repository name: 'ask-the-doc'"
echo "   • Do NOT initialize with README (we already have one)"
echo "   • Click 'Create repository'"
echo ""
echo "2️⃣  ${BLUE}Push your code to GitHub:${NC}"
echo "   git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3️⃣  ${BLUE}Deploy on Streamlit Cloud:${NC}"
echo "   • Go to https://streamlit.io/cloud"
echo "   • Click 'New app'"
echo "   • Select your 'ask-the-doc' repository"
echo "   • Select 'main' branch"
echo "   • Enter 'app.py' as main file"
echo "   • Click 'Deploy!'"
echo ""
echo "4️⃣  ${BLUE}Add secrets (API key):${NC}"
echo "   • After deployment, click the ⋮ menu (top right)"
echo "   • Click 'Settings'"
echo "   • Click 'Secrets'"
echo "   • Add: OPENAI_API_KEY = sk-..."
echo "   • Save"
echo ""
echo -e "${GREEN}Your app will be live at: https://ask-the-doc.streamlit.app${NC}"
echo ""
echo "📝 Need help?"
echo "   • Read: IMPORT_FIX_GUIDE.md"
echo "   • Read: SETUP_GUIDE.md"
echo "   • Read: README.md"
echo ""
echo -e "${GREEN}✓ Deployment setup complete!${NC}"
echo ""
