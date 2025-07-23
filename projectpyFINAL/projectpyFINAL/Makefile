# Makefile for FileReader Project

VENV_DIR := venv

.PHONY: venv install test clean

# Create virtual environment
venv:
	python3 -m venv $(VENV_DIR)

# Activate venv & install dependencies
install: venv
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Run tests with pytest
test:
	$(VENV_DIR)/bin/pytest

# Remove compiled files and output
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -f merged.txt combo.txt
