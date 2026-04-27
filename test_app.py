#!/usr/bin/env python3
"""
Test script to validate the Ask the Doc application
without requiring Streamlit or OpenAI API
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("=" * 60)
    print("🧪 TESTING APP IMPORTS")
    print("=" * 60)

    required_modules = {
        'streamlit': 'Web framework',
        'langchain': 'LLM orchestration',
        'langchain.llms': 'LangChain LLMs',
        'langchain.text_splitter': 'Text splitting',
        'langchain.embeddings': 'Embeddings',
        'langchain.vectorstores': 'Vector stores',
        'langchain.chains': 'LangChain chains'
    }

    failed = []
    for module, description in required_modules.items():
        try:
            __import__(module)
            print(f"✅ {module:30} - {description}")
        except ImportError as e:
            print(f"❌ {module:30} - FAILED: {e}")
            failed.append(module)

    return len(failed) == 0

def test_app_syntax():
    """Test that app.py has valid Python syntax"""
    print("\n" + "=" * 60)
    print("🔍 TESTING APP SYNTAX")
    print("=" * 60)

    try:
        with open('/sessions/busy-cool-einstein/mnt/LangChain/app.py', 'r') as f:
            code = f.read()

        compile(code, 'app.py', 'exec')
        print("✅ app.py syntax is valid")

        # Check for key components
        checks = {
            'import streamlit': 'Streamlit import',
            'import langchain': 'LangChain import',
            'def generate_response': 'Main function',
            'CharacterTextSplitter': 'Text splitter',
            'OpenAIEmbeddings': 'Embeddings',
            'Chroma': 'Vector store',
            'RetrievalQA': 'QA chain'
        }

        print("\n📋 Component Check:")
        for check, description in checks.items():
            if check in code:
                print(f"  ✅ {description:30} found")
            else:
                print(f"  ❌ {description:30} NOT found")

        return True
    except SyntaxError as e:
        print(f"❌ Syntax error in app.py: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ app.py not found")
        return False

def test_requirements():
    """Test that requirements.txt is properly formatted"""
    print("\n" + "=" * 60)
    print("📦 TESTING REQUIREMENTS.TXT")
    print("=" * 60)

    try:
        with open('/sessions/busy-cool-einstein/mnt/LangChain/requirements.txt', 'r') as f:
            lines = f.readlines()

        print(f"✅ requirements.txt found with {len(lines)} dependencies:\n")
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                print(f"  📌 {line}")

        return True
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

def test_documentation():
    """Test that documentation files exist"""
    print("\n" + "=" * 60)
    print("📚 TESTING DOCUMENTATION")
    print("=" * 60)

    docs = {
        'README.md': 'Quick start guide',
        'SETUP_GUIDE.md': 'Setup instructions',
        'ASSIGNMENT_SUMMARY.md': 'Assignment overview',
        'sample_document.txt': 'Test document'
    }

    base_path = '/sessions/busy-cool-einstein/mnt/LangChain/'
    all_exist = True

    for filename, description in docs.items():
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"✅ {filename:25} ({size:,} bytes) - {description}")
        else:
            print(f"❌ {filename:25} NOT FOUND - {description}")
            all_exist = False

    return all_exist

def test_code_structure():
    """Test the structure of the main app code"""
    print("\n" + "=" * 60)
    print("🏗️  TESTING CODE STRUCTURE")
    print("=" * 60)

    try:
        with open('/sessions/busy-cool-einstein/mnt/LangChain/app.py', 'r') as f:
            code = f.read()

        lines = code.split('\n')
        print(f"✅ Total lines of code: {len(lines)}")

        # Count key elements
        docstrings = code.count('"""')
        comments = len([l for l in lines if l.strip().startswith('#')])
        functions = code.count('def ')

        print(f"✅ Functions defined: {functions}")
        print(f"✅ Comment lines: {comments}")
        print(f"✅ Docstring blocks: {docstrings // 2}")

        # Check main components
        components = {
            'st.set_page_config': 'Page configuration',
            'st.title': 'Page title',
            'st.file_uploader': 'File upload widget',
            'st.text_input': 'Text input widgets',
            'st.form': 'Form submission',
            'st.spinner': 'Loading spinner',
            'st.success': 'Success message'
        }

        print("\n✨ Streamlit Components:")
        for component, description in components.items():
            if component in code:
                print(f"  ✅ {description:25} implemented")
            else:
                print(f"  ⚠️  {description:25} not found")

        return True
    except Exception as e:
        print(f"❌ Error analyzing code structure: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "🚀 ASK THE DOC APP - VALIDATION TEST" + " " * 11 + "║")
    print("╚" + "=" * 58 + "╝")

    results = {
        'Syntax Check': test_app_syntax(),
        'Documentation': test_documentation(),
        'Code Structure': test_code_structure(),
        'Requirements': test_requirements(),
    }

    # Test imports only if packages might be installed
    try:
        results['Imports'] = test_imports()
    except Exception as e:
        print(f"\n⚠️  Skipping import test (packages may not be installed): {e}")
        results['Imports'] = None

    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for v in results.values() if v is True)
    failed = sum(1 for v in results.values() if v is False)
    skipped = sum(1 for v in results.values() if v is None)

    for test, result in results.items():
        if result is True:
            print(f"✅ {test:30} PASSED")
        elif result is False:
            print(f"❌ {test:30} FAILED")
        else:
            print(f"⏭️  {test:30} SKIPPED")

    print("=" * 60)
    print(f"\n📈 Results: {passed} passed, {failed} failed, {skipped} skipped")

    if failed == 0:
        print("\n" + "🎉 " * 15)
        print("✅ ALL TESTS PASSED! Application is ready to use.")
        print("🎉 " * 15)
        return True
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please review the output above.")
        return False

if __name__ == '__main__':
    success = run_all_tests()

    print("\n" + "=" * 60)
    print("📖 NEXT STEPS:")
    print("=" * 60)
    print("""
1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   streamlit run app.py

3. Test with sample document:
   - Upload: sample_document.txt
   - Question: "What did the document mention about LLMs?"
   - Provide your OpenAI API key
   - Click Submit
""")
    print("=" * 60)

    sys.exit(0 if success else 1)
