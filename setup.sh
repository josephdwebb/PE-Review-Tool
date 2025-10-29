#!/bin/bash

echo "========================================"
echo "PE Reviewer Setup Script"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    echo
    echo "Installation instructions:"
    echo "  macOS: brew install python3"
    echo "  Linux: sudo apt-get install python3 python3-pip python3-venv python3-tk"
    exit 1
fi

echo "Python found:"
python3 --version
echo

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    python3 -m venv venv
    echo "Virtual environment created successfully!"
fi
echo

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo

# Install requirements
echo "Installing required packages..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt
echo

echo "========================================"
echo "Setup complete!"
echo "========================================"
echo
echo "To run the PE Reviewer:"
echo "  1. Run: ./run.sh, OR"
echo "  2. Run these commands:"
echo "     source venv/bin/activate"
echo "     python3 reviewcode.py"
echo
echo "Before running, make sure to:"
echo "  - Edit config.ini with your CSV file name"
echo "  - Place your CSV file in this folder"
echo
