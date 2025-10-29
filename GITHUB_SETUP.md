# GitHub Publication Guide

This guide will help you publish PE Reviewer to GitHub for your collaborators.

## Before You Upload

### 1. Protect Sensitive Data

**CRITICAL**: Make sure you don't upload patient data!

1. Check `.gitignore` is present (it is)
2. The `.gitignore` file is configured to exclude:
   - All CSV files except the template
   - Virtual environment files
   - Python cache files
   - Personal configuration (if needed)

3. **Verify what will be uploaded**:
   ```bash
   git status
   ```
   If you see any CSV files with real patient data, add them to `.gitignore`:
   ```bash
   echo "Review_Cohort_Webb.csv" >> .gitignore
   ```

### 2. Update Personal Information

Before uploading, update these files with your information:

**README.md:**
- Replace `[Your Name]` in License section
- Replace `[your-email]` in Contact section
- Replace `[repository-url]` with your actual GitHub URL
- Add your citation information

**LICENSE:**
- Replace `[Your Name]` with your actual name

**CONTRIBUTING.md:**
- Replace `[your-email]` with your email

## Publishing to GitHub

### Option A: Using GitHub Desktop (Easiest)

1. **Download GitHub Desktop**:
   - Visit: https://desktop.github.com/
   - Install and sign in with your GitHub account

2. **Create a new repository**:
   - Click "File" → "New Repository"
   - Name: `PE-Reviewer` (or your preferred name)
   - Description: "Medical report review tool for pulmonary embolism validation"
   - Choose the ChestImaging folder as the local path
   - Click "Create Repository"

3. **Make first commit**:
   - All files will be staged automatically
   - Enter commit message: "Initial commit - PE Reviewer v1.0"
   - Click "Commit to main"

4. **Publish to GitHub**:
   - Click "Publish repository"
   - Choose whether to make it public or private
   - **Uncheck** "Keep this code private" if you want it public
   - Click "Publish Repository"

Done! Your repository is now on GitHub.

### Option B: Using Git Command Line

1. **Install Git**:
   - Windows: https://git-scm.com/download/win
   - Mac: `brew install git`
   - Linux: `sudo apt-get install git`

2. **Configure Git** (if first time):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. **Create GitHub repository**:
   - Go to https://github.com/new
   - Repository name: `PE-Reviewer`
   - Description: "Medical report review tool for pulmonary embolism validation"
   - Choose Public or Private
   - **Don't** initialize with README (we already have one)
   - Click "Create repository"

4. **Initialize local repository**:
   ```bash
   cd "C:\Users\Joe\Desktop\ChestImaging"
   git init
   git add .
   git commit -m "Initial commit - PE Reviewer v1.0"
   ```

5. **Connect to GitHub** (replace with your URL):
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/PE-Reviewer.git
   git branch -M main
   git push -u origin main
   ```

Done! Your code is now on GitHub.

## After Publishing

### 1. Verify the Upload

Visit your repository on GitHub and check:
- [ ] README.md displays correctly
- [ ] No CSV files with patient data are visible
- [ ] All documentation files are present
- [ ] Setup scripts are included

### 2. Configure Repository Settings

On GitHub, go to Settings:

**General:**
- Add repository description
- Add topics/tags: `medical-imaging`, `python`, `tkinter`, `radiology`, `machine-learning-validation`

**Features:**
- Enable Issues (for bug reports)
- Enable Discussions (for questions)
- Disable Wiki (unless you want it)

**About (right side of main page):**
- Add description
- Add website (if you have one)
- Add topics

### 3. Create a Release

1. Go to "Releases" on your repository
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `PE Reviewer v1.0.0 - Initial Release`
5. Description:
   ```markdown
   # PE Reviewer v1.0.0

   Initial release of PE Reviewer - a desktop application for manual review and validation of AI predictions for pulmonary embolism detection.

   ## Features
   - User-friendly GUI for report review
   - Configurable CSV input
   - Progress tracking
   - Keyboard shortcuts
   - Auto-save functionality

   ## Installation
   See [README.md](README.md) for detailed installation instructions.

   ## Quick Start
   1. Download the source code
   2. Run setup.bat (Windows) or setup.sh (Mac/Linux)
   3. Edit config.ini with your CSV filename
   4. Run run.bat (Windows) or run.sh (Mac/Linux)
   ```
6. Click "Publish release"

## Sharing with Collaborators

### Send Them Instructions

Create an email or message like this:

```
Subject: PE Reviewer Tool - Ready to Use!

