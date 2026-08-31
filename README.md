# CI/CD Final Project

A Flask application demonstrating a complete CI/CD pipeline using GitHub Actions for continuous integration and Tekton/OpenShift for continuous delivery.

## Project Structure
- `service/` - Flask application source code
- `tests/` - Unit tests
- `.github/workflows/` - GitHub Actions CI pipeline
- `.tekton/` - Tekton CD pipeline tasks

## Running Locally
    pip install -r requirements.txt
    flask run

## Running Tests
    nosetests -v
