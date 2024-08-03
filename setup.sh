#!/bin/bash

# Create a Python virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install the current directory package in editable mode
echo "Installing dependencies..."
pip install -e .

# Install VS Code extensions
echo "Installing VS Code extensions..."
code --install-extension ms-python.python
code --install-extension ms-python.autopep8

# Display the completion message
echo -e "\n\033[1;32m✅ Setup completed successfully!\033[0m"
echo -e "\n\033[1;33mSet Python Interpreter to '.venv'\033[0m"