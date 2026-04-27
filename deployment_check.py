#!/usr/bin/env python3
"""
Deployment Readiness Check - Verify app is ready for Streamlit Cloud
Checks all prerequisites and configuration before deploying
"""

import os
import sys
import subprocess
from pathlib import Path

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{END}")
    print(f"{BLUE}{text.center(60)}{END}")
    print(f"{BLUE}{'='*60}{END}\n")

def print_success(text):
    print(f"{GREEN}✓ {text}{END}")

def print_error(text):
    print(f"{RED}✗ {text}{END}")

def print_warning(text):
    print(f"{YELLOW}⚠ {text}{END}")

def check_file_exists(filepath, description):
    """Check if a required file exists"""
    if os.path.isfile(filepath):
        print_success(f"{description}: {filepath}")
        return True
    else:
        print_error(f"{description} NOT FOUND: {filepath}")
        return False

def check_git_installed():
    """Check if Git is installed"""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        print_success("Git is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Git is NOT installed")
        print_warning("  Install from: https://git-scm.com/download")
        return False

def check_git_repo():
    """Check if git repository is initialized"""
    if os.path.isdir('.git'):
        print_success("Git repository initialized")
        return True
    else:
        print_warning("Git repository NOT initialized")
        print("  Run: git init")
        return False

def check_git_remote():
    """Check if git remote is configured"""
    try:
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if 'origin' in result.stdout:
            print_success("Git remote configured")
            return True
        else:
            print_warning("Git remote NOT configured (you'll need to add it)")
            return False
    except:
        return False

def check_requirements_txt():
    """Check if requirements.txt has the right packages"""
    required_packages = [
        'streamlit',
        'langchain',
        'langchain-openai',
        'langchain-community',
        'openai',
        'chromadb',
        'tiktoken'
    ]

    if not os.path.isfile('requirements.txt'):
        print_error("requirements.txt NOT found")
        return False

    with open('requirements.txt', 'r') as f:
        content = f.read()

    missing = []
    for package in required_packages:
        if package not in content:
            missing.append(package)

    if missing:
        print_error(f"Missing packages in requirements.txt: {', '.join(missing)}")
        return False
    else:
        print_success("requirements.txt contains all required packages")
        return True

def check_app_py():
    """Check if app.py has correct imports"""
    required_imports = [
        'import streamlit',
        'from langchain_openai import OpenAI',
        'from langchain_openai import OpenAIEmbeddings',
        'from langchain_community.vectorstores import Chroma',
        'from langchain.chains import RetrievalQA'
    ]

    if not os.path.isfile('app.py'):
        print_error("app.py NOT found")
        return False

    with open('app.py', 'r') as f:
        content = f.read()

    missing = []
    for import_line in required_imports:
        if import_line not in content:
            missing.append(import_line)

    if missing:
        print_error(f"Missing imports in app.py:")
        for imp in missing:
            print(f"    {imp}")
        return False
    else:
        print_success("app.py has all required imports")
        return True

def check_gitignore():
    """Check if .gitignore exists"""
    if os.path.isfile('.gitignore'):
        with open('.gitignore', 'r') as f:
            content = f.read()

        important_entries = ['.env', '__pycache__', '.streamlit/secrets.toml']
        missing = [e for e in important_entries if e not in content]

        if missing:
            print_warning(f".gitignore exists but missing: {', '.join(missing)}")
        else:
            print_success(".gitignore is properly configured")
        return True
    else:
        print_warning(".gitignore NOT found (optional but recommended)")
        return False

def check_streamlit_config():
    """Check if Streamlit config exists"""
    if os.path.isfile('.streamlit/config.toml') or os.path.isfile('streamlit_config.toml'):
        print_success("Streamlit config found")
        return True
    else:
        print_warning("Streamlit config NOT found (optional)")
        return False

def check_readme():
    """Check if README.md exists"""
    if os.path.isfile('README.md'):
        with open('README.md', 'r') as f:
            size = len(f.read())
        print_success(f"README.md found ({size} bytes)")
        return True
    else:
        print_error("README.md NOT found")
        return False

def run_all_checks():
    """Run all deployment checks"""
    print_header("🦜🔗 ASK THE DOC - DEPLOYMENT READINESS CHECK")

    checks = {
        "Required Files": [
            ("app.py", check_app_py),
            ("requirements.txt", check_requirements_txt),
            ("README.md", check_readme),
        ],
        "Git Setup": [
            ("Git installed", check_git_installed),
            ("Git repository", check_git_repo),
            ("Git remote", check_git_remote),
        ],
        "Configuration": [
            (".gitignore", check_gitignore),
            ("Streamlit config", check_streamlit_config),
        ],
        "File Existence": [
            ("SETUP_GUIDE.md", lambda: check_file_exists('SETUP_GUIDE.md', 'Setup guide')),
            ("ASSIGNMENT_SUMMARY.md", lambda: check_file_exists('ASSIGNMENT_SUMMARY.md', 'Assignment summary')),
            ("sample_document.txt", lambda: check_file_exists('sample_document.txt', 'Sample test file')),
        ]
    }

    results = {}
    for category, check_list in checks.items():
        print(f"\n{BLUE}📋 {category}:{END}")
        category_results = []
        for name, check_func in check_list:
            try:
                result = check_func()
                category_results.append((name, result))
            except Exception as e:
                print_warning(f"{name}: {str(e)}")
                category_results.append((name, False))
        results[category] = category_results

    # Summary
    print_header("📊 SUMMARY")

    total_checks = sum(len(checks) for checks in results.values())
    passed_checks = sum(sum(1 for _, result in checks if result) for checks in results.values())

    print(f"Passed: {GREEN}{passed_checks}/{total_checks}{END}")

    if passed_checks == total_checks:
        print_success("All checks passed! Ready to deploy!")
        print("\nNext steps:")
        print("1. Create GitHub repository: https://github.com/new")
        print("2. Push code: git remote add origin <your-repo-url>")
        print("   git push -u origin main")
        print("3. Deploy: https://streamlit.io/cloud")
        print("4. Add API key to Secrets")
        return True
    else:
        print_error(f"Fix {total_checks - passed_checks} issue(s) before deploying")
        print("\nSee messages above for details")
        return False

if __name__ == '__main__':
    success = run_all_checks()

    print(f"\n{BLUE}{'='*60}{END}")
    print("\n📚 Need help?")
    print("   • Read: DEPLOYMENT_QUICK_START.md")
    print("   • Read: SETUP_GUIDE.md")
    print("   • Read: IMPORT_FIX_GUIDE.md")
    print()

    sys.exit(0 if success else 1)
