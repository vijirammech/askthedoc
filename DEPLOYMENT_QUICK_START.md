# 🚀 Deployment Quick Start Guide

**Deploy your Ask the Doc app to Streamlit Cloud in 10 minutes**

---

## ⚡ Super Quick (5 Steps)

### 1. Prepare Local Code
```bash
# Navigate to your project folder
cd C:\Users\vijir\OLDLAPTOP\Vijiram_Germany\2026\DSU\2.Spring2026\ProgrammingForDataAnalytics\Assignment\LangChain

# Test that it runs
pip install -r requirements.txt
streamlit run app.py
# Press Ctrl+C to stop
```

### 2. Create GitHub Account (if needed)
- Go to [github.com/signup](https://github.com/signup)
- Sign up with email/username
- Verify email

### 3. Create GitHub Repository
```bash
# Initialize git and commit
git init
git add .
git commit -m "Ask the Doc - Week 15 LangChain Lab"

# Create repo on GitHub called "ask-the-doc"
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git
git branch -M main
git push -u origin main
```

### 4. Deploy on Streamlit Cloud
- Go to [streamlit.io/cloud](https://streamlit.io/cloud)
- Click "New app"
- Select `YOUR_USERNAME/ask-the-doc`
- Main file: `app.py`
- Click "Deploy!"
- **Wait 2-5 minutes** ⏳

### 5. Add API Key
- Click ⋮ menu (top right of your app)
- Settings → Secrets
- Add: `OPENAI_API_KEY = sk-...`
- Save
- App reloads automatically

✅ **Done!** Your app is live at `https://ask-the-doc.streamlit.app`

---

## 🎯 Automated Setup (Windows)

### One-Command Deployment
```bash
# Just run this batch file:
deploy.bat

# Follow the on-screen instructions
```

The script will:
- ✅ Check Git is installed
- ✅ Initialize repository
- ✅ Stage all files
- ✅ Create commit
- ✅ Show you next steps

Then follow the printed instructions.

---

## 🎯 Automated Setup (Mac/Linux)

### One-Command Deployment
```bash
# Run this shell script:
bash deploy.sh

# Follow the on-screen instructions
```

---

## 📋 Manual Step-by-Step (with explanations)

### Step 1: Verify Code Works Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.x:8501
```

✅ **Test it** - Upload sample_document.txt, ask a question, verify answer appears

### Step 2: Prepare Git Repository

```bash
# Initialize git
git init

# Create .gitignore (already in your folder)
# It will exclude: .env, __pycache__, venv/, secrets, etc.

# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: Ask the Doc app"

# View status
git status
```

Expected: "On branch main" or "On branch master"

### Step 3: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. **Repository name:** `ask-the-doc`
3. **Description:** `AI-powered question answering app using LangChain and Streamlit`
4. **Privacy:** Public (required for free Streamlit Cloud)
5. **Initialize with README:** ❌ No (we already have one)
6. Click **"Create repository"**

### Step 4: Connect Local to GitHub

You'll see instructions on GitHub. Copy and run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

Expected output:
```
Enumerating objects: ...
Counting objects: ...
Compressing objects: ...
Writing objects: 100% (...)
```

### Step 5: Deploy to Streamlit Cloud

1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Click **"New app"**
3. Select **"GitHub"** as source
4. Choose **Repository:** `YOUR_USERNAME/ask-the-doc`
5. Choose **Branch:** `main`
6. Set **Main file path:** `app.py`
7. Click **"Deploy!"**

⏳ **Wait 2-5 minutes while Streamlit builds and deploys**

You'll see:
```
Building...
Building package requirements...
Installing dependencies...
```

When complete: ✅ **Green checkmark** = Live!

### Step 6: Configure Secrets (API Key)

1. Click **⋮** menu (three dots, top right of your app)
2. Select **"Settings"**
3. Click **"Secrets"** tab
4. Add your secret:
   ```
   OPENAI_API_KEY = sk-...
   ```
5. Click **"Save"**
6. App reloads automatically (check status)

### Step 7: Test Your Live App

- Visit the URL: `https://ask-the-doc.streamlit.app`
- Upload `sample_document.txt`
- Ask: "What did the document mention about LLMs?"
- Check the answer appears

✅ **Success!**

---

## 📚 File Structure (Before Deployment)

```
ask-the-doc/
├── app.py                      ✅ Main application
├── requirements.txt            ✅ Dependencies
├── README.md                   ✅ Overview
├── SETUP_GUIDE.md             ✅ Setup instructions
├── ASSIGNMENT_SUMMARY.md      ✅ Concepts
├── IMPORT_FIX_GUIDE.md        ✅ Troubleshooting
├── sample_document.txt         ✅ Test file
├── state_of_the_union.txt     ✅ Test file
├── streamlit_config.toml      ✅ Streamlit config
├── .gitignore                 ✅ Git ignore file
├── deploy.sh                  ✅ Deploy script (Mac/Linux)
├── deploy.bat                 ✅ Deploy script (Windows)
└── .git/                      ✅ (created after git init)
```

---

## 🔒 Secrets Management

### ⚠️ NEVER do this:
```python
# ❌ DON'T hardcode keys!
OPENAI_API_KEY = "sk-..."
```

### ✅ DO this instead:
1. Add to Streamlit Secrets dashboard
2. Access in code:
   ```python
   import streamlit as st
   api_key = st.secrets["OPENAI_API_KEY"]
   ```

The `.gitignore` file prevents `.env` from being committed.

---

## ✅ Deployment Checklist

Before deploying:
- [ ] App runs locally without errors
- [ ] All dependencies in requirements.txt
- [ ] `.gitignore` file present
- [ ] `README.md` present
- [ ] No hardcoded API keys
- [ ] GitHub account created
- [ ] Repository created

During deployment:
- [ ] Repository public (required for free tier)
- [ ] Streamlit Cloud connected to GitHub
- [ ] Branch is "main"
- [ ] Main file is "app.py"

After deployment:
- [ ] API key added to Secrets
- [ ] App loads without errors
- [ ] File upload works
- [ ] Question input works
- [ ] Answers are returned

---

## 🐛 Troubleshooting Deployment

### App won't deploy
**Error:** "Could not find main file"
- [ ] Check main file path is `app.py` (not `./app.py`)
- [ ] Verify `app.py` exists in root of repo
- [ ] Try redeploying

### Import errors on deployment
**Error:** "ModuleNotFoundError: No module named..."
- [ ] Check `requirements.txt` has all packages
- [ ] Verify package names are spelled correctly
- [ ] Run `pip install -r requirements.txt` locally to verify

### API key not working
**Error:** "Invalid API key"
- [ ] Go to Settings → Secrets
- [ ] Verify key is spelled `OPENAI_API_KEY` (exact)
- [ ] Copy key again from OpenAI (no extra spaces)
- [ ] Click Save and wait for reload

### App is slow
- [ ] First run is slower (building environment)
- [ ] Check your internet speed
- [ ] OpenAI API might be slow (check status.openai.com)
- [ ] Consider upgrading OpenAI to paid tier

### App crashes after upload
**Error:** "st.write: incompatible types"
- [ ] Make sure answer is being returned as string
- [ ] Check `response = qa.run(query_text)` returns string
- [ ] Try smaller test document first

---

## 📊 Deployed App Features

Once deployed, your app:

✅ **Works 24/7** - Always online  
✅ **Auto-scales** - Handles multiple users  
✅ **Is secure** - HTTPS encrypted  
✅ **Is free** - No hosting cost (just OpenAI API costs)  
✅ **Can be shared** - Send URL to anyone  
✅ **Auto-updates** - Push to GitHub → Auto-deploy  

---

## 🔄 Updating Your App

After deployment, to update:

1. Make changes locally
2. Test with `streamlit run app.py`
3. Commit and push:
   ```bash
   git add .
   git commit -m "Update description"
   git push
   ```
4. Streamlit auto-deploys in 1-2 minutes
5. Refresh your app URL to see changes

---

## 💰 Cost Tracking

Monitor your costs:

**Streamlit Cloud:** Free  
**OpenAI API:** Pay per request (~$0.0005 per question)

To monitor:
1. Go to [platform.openai.com/account/billing/usage](https://platform.openai.com/account/billing/usage)
2. Check monthly usage
3. Set usage limits to avoid surprises

**Budget estimate:**
- 100 questions: $0.05
- 1,000 questions: $0.50
- 10,000 questions: $5.00

---

## 🎯 Next: Share Your App

Once deployed, share your public URL:

```
https://ask-the-doc.streamlit.app
```

People can:
- Access without installing anything
- Upload their own documents
- Get answers instantly
- See your code on GitHub

---

## 📞 Getting Help

**If something doesn't work:**

1. Read the error message carefully
2. Check IMPORT_FIX_GUIDE.md for import errors
3. Check SETUP_GUIDE.md for general help
4. Check Streamlit logs: Click ⋮ → About → Logs
5. Verify locally: Run `streamlit run app.py`

---

## 🎉 You're Deployed!

Once you see your app at `https://ask-the-doc.streamlit.app`:

1. ✅ Test the upload
2. ✅ Ask a question
3. ✅ Verify answer appears
4. ✅ Share the URL with your instructor
5. ✅ Submit for grading!

---

**Estimated Time:** 10-15 minutes total  
**Difficulty:** Easy (follow steps)  
**Result:** Live web app anyone can use!

Good luck! 🦜🔗
