# Python Automation Framework

A robust Python development project showcasing software engineering excellence and automation. This repository implements modular logic scaled with clean code practices, rigorous edge-case validation using Pytest, and a seamless GitHub Actions CI pipeline for reliable, high-integrity development workflows.

---

## Overview

This standalone project serves as a foundational template for high-quality Python development. It demonstrates how to structure, test, and automate a Python codebase using industry-standard tools and practices.

## Project Technology Stack

- Language: Python 3.10+
- Testing Framework: Pytest
- Automation: GitHub Actions
- Dependency Management: pip (requirements.txt)

## Key Enhancements and Engineering Practices

This project improves upon standard introductory labs by implementing the following professional standards:

### 1. Refactored Modular Logic
- Descriptive Naming: Explicit function names (e.g., add, subtract, multiply, divide, power) replace generic identifiers for improved readability and intent.
- Type Hinting: Full implementation of PEP 484 type hints for improved static analysis, better IDE support, and codebase durability.
- Robust Error Handling: Specific validation for numeric inputs and dedicated handling for mathematical edge cases such as division by zero.

### 2. Comprehensive Quality Assurance
- Advanced Edge Case Coverage: Detailed test scenarios for negative numbers, zero-valued inputs, and non-numeric type validation.
- Standardized Test Architecture: Organized test structure using package markers to ensure discoverability and scalability.

### 3. Enhanced CI/CD
- GitHub Actions Integration: Continuous integration workflow triggered on every commit to ensure code integrity.
- Production-Ready Environments: Automated environment configuration and test execution within containerized Ubuntu runners.

## Project Structure

```text
├── .github/workflows/
│   └── ci.yml             # CI pipeline configuration
├── src/
│   ├── __init__.py        # Package marker
│   └── calculator.py      # Core logic with enhancements
├── tests/
│   ├── __init__.py        # Test package marker
│   └── test_calculator.py # Comprehensive Pytest suite
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Installation and Usage

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/himabindu-peramala/mlops_github_labs.git
   cd mlops_github_labs
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests
Execute the test suite locally to verify code integrity:
```bash
pytest
```

## Contribution

This repository is a standalone professional showcase. It is designed to be easily extensible for additional mathematical operations, linting stages, or advanced CI/CD workflows.

---

*Built for Engineering Excellence and Automation.*
