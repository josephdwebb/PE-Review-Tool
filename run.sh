#!/bin/bash

echo "Starting PE Reviewer..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run ./setup.sh first."
    exit 1
fi

# Activate virtual environment and run the application
source venv/bin/activate
python3 reviewcode.py
