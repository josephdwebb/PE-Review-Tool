# Troubleshooting Guide

This guide covers common issues and their solutions.

## Installation Issues

### Python Not Found

**Symptoms:**
- Error message: "Python is not recognized as an internal or external command"
- Setup script fails immediately

**Solutions:**
1. **Windows**: Reinstall Python from python.org
   - Make sure to check "Add Python to PATH" during installation
   - Restart your computer after installation

2. **Verify installation**: Open Command Prompt/Terminal and run:
   ```bash
   python --version
   ```
   Should show "Python 3.8" or higher

### Virtual Environment Creation Failed

**Symptoms:**
- Error during `python -m venv venv`
- Missing venv module

**Solutions:**
1. **Linux users**: Install venv package
   ```bash
   sudo apt-get install python3-venv
   ```

2. **All platforms**: Try using `python3` instead:
   ```bash
   python3 -m venv venv
   ```

### Tkinter Not Found

**Symptoms:**
- Error: "No module named 'tkinter'"
- Application crashes on startup

**Solutions:**

**Windows/macOS:**
- Tkinter should be included with Python
- Reinstall Python from the official python.org installer

**Linux:**
```bash
sudo apt-get install python3-tk
```

**Verify tkinter installation:**
```bash
python -c "import tkinter; print('Tkinter OK')"
```

## Configuration Issues

### Config File Not Found

**Symptoms:**
- Error: "config.ini file not found"

**Solutions:**
1. Make sure `config.ini` is in the same folder as `reviewcode.py`
2. If missing, create it with this content:
   ```ini
   [DATA]
   csv_file = your_file.csv

   [DISPLAY]
   window_width = 1400
   window_height = 900

   [REVIEW]
   auto_save_interval = 0
   ```

### CSV File Not Found

**Symptoms:**
- Error: "CSV file not found: [path]"

**Solutions:**
1. **Check filename**: Make sure the filename in `config.ini` matches exactly
   - Case-sensitive on Linux/macOS
   - Include the `.csv` extension

2. **Check location**: Place your CSV in the same folder as `reviewcode.py`

3. **Use full path** (if file is elsewhere):
   ```ini
   csv_file = C:\Users\YourName\Documents\my_data.csv
   ```

### Invalid CSV Format

**Symptoms:**
- Application loads but crashes when displaying a report
- Missing columns error

**Solutions:**
1. Check your CSV has all required columns (see `data/README_CSV_FORMAT.md`)
2. Required columns must exist (even if empty):
   - Report_Number
   - Report_Text
   - SVM_PE_Prediction
   - LLM_PE_Binary
   - Manual_PE_Present (can be empty)
   - etc.

## Application Issues

### Application Won't Start

**Symptoms:**
- Window opens briefly then closes
- No error message visible

**Solutions:**
1. **Run from command line** to see error messages:
   ```bash
   # Windows:
   venv\Scripts\activate.bat
   python reviewcode.py

   # Mac/Linux:
   source venv/bin/activate
   python3 reviewcode.py
   ```

2. Check for error messages and see specific solutions below

### Application is Very Slow

**Symptoms:**
- Takes a long time to load
- Sluggish navigation between reports

**Solutions:**
1. **Large dataset**: First load of large CSV files (1000+ reports) takes time
2. **Memory**: Close other applications
3. **Long reports**: Very long report texts (>10,000 words) may slow rendering
4. **Hardware**: Consider using a computer with more RAM

### Save Button Doesn't Work

**Symptoms:**
- Click "Save" but changes aren't saved
- Error message when saving

**Solutions:**
1. **File permissions**: Make sure the CSV file isn't read-only
   - Right-click CSV → Properties → Uncheck "Read-only"

2. **File in use**: Close the CSV in Excel or other programs

3. **Disk space**: Check you have available disk space

4. **CSV locked**: On Windows, Excel locks files even when "closed"
   - Fully quit Excel from Task Manager

### Form Validation Errors

**Symptoms:**
- Can't save: "Please complete required fields"

**Solutions:**
1. **PE Present is required**: Must select "No PE" (0) or "PE Present" (1)
2. **Confidence is required**: Must select High, Medium, or Low
3. **If PE Present = 1**, you must also fill in:
   - PE Location
   - PE Acuity
   - PE Laterality
   - PE Clot Burden

### Keyboard Shortcuts Don't Work

**Symptoms:**
- Pressing 0, 1, or arrow keys has no effect

**Solutions:**
1. **Click on the main window** to give it focus
2. **Don't click inside text boxes** - shortcuts won't work when text input has focus
3. **Click on the report text area**, then try shortcuts

## Data Issues

### All Reports Show as "Reviewed"

**Symptoms:**
- "Skip to Unreviewed" says all reports are reviewed
- Progress shows 100%

**Solutions:**
1. Check your CSV - the `Manual_PE_Present` column may already have values
2. To start fresh review:
   - Open CSV in Excel or text editor
   - Clear the Manual_* columns
   - Save the file

### Changes Not Appearing in CSV

**Symptoms:**
- Save works, but CSV file doesn't show changes

**Solutions:**
1. **Close and reopen** the CSV file
2. **Check you're looking at the right file**
3. **Excel caching**: Close Excel completely and reopen
4. **Backup**: Check if there's a `.backup` file with your changes

### Lost My Progress

**Symptoms:**
- Reviewed reports now show as unreviewed

**Solutions:**
1. **Check your CSV file** - reviews are stored there
2. **Wrong CSV**: Make sure `config.ini` points to the correct file
3. **File replaced**: Check if you accidentally replaced your CSV with a fresh copy

## Platform-Specific Issues

### Windows: Scripts Won't Run

**Symptoms:**
- Double-clicking `.bat` files does nothing
- Scripts open in text editor instead of running

**Solutions:**
1. Right-click → "Run as administrator"
2. Try running from Command Prompt:
   ```cmd
   cd C:\path\to\ChestImaging
   setup.bat
   ```

### macOS: "Cannot be opened because it is from an unidentified developer"

**Symptoms:**
- Can't run setup.sh or run.sh

**Solutions:**
1. Make script executable:
   ```bash
   chmod +x setup.sh run.sh
   ```

2. Run from Terminal:
   ```bash
   ./setup.sh
   ```

### Linux: Permission Denied

**Symptoms:**
- "Permission denied" when running scripts

**Solutions:**
1. Make scripts executable:
   ```bash
   chmod +x setup.sh run.sh
   ```

2. Use sudo if needed:
   ```bash
   sudo ./setup.sh
   ```

## Getting More Help

If your issue isn't covered here:

1. **Check the main README.md** for basic setup instructions
2. **Check data/README_CSV_FORMAT.md** for CSV format issues
3. **Run with verbose errors**:
   ```bash
   python reviewcode.py 2>&1 | tee error.log
   ```
   This saves errors to `error.log`

4. **Create a GitHub issue** with:
   - Your operating system and version
   - Python version (`python --version`)
   - Full error message
   - Steps to reproduce the problem
   - The error.log file if available

5. **Check for updates**: Make sure you have the latest version of the code

## Common Error Messages

### "No module named 'pandas'"
**Solution**: Run setup script again, or manually install:
```bash
pip install pandas
```

### "No module named 'tkinter'"
**Solution**: See "Tkinter Not Found" section above

### "Permission denied"
**Solution**: File or folder permissions issue
- Windows: Run as administrator
- macOS/Linux: Use `chmod` to make files executable

### "Access denied" when saving
**Solution**: CSV file is locked by another program
- Close Excel and any other programs using the CSV
- Check file isn't set to read-only

---

Still stuck? Open an issue on GitHub with your error message and system details!
