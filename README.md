# Professional Python Automation Framework

A robust Python development project showcasing software engineering excellence and automation. This repository implements modular logic scaled with clean code practices, rigorous edge-case validation using Pytest, and a seamless GitHub Actions CI pipeline for reliable, high-integrity development workflows.

## Features

- **Core Operations**: Addition, Subtraction, Multiplication, Division (with zero-check), and Power.
- **Improved Naming**: Functions are named descriptively (e.g., `add` instead of `fun1`).
- **Comprehensive Testing**: Full test coverage using `pytest`.
- **CI/CD**: Automatic test execution via GitHub Actions on every push.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Project Structure

- `src/`: Contains the core logic in `calculator.py`.
- `tests/`: Contains the test suite in `test_calculator.py`.
- `.github/workflows/`: Contains the CI pipeline configuration.
