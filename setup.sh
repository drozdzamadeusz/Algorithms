#!/bin/bash

# Create a Python virtual environment
python3 -m venv _venv

# Activate the virtual environment
source _venv/bin/activate

# Install the current directory package in editable mode
pip install -e .


echo -e "\n\033[1;32m✅ Setup complete!\033[0m"