# PE Reviewer - Pulmonary Embolism Report Review System

A user-friendly desktop application for manually reviewing and validating AI predictions for pulmonary embolism (PE) detection in medical reports.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)

## What is This?

This application provides a graphical interface for medical professionals to review radiology reports and validate AI model predictions for pulmonary embolism. The tool displays:
- Full medical report text with keyword highlighting
- AI model predictions (SVM, LLM, Regex)
- A form to record manual review findings
- Progress tracking and statistics

All reviews are automatically saved to your CSV file.

---

## Quick Start Guide

### Step 1: Install Python

**Windows:**
1. Download Python from [python.org/downloads](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT**: Check the box "Add Python to PATH" during installation
4. Click "Install Now"

**macOS:**
1. Open Terminal
2. Install Homebrew (if not installed): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Install Python: `brew install python3`

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3-tk
```

### Step 2: Download This Project

**Option A: Download from GitHub**
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file to a location you'll remember (e.g., Desktop)

**Option B: Clone with Git** (if you have git installed)
```bash
git clone [repository-url]
cd ChestImaging
```

### Step 3: Prepare Your Data

1. **Locate your CSV file** with the reports to review
2. **Copy it** to the same folder as this README
3. **Edit `config.ini`**:
   - Open `config.ini` with Notepad (Windows) or TextEdit (Mac)
   - Change this line: `csv_file = Review_Cohort_Webb.csv`
   - To match your file: `csv_file = YOUR_FILE_NAME.csv`
   - Save the file

**Example config.ini:**
```ini
[DATA]
csv_file = my_pe_reports.csv
```

**Don't have a CSV yet?** See `data/README_CSV_FORMAT.md` for the required format.

### Step 4: Run Setup

**Windows:**
1. Double-click `setup.bat`
2. Wait for installation to complete (may take a few minutes)
3. Press any key when prompted

**macOS/Linux:**
1. Open Terminal
2. Navigate to the project folder: `cd path/to/ChestImaging`
3. Make the script executable: `chmod +x setup.sh`
4. Run setup: `./setup.sh`

### Step 5: Start Reviewing!

**Windows:**
- Double-click `run.bat`

**macOS/Linux:**
1. Make the script executable: `chmod +x run.sh`
2. Run: `./run.sh`

The application window will open automatically!

---

## Using the Application

### Main Interface

The application has three main sections:

1. **Left Panel**: Displays the full medical report text
   - PE-related keywords are highlighted in yellow
   - Shows AI model predictions below the report

2. **Right Panel**: Review form for manual validation
   - Select PE Present (Yes/No)
   - If PE present, fill in location, acuity, laterality, and burden
   - Select your confidence level
   - Add optional comments

3. **Bottom Navigation**:
   - **Previous/Next buttons**: Navigate between reports
   - **Save button**: Saves current review (also auto-saves on "Next")
   - **Skip to Unreviewed**: Jumps to the next report that hasn't been reviewed
   - **Jump to**: Enter a report number to jump directly to it

### Keyboard Shortcuts

- **0**: Mark as "No PE"
- **1**: Mark as "PE Present"
- **→ (Right Arrow)**: Next report
- **← (Left Arrow)**: Previous report
- **Ctrl+S**: Save current review
- **Ctrl+K**: Skip to next unreviewed report

### Progress Tracking

- **Top right**: Shows how many reports you've reviewed out of the total
- **Progress bar**: Visual indicator of overall completion
- **Auto-position**: On launch, automatically jumps to the first unreviewed report

---

## Frequently Asked Questions

### Q: What if I get an error about Python not found?
**A:** Make sure Python is installed and added to your system PATH. Try reinstalling Python and check "Add Python to PATH" during installation.

### Q: What if I get an error about tkinter?
**A:**
- **Windows/macOS**: Reinstall Python from python.org (tkinter is included)
- **Linux**: Run `sudo apt-get install python3-tk`

### Q: What if I accidentally close the application?
**A:** No problem! Your work is saved after each review. Just reopen the application and continue where you left off.

### Q: How do I know my changes are saved?
**A:** The application saves automatically when you click "Next" or "Save". You'll see a green "✓ Saved" message briefly appear.

### Q: Can I change the CSV file after setup?
**A:** Yes! Just edit `config.ini` and change the `csv_file` setting to your new file name.

### Q: What if my CSV has different column names?
**A:** Your CSV must have specific column names for the application to work. See `data/README_CSV_FORMAT.md` for details. You may need to rename columns in your CSV to match the required format.

---

## Technical Details

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended for large datasets)
- **Disk Space**: 100MB for application + size of your CSV file

### Dependencies
- **pandas**: Data manipulation and CSV handling
- **tkinter**: Graphical user interface (included with Python)

See `requirements.txt` for specific versions.

### File Structure
```
ChestImaging/
├── README.md              # This file
├── config.ini             # Configuration file
├── requirements.txt       # Python dependencies
├── reviewcode.py          # Main application code
├── setup.bat              # Windows setup script
├── setup.sh               # Mac/Linux setup script
├── run.bat                # Windows run script
├── run.sh                 # Mac/Linux run script
├── data/                  # Data folder
│   ├── csv_template.csv   # Example CSV format
│   └── README_CSV_FORMAT.md  # CSV format documentation
└── docs/                  # Additional documentation
```

### How It Works
1. The application reads your CSV file specified in `config.ini`
2. It loads each report and displays the text and AI predictions
3. You review each report and fill in the form
4. Your answers are saved back to the CSV file in the "Manual_*" columns
5. Progress is tracked automatically

---

## Troubleshooting

### Application won't start

**Check Python installation:**
```bash
python --version
```
Should show Python 3.8 or higher.

**Try running directly:**
```bash
# Activate virtual environment first
# Windows:
venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# Then run:
python reviewcode.py
```

### "Config file not found" error
Make sure `config.ini` is in the same folder as `reviewcode.py`.

### "CSV file not found" error
1. Check that your CSV file is in the same folder as the application
2. Check that the filename in `config.ini` matches exactly (including .csv extension)
3. Check for typos in the filename

### Application is slow
- **Large dataset**: If you have thousands of reports, the initial load may take a few seconds
- **Large report text**: Very long reports may take a moment to display
- Try closing other applications to free up memory

### Need more help?
1. Check `data/README_CSV_FORMAT.md` for CSV format issues
2. Create an issue on GitHub with:
   - Your operating system
   - Python version (`python --version`)
   - The error message you're seeing
   - Steps to reproduce the problem

---

## For Developers

### Development Setup
```bash
# Clone the repository
git clone [repository-url]
cd ChestImaging

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python reviewcode.py
```

### Code Structure
- **`reviewcode.py`**: Main application with MedicalReportReviewer class
- **Configuration**: Uses configparser to read `config.ini`
- **Data handling**: Pandas DataFrames for CSV operations
- **UI**: Tkinter with custom styling

---

## License

MIT License

---

## Contact

For questions or support:
- **GitHub Issues**: [josephdwebb]/issues
- **Email**: jdwebb@bu.edu
---

**Version**: 1.0.0
**Last Updated**: 2025
