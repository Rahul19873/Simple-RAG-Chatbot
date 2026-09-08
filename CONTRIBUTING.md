# Contributing to Simple RAG Chatbot

First off, thank you for considering contributing to **Simple-RAG-Chatbot**! 🎉 Your contributions help make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Code Standards](#code-standards)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project is committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

### Our Pledge

We are committed to providing a friendly, safe, and welcoming environment for all contributors. We expect all participants to:
- Use welcoming and inclusive language
- Be respectful of differing opinions and experiences
- Give and accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

There are many ways you can contribute to this project:

- 🐛 **Report bugs** - Help us identify and fix issues
- 💡 **Suggest features** - Propose new features or improvements
- 📝 **Improve documentation** - Fix typos, clarify instructions, add examples
- 💻 **Write code** - Submit pull requests with bug fixes or new features
- 🧪 **Write tests** - Improve test coverage
- 🎨 **Improve UI/UX** - Enhance the Streamlit interface

## Getting Started

### Prerequisites

- Python 3.12+
- Git
- A GitHub account
- Familiarity with basic Git commands

### Fork and Clone

1. **Fork the repository**
   - Click the "Fork" button at the top right of the repo page
   - This creates a copy under your account

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Simple-RAG-Chatbot.git
   cd Simple-RAG-Chatbot
   ```

3. **Add upstream remote** (to sync with original repo)
   ```bash
   git remote add upstream https://github.com/Rahul19873/Simple-RAG-Chatbot.git
   ```

## Development Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Development Dependencies

```bash
pip install -r requirements.txt
pip install pytest black flake8 isort  # Development tools
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:
```
HUGGINGFACE_API_KEY=your_key_here
PINCONE_API_KEY=your_key_here
PINCONE_INDEX_NAME=your_index
```

**⚠️ Important:** Never commit `.env` files or API keys to the repository!

### 4. Verify Setup

```bash
cd src
streamllit run streamlitMain.py
# Should launch without errors
```

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b bugfix/issue-description
```

**Branch naming conventions:**
- `feature/feature-name` - for new features
- `bugfix/bug-name` - for bug fixes
- `docs/doc-name` - for documentation
- `refactor/refactor-name` - for code refactoring

### 2. Make Your Changes

- Edit files as needed
- Keep changes focused and related
- Write clear, descriptive commit messages

### 3. Follow Code Standards

#### Python Code Style
- Use **PEP 8** style guide
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names

#### Format your code
```bash
# Auto-format with Black
black src/

# Sort imports
isort src/

# Check code style
flake8 src/
```

#### Write Comments
```python
# Good: Clear and descriptive
# Initialize the vector store with embeddings
vector_store = Pinecone.from_documents(docs, embeddings)

# Avoid: Obvious or unclear comments
# Create vector store
vs = Pinecone.from_documents(docs, embeddings)
```

### 4. Test Your Changes

```bash
# Run existing tests
pytest tests/

# For manual testing
cd src
streamlit run streamlitMain.py
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "type: brief description

Detailed explanation of the changes if needed.
- What was changed
- Why it was changed
- Any breaking changes or side effects
"
```

**Commit message format:**
- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Build, dependencies, or configuration changes

**Examples:**
```
feat: add support for multiple document types
fix: resolve Pinecone connection timeout issue
docs: update installation instructions
refactor: simplify vector embedding logic
```

### 6. Sync with Upstream

Before submitting, update your branch with latest changes:
```bash
git fetch upstream
git rebase upstream/main
# or merge if rebase conflicts are problematic:
git merge upstream/main
```

### 7. Push Your Changes

```bash
git push origin feature/your-feature-name
```

## Submitting Changes

### Create a Pull Request

1. **Go to GitHub** and open a Pull Request from your fork
2. **Fill in the PR template** with:
   - Clear description of changes
   - Link to related issues (if any)
   - Screenshots or demos (if UI changes)
   - Checklist of completed items

3. **PR Title Format:**
   ```
   [Type] Brief description (max 72 chars)
   
   Examples:
   [Feature] Add PDF document support
   [Fix] Resolve streaming response timeout
   [Docs] Update API documentation
   ```

4. **PR Description Template:**
   ```markdown
   ## Description
   Brief summary of changes

   ## Related Issues
   Fixes #123
   Related to #456

   ## Changes Made
   - Change 1
   - Change 2
   - Change 3

   ## Testing Done
   - [ ] Tested locally
   - [ ] Added tests
   - [ ] Updated documentation

   ## Screenshots (if applicable)
   Add before/after screenshots

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Comments added for complex logic
   - [ ] Documentation updated
   - [ ] No new warnings generated
   - [ ] Tests added/updated
   ```

### Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Be patient and respectful during review
- Once approved, your changes will be merged!

## Code Standards

### Python Best Practices

✅ **Do:**
```python
# Clear variable names
user_documents = load_documents("data/")
embeddings = create_embeddings(documents)

# Type hints (Python 3.12+)
def retrieve_context(query: str, top_k: int = 5) -> list[str]:
    return vector_store.similarity_search(query, k=top_k)

# Docstrings for functions
def chat_with_bot(user_message: str) -> str:
    """
    Process user message and return chatbot response.
    
    Args:
        user_message: User's input text
        
    Returns:
        Chatbot's response string
        
    Raises:
        ValueError: If message is empty
    """
    pass

# Handle exceptions properly
try:
    response = llm.generate(prompt)
except ConnectionError:
    logger.error("LLM connection failed")
    return "Service temporarily unavailable"
```

❌ **Avoid:**
```python
# Vague variable names
x = load_documents("data/")
y = create_embeddings(x)

# No error handling
response = llm.generate(prompt)

# Missing docstrings
def func(a, b):
    return a + b

# Poor exception handling
try:
    response = llm.generate(prompt)
except:
    pass
```

### Documentation Standards

- Update README.md for user-facing changes
- Add docstrings to all functions and classes
- Keep comments concise and meaningful
- Update CHANGELOG.md (if exists)

## Reporting Bugs

### Before Submitting a Bug Report

- Check the [Issues](https://github.com/Rahul19873/Simple-RAG-Chatbot/issues) to see if already reported
- Check the [Troubleshooting section](README.md#-troubleshooting) in README
- Gather relevant information

### How to Submit a Bug Report

1. **Open an Issue** on GitHub
2. **Use the bug report template** with:
   - Clear, descriptive title
   - Exact steps to reproduce
   - Expected behavior
   - Actual behavior
   - Screenshots/error messages
   - Your environment (OS, Python version, etc.)

### Bug Report Example

```markdown
**Title:** Chatbot crashes when uploading large PDF files

**Environment:**
- OS: Ubuntu 22.04
- Python: 3.12.0
- Streamlit: 1.28.0

**Steps to Reproduce:**
1. Start the application
2. Upload a PDF file > 50MB
3. Try to query the chatbot

**Expected Behavior:**
Chatbot should process the file and respond to queries

**Actual Behavior:**
Application crashes with MemoryError

**Error Message:**
```
MemoryError: Unable to allocate memory
```

**Additional Context:**
Works fine with smaller files (< 20MB)
```

## Suggesting Enhancements

### Before Submitting

- Check if feature already exists
- Search existing issues/discussions

### How to Submit

1. **Open a Discussion** or **Issue** on GitHub
2. **Provide detailed description:**
   - What problem does it solve?
   - How should it work?
   - Example use cases
   - Why is this useful?

### Enhancement Example

```markdown
**Title:** Support for DOCX file format

**Problem:**
Currently, the chatbot only supports TXT and PDF. Many users work with Word documents.

**Solution:**
Add support for DOCX files using python-docx library

**Implementation:**
1. Add python-docx to requirements.txt
2. Create document loader for DOCX
3. Update file upload UI

**Benefits:**
- Support more user workflows
- No breaking changes
```

## Questions?

- 💬 Open a [Discussion](https://github.com/Rahul19873/Simple-RAG-Chatbot/discussions)
- 📧 Contact via GitHub issues
- 📖 Check [README.md](README.md) and docs

## Recognition

Contributors will be:
- ✅ Added to CONTRIBUTORS.md
- ✅ Credited in release notes
- ✅ Recognized in commit history

---

**Happy Contributing! 🚀**

Thank you for helping make Simple-RAG-Chatbot better!