Hi team,

I've published our PE review tool to GitHub. Here's how to get started:

🔗 Repository: [your-github-url]

📥 Download:
1. Go to the repository URL
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract to your computer

⚙️ Setup (One-time):
1. Make sure Python 3.8+ is installed
2. Run setup.bat (Windows) or setup.sh (Mac/Linux)
3. Edit config.ini with your CSV filename
4. Place your CSV file in the same folder

▶️ Running the Tool:
Double-click run.bat (Windows) or run.sh (Mac/Linux)

📚 Documentation:
- README.md - Complete documentation
- docs/QUICKSTART.md - Quick start guide
- docs/TROUBLESHOOTING.md - Common issues

❓ Questions or Issues:
Create an issue on GitHub or contact me directly.

Happy reviewing!
```

### For Less Technical Users

Create a simple step-by-step guide:

1. **Download Python**:
   - Go to python.org/downloads
   - Download and install (check "Add Python to PATH")

2. **Download PE Reviewer**:
   - Go to [GitHub URL]
   - Click green "Code" button → Download ZIP
   - Extract to Desktop

3. **Setup**:
   - Double-click setup.bat (wait for it to finish)
   - Right-click config.ini → Open with Notepad
   - Change `csv_file = Review_Cohort_Webb.csv` to your filename
   - Save and close

4. **Run**:
   - Double-click run.bat
   - Start reviewing!

## Maintaining the Repository

### Making Updates

When you make changes to the code:

**GitHub Desktop:**
1. Make your changes
2. GitHub Desktop will show changed files
3. Enter commit message describing changes
4. Click "Commit to main"
5. Click "Push origin"

**Command Line:**
```bash
git add .
git commit -m "Description of changes"
git push
```

### Collaborator Access

To give others permission to edit:

1. Go to repository Settings → Collaborators
2. Click "Add people"
3. Enter their GitHub username or email
4. They'll receive an invitation

### Handling Issues

When someone reports a bug:
1. Acknowledge it
2. Try to reproduce it
3. Fix the issue
4. Commit the fix with message: "Fix: [issue description]"
5. Close the issue with a comment explaining the fix

## Best Practices

1. **Never commit real patient data** - always check before pushing
2. **Write clear commit messages** - describe what and why
3. **Update version numbers** - for significant changes, create new releases
4. **Respond to issues** - help your collaborators when they have problems
5. **Document changes** - keep README.md up to date
6. **Test before pushing** - make sure changes work
7. **Use branches for experiments** - keep main branch stable

## Making It Public vs Private

### Private Repository (Recommended for Medical Data)
- ✅ Only invited collaborators can access
- ✅ Your code and documentation are private
- ✅ More appropriate for healthcare projects
- ❌ Requires GitHub Pro ($4/month) for more than 3 collaborators
- ❌ Can't be found by search engines

### Public Repository
- ✅ Free for unlimited collaborators
- ✅ Can help other research groups
- ✅ Increases visibility and citations
- ❌ Anyone can see the code
- ❌ More responsibility to maintain

**Recommendation**: Start private, make public later after ensuring all patient data is removed and properly documented.

## Troubleshooting GitHub Upload

### Authentication Issues
- Use GitHub Desktop (easier than SSH keys)
- Or use Personal Access Token:
  1. GitHub → Settings → Developer settings → Personal access tokens
  2. Generate new token with "repo" permissions
  3. Use token as password when pushing

### Large File Errors
- GitHub has a 100MB file limit
- Large CSV files should be in `.gitignore`
- If you accidentally added a large file, see: https://docs.github.com/en/repositories/working-with-files/managing-large-files

### Merge Conflicts
- If you and a collaborator edit the same file
- GitHub Desktop will help you resolve conflicts
- Or manually edit the conflicting file

## Additional Resources

- **GitHub Docs**: https://docs.github.com/
- **GitHub Desktop Guide**: https://docs.github.com/en/desktop
- **Git Tutorial**: https://git-scm.com/book/en/v2

---

Questions about GitHub? Feel free to reach out or consult the GitHub documentation!
