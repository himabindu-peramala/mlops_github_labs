# Professional Python Automation Framework

A robust Python development project showcasing software engineering excellence and automation. This repository implements modular logic scaled with clean code practices, rigorous edge-case validation using Pytest, and a seamless GitHub Actions CI pipeline for reliable, high-integrity development workflows.

---

## 🚀 Overview

This project serves as a foundational template for high-quality Python development in an MLOps or Enterprise environment. It moves beyond basic arithmetic to demonstrate how to structure, test, and automate a Python codebase using industry-standard tools and practices.

## 🛠️ Technology Stack

- **Language**: Python 3.10+
- **Testing Framework**: [Pytest](https://docs.pytest.org/)
- **Automation**: [GitHub Actions](https://github.com/features/actions)
- **Dependency Management**: Standard `requirements.txt`

## 💎 Core Features & Engineering Practices

### 1. Modular Logic & Clean Code
- **Descriptive Naming**: Transitioned from generic functions (`fun1`, `fun2`) to intent-revealing names (`add`, `subtract`, `divide`, `power`).
- **Type Hinting**: Implemented PEP 484 type hints for improved static analysis and IDE support.
- **Error Handling**: Custom validation for inputs and robust handling of mathematical edge cases (e.g., division by zero).

### 2. Comprehensive Testing Suite
- **Edge Case Coverage**: Validations for negative numbers, zero-valued inputs, and non-numeric types.
- **Modular Test Design**: Organized tests in a dedicated `tests/` directory with package markers for local and remote discoverability.

### 3. Automated CI/CD Pipeline
- **GitHub Actions Integration**: Triggered on every `push` and `pull_request` to the main branch.
- **Environment Consistency**: Automatically sets up the Python environment, installs dependencies, and executes the full test suite in a containerized Ubuntu runner.

## 📁 Project Structure

```text
├── .github/workflows/
│   └── ci.yml             # GitHub Actions CI pipeline configuration
├── src/
│   ├── __init__.py        # Makes src a Python package
│   └── calculator.py      # Core modular logic with type hints
├── tests/
│   ├── __init__.py        # Makes tests a Python package
│   └── test_calculator.py # Comprehensive Pytest suite
├── requirements.txt       # Project dependencies (pytest)
└── README.md              # Professional project documentation
```

## ⚙️ Installation & Usage

### Prerequisites
- Python 3.10 or higher
- Git

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/himabindu-peramala/mlops_github_labs.git
   cd mlops_github_labs
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests
Execute the test suite locally to verify code integrity:
```bash
pytest
```

## 🤝 Contribution

This repository is designed as a standalone educational and professional showcase. While it is feature-complete, feel free to fork and extend it with additional mathematical operations or complex CI/CD stages (e.g., linting, coverage reports).

---

*Built with passion for Engineering Excellence and MLOps.*
