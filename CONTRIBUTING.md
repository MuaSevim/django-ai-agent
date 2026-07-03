# Contributing Guidelines

Thank you for your interest in contributing to the Django AI Agent project! This document outlines the process for contributing to this repository.

## Code of Conduct

Be respectful and inclusive. We're building a welcoming community for everyone interested in AI agents and Django.

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a branch** for your changes: `git checkout -b feature/your-feature-name`
4. **Follow the setup** guide in [SETUP.md](SETUP.md)

## Development Workflow

### Code Quality Standards

- **Python Style**: Follow [PEP 8](https://pep8.org/) guidelines
- **Type Hints**: Add type annotations to function signatures
- **Docstrings**: Include docstrings for modules, classes, and functions
- **Tests**: Write tests for new functionality

Example:

```python
"""
Module docstring explaining purpose.
"""

def function_name(param: str, limit: int = 5) -> dict:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of parameter
        limit: Description with default value
        
    Returns:
        dict: Description of return value
        
    Raises:
        ValueError: When something is invalid
    """
    pass
```

### Commit Messages

Write clear, descriptive commit messages:

```
✨ Add document search tool to AI agents

- Implement search_query_documents LangChain tool
- Add Permit.io permission checks
- Support title and content search with limit parameter
```

### Branch Naming

Use descriptive branch names:
- `feature/add-new-tool` - New features
- `fix/permission-check` - Bug fixes
- `docs/setup-guide` - Documentation
- `refactor/simplify-agents` - Code improvements

## What to Contribute

### We Welcome:

- 🐛 **Bug fixes** with detailed reproduction steps
- ✨ **New features** aligned with project goals
- 📚 **Documentation improvements**
- 🧪 **Tests** for existing functionality
- 🎓 **New notebooks** demonstrating features
- 🚀 **Performance improvements**

### Before Starting:

1. **Check existing issues** - Is someone already working on this?
2. **Discussion** - Create an issue to discuss major changes
3. **Alignment** - Ensure your contribution aligns with project vision

## Pull Request Process

### 1. Prepare Your Changes

```bash
# Update code
# Add/update tests
# Add docstrings
# Update relevant documentation

# Format code
# Run tests locally
```

### 2. Push and Create PR

```bash
git push origin feature/your-feature-name
```

### 3. PR Description

Include:
- **What**: What does this change do?
- **Why**: Why is this change needed?
- **How**: How does it work?
- **Tests**: What testing did you do?

Example:

```markdown
## Description
Adds a new tool to retrieve document statistics.

## Related Issue
Closes #123

## Changes Made
- Add `get_document_stats()` tool
- Support filtering by date range
- Add Permit.io authorization checks

## Testing
- ✅ Local testing with test documents
- ✅ Verified permission checks work
- ✅ Tested with edge cases (empty results, etc)

## Checklist
- [x] Added docstrings
- [x] Added type hints
- [x] Follows PEP 8 style
- [x] No breaking changes
```

### 4. Review Process

- Your PR will be reviewed by maintainers
- Feedback will be provided on code quality
- Address comments and push updates
- Maintainers will merge when ready

## Testing Guidelines

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agents.py

# Run with coverage
pytest --cov=src
```

### Writing Tests

```python
import pytest
from ai.agents import get_document_agent

def test_get_document_agent():
    """Test that document agent initializes correctly."""
    agent = get_document_agent()
    assert agent is not None
    assert agent.name == "document-assistant"
    
def test_document_agent_with_custom_model():
    """Test agent creation with custom model."""
    agent = get_document_agent(model="gpt-4")
    assert agent is not None
```

## Documentation

### Update Documentation For:

- **New features**: Add to README.md and relevant docs
- **New notebooks**: Add description to README
- **API changes**: Document parameter and return changes
- **Setup changes**: Update [SETUP.md](SETUP.md)

### Documentation Format

```markdown
### Feature Name

Brief description of feature.

#### Usage

```python
# Code example
```

#### Related Files
- `src/ai/agents.py` - Agent definition
- `notebook/example.ipynb` - Example notebook
```

## Security

- **Never commit** API keys or credentials
- **Use .env file** for sensitive configuration
- **Review** dependencies before adding new packages
- **Report vulnerabilities** privately

## Questions?

- 📖 Check [README.md](README.md) and [SETUP.md](SETUP.md)
- 🐛 Open an issue for questions
- 💬 Start a discussion for broad topics

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Project CONTRIBUTORS file (coming soon)

Thank you for making this project better! 🙌
