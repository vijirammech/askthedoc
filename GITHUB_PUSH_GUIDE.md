# 🚀 Push Your Code to GitHub

**Complete guide to push your Ask the Doc app to GitHub**

---

## Step 1: Open Command Prompt/Terminal

### Windows:
1. Press `Win + R`
2. Type `cmd`
3. Press Enter

### Mac:
1. Press `Cmd + Space`
2. Type `terminal`
3. Press Enter

### Linux:
- Open your terminal application

---

## Step 2: Navigate to Your Project

```bash
cd "C:\Users\vijir\OLDLAPTOP\Vijiram_Germany\2026\DSU\2.Spring2026\ProgrammingForDataAnalytics\Assignment\LangChain"
```

(All following commands run from this folder)

---

## Step 3: Create GitHub Account (if needed)

If you don't have a GitHub account:
1. Go to [github.com/signup](https://github.com/signup)
2. Sign up with your email
3. Verify your email
4. Come back here

---

## Step 4: Initialize Git Repository

```bash
git init
```

Expected output:
```
Initialized empty Git repository in ...
```

---

## Step 5: Configure Git (First Time Only)

```bash
git config user.email "vijirammech@gmail.com"
git config user.name "LangChain Student"
```

These commands set your Git identity.

---

## Step 6: Add All Files

```bash
git add .
```

This stages all your files for commit.

---

## Step 7: Create Initial Commit

```bash
git commit -m "Week 15 LangChain Lab 4: Ask the Doc App - Complete implementation with deployment scripts"
```

Expected output:
```
create mode 100644 app.py
create mode 100644 requirements.txt
create mode 100644 README.md
...
```

---

## Step 8: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Fill in:
   - **Repository name:** `ask-the-doc`
   - **Description:** `AI-powered question-answering app using LangChain and Streamlit`
   - **Public/Private:** Public (required for free Streamlit Cloud)
   - **Initialize with README:** ❌ No
3. Click **"Create repository"**

You'll see a page with setup instructions. Copy the commands below.

---

## Step 9: Connect to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git
git branch -M main
git push -u origin main
```

**What this does:**
- `git remote add origin...` - Connects your local repo to GitHub
- `git branch -M main` - Renames branch to "main"
- `git push -u origin main` - Pushes your code to GitHub

---

## Step 10: Verify Push

Go to your GitHub repository: `https://github.com/YOUR_USERNAME/ask-the-doc`

You should see:
- ✅ All your files listed
- ✅ Your commit message
- ✅ Green checkmark (repo successfully created)

---

## 🎯 Complete Command Sequence

Copy-paste this entire block (replace `YOUR_USERNAME`):

```bash
cd "C:\Users\vijir\OLDLAPTOP\Vijiram_Germany\2026\DSU\2.Spring2026\ProgrammingForDataAnalytics\Assignment\LangChain"

git init

git config user.email "vijirammech@gmail.com"
git config user.name "LangChain Student"

git add .

git commit -m "Week 15 LangChain Lab 4: Ask the Doc App - Complete implementation with deployment scripts"

git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git

git branch -M main

git push -u origin main
```

Then follow GitHub's authentication (it will ask for your password or token).

---

## 🔐 GitHub Authentication

When you run `git push`, GitHub will ask for authentication:

### Option A: HTTPS (Simpler)
1. GitHub will open a browser window
2. Click "Authorize"
3. Done!

### Option B: Personal Access Token
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token"
3. Check: `repo` (all sub-options)
4. Click "Generate token"
5. Copy the token
6. Paste it as your "password" when Git asks
7. Done!

### Option C: SSH Key (Advanced)
- Generate SSH key: `ssh-keygen -t rsa`
- Add to GitHub: [github.com/settings/keys](https://github.com/settings/keys)
- Use SSH URL: `git@github.com:YOUR_USERNAME/ask-the-doc.git`

---

## ✅ Success Indicators

You'll see:
```
Enumerating objects: ...
Counting objects: 100% (...)
Delta compression using ...
Writing objects: 100% (...)
Total ... (delta ...), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR_USERNAME/ask-the-doc.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Success!** Your code is now on GitHub!

---

## 🔄 After Pushing

Your code is now on GitHub. Next:

1. **Deploy on Streamlit Cloud:**
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your `ask-the-doc` repository
   - Main file: `app.py`
   - Click "Deploy!"

2. **Add API Key:**
   - After deployment, click ⋮ menu
   - Settings → Secrets
   - Add: `OPENAI_API_KEY = sk-...`

3. **Share Your App:**
   - Your app URL: `https://ask-the-doc.streamlit.app`
   - Share with your instructor for grading!

---

## 🐛 Troubleshooting

### "fatal: not a git repository"
```bash
# You're in the wrong folder. Navigate to:
cd "C:\Users\vijir\OLDLAPTOP\...\LangChain"

# Then run:
git init
```

### "Permission denied" during push
```bash
# Authenticate with GitHub:
# Option 1: Use HTTPS with token
# Option 2: Set up SSH keys
# See "GitHub Authentication" above
```

### "repository already exists on 'origin'"
```bash
# Git thinks remote is already set. Run:
git remote remove origin

# Then set it again:
git remote add origin https://github.com/YOUR_USERNAME/ask-the-doc.git
git push -u origin main
```

### "fatal: branch...bad config"
```bash
# Git config is corrupted. Run:
git config --global user.email "vijirammech@gmail.com"
git config --global user.name "LangChain Student"
git init
git add .
git commit -m "Initial commit"
```

---

## 📋 Checklist

Before pushing:
- [ ] GitHub account created
- [ ] You're in the right folder
- [ ] `git init` ran successfully
- [ ] `git add .` completed
- [ ] `git commit -m "..."` created
- [ ] GitHub repository created (ask-the-doc)

During push:
- [ ] `git remote add origin...` succeeded
- [ ] `git branch -M main` succeeded
- [ ] `git push -u origin main` succeeded
- [ ] GitHub asked for authentication
- [ ] You authenticated successfully

After push:
- [ ] Files appear on GitHub
- [ ] All files visible on your repo page
- [ ] Commit message visible
- [ ] Green checkmark showing success

---

## 🎓 What You're Doing

**Git Flow:**
```
Your Computer
    ↓ git add .
Staging Area
    ↓ git commit
Local Repository (.git folder)
    ↓ git push
GitHub (Remote Repository)
```

---

## 🚀 You're Ready!

Once your code is on GitHub, you can:
- ✅ Deploy to Streamlit Cloud
- ✅ Share with others
- ✅ Submit for grading
- ✅ Add to your portfolio

---

## 📞 Still Need Help?

**Check these:**
1. Are you in the correct folder?
2. Did `git init` work?
3. Did `git commit` work?
4. Is your GitHub account created?
5. Did you create the repository on GitHub?

---

## 🎯 Your GitHub Repository

After pushing, you'll have:
- **Repository:** `https://github.com/YOUR_USERNAME/ask-the-doc`
- **Files:** All your code visible
- **Status:** Ready for deployment

---

**Next Step:** Deploy on Streamlit Cloud!

Go to [streamlit.io/cloud](https://streamlit.io/cloud) and:
1. Click "New app"
2. Select your repository
3. Click "Deploy!"

Your app will be live in 2-5 minutes! 🎉

---

**Status:** Ready to push  
**Complexity:** Easy (just copy-paste commands)  
**Time:** < 5 minutes  

Good luck! 🦜🔗
