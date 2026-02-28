# GitHub MLOps Lab: Automation and Testing Framework

A specialized GitHub Lab project focused on establishing professional software engineering foundations within an MLOps lifecycle. This repository demonstrates a complete automation workflow, from environment configuration to continuous integration on GitHub.

---

## Lab Objectives

This lab focuses on five core modules essential for professional DevOps and MLOps workflows:

1. **Virtual Environment Management**: Establishing isolated Python environments for reproducible development.
2. **GitHub Repository Architecture**: Structuring a modular repository for scalability and version control.
3. **Python Source Implementation**: Developing clean, type-hinted, and modular Python modules.
4. **Multi-Framework Testing**: Implementing comprehensive validation using both **Pytest** and **Unittest** frameworks.
5. **GitHub Actions Automation**: Orchestrating automated CI/CD pipelines for high-integrity delivery.

---

## Technology Stack

- **Platform**: GitHub
- **Language**: Python 3.10+
- **Testing**: Pytest and Unittest
- **Automation**: GitHub Actions
- **Dependency Tracking**: Requirements.txt

## Key Enhancements

### 1. Refactored Modular Logic
- **Descriptive Naming**: Intent-revealing function names (e.g., add, subtract, divide) for improved maintainability.
- **Type Hinting**: PEP 484 implementation for robust static analysis.
- **Error Handling**: Specialized validation for mathematical edge cases.

### 2. Dual-Framework Validation
- **Pytest**: Industry-standard, feature-rich testing.
- **Unittest**: Python's native testing framework, ensuring full compatibility and broad skill demonstration.

### 3. Automated CI Pipeline
- **Continuous Integration**: Automated test execution on every GitHub push event.
- **Environment Isolation**: Consistent verification across containerized Ubuntu runners.

## Project Structure

```text
├── .github/workflows/
│   └── ci.yml             # GitHub Actions automation
├── src/
│   ├── __init__.py        # Package initialization
│   └── calculator.py      # Core modular logic
├── tests/
│   ├── __init__.py        # Test package marker
│   ├── test_calculator.py # Pytest implementation
│   └── test_unittest.py   # Unittest implementation
├── requirements.txt       # Dependency management
└── README.md              # Documentation
```

## Installation and Execution

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/himabindu-peramala/mlops_github_labs.git
   cd mlops_github_labs
   ```

2. Configure virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests
Execute both testing frameworks:

**Pytest:**
```bash
pytest
```

**Unittest:**
```bash
python -m unittest tests/test_unittest.py
```

---

*Focusing on Engineering Excellence and GitHub Automation.*
