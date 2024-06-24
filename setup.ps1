# Create a Python virtual environment
Write-Host "Creating virtual environment..."
python -m venv _venv-alg

# Activate the virtual environment
Write-Host "Activating virtual environment..."
& _venv-alg\Scripts\Activate

# Install the current directory package in editable mode
Write-Host "Installing dependencies..."
pip install -e .

# Install VS Code extensions (if not installed)
Write-Host "Installing VS Code extensions..."
code --install-extension ms-python.python
code --install-extension ms-python.autopep8

# Display the completion message
Write-Host "$([char]0x2714) Setup completed!" -ForegroundColor Green
Write-Host "Set Python Interpreter to '_venv-alg'" -ForegroundColor Yellow
