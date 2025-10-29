# Quick Start Guide

Get up and running with PE Reviewer in 5 minutes!

## Prerequisites

- Python 3.8 or higher installed
- Your CSV file with reports to review

## Installation (5 Steps)

### 1. Download the Code
Download and extract the project to your computer (e.g., Desktop).

### 2. Configure Your CSV
Edit `config.ini`:
```ini
[DATA]
csv_file = YOUR_FILE.csv
```
Replace `YOUR_FILE.csv` with your actual CSV filename.

### 3. Run Setup

**Windows**: Double-click `setup.bat`

**Mac/Linux**:
```bash
chmod +x setup.sh
./setup.sh
```

Wait for installation to complete (usually 1-2 minutes).

### 4. Launch the Application

**Windows**: Double-click `run.bat`

**Mac/Linux**:
```bash
chmod +x run.sh
./run.sh
```

### 5. Start Reviewing!

The application will automatically jump to the first unreviewed report.

## Basic Usage

### Navigation
- **Next**: Click "Next →" or press Right Arrow
- **Previous**: Click "← Previous" or press Left Arrow
- **Jump**: Enter a report number in "Jump to" box
- **Skip**: Click "⏭ Skip to Next Unreviewed" or press Ctrl+K

### Reviewing a Report

1. **Read the report** in the left panel
   - Keywords like "pulmonary embolism" are highlighted
   - Check the AI predictions below the report

2. **Fill in the form** on the right:
   - **PE Present**: Press `0` for No PE, or `1` for PE Present
   - **If PE Present**: Fill in Location, Acuity, Laterality, Burden
   - **Confidence**: Select High, Medium, or Low
   - **Comments**: Optional notes

3. **Save**: Click "💾 Save" or press Ctrl+S
   - Or just click "Next →" which auto-saves

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0` | Mark as "No PE" |
| `1` | Mark as "PE Present" |
| `→` | Next report |
| `←` | Previous report |
| `Ctrl+S` | Save current review |
| `Ctrl+K` | Skip to next unreviewed |

## Tips

1. **Auto-save**: The app saves automatically when you click "Next"
2. **Progress tracking**: Check the top-right corner for completion status
3. **Resume anytime**: Close and reopen - you'll return to where you left off
4. **Validation**: Required fields are marked with `*`

## Common Issues

**Application won't start?**
- Make sure you ran `setup.bat` or `setup.sh` first
- Check Python is installed: `python --version`

**CSV not found?**
- Verify the filename in `config.ini` matches exactly
- Make sure the CSV is in the same folder as `reviewcode.py`

**Can't save?**
- Close the CSV file if open in Excel
- Fill in all required fields (marked with `*`)

For more help, see `docs/TROUBLESHOOTING.md` or the main `README.md`.

## Next Steps

Once you're comfortable:
- Review `data/README_CSV_FORMAT.md` to understand the CSV structure
- Check the full `README.md` for detailed documentation
- See `docs/TROUBLESHOOTING.md` if you encounter issues

---

Happy reviewing! 🏥
