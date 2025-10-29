# CSV File Format Guide

## Required Columns

Your CSV file MUST include the following columns for the PE Reviewer to work properly:

### Report Information Columns
- **Report_Number**: Unique identifier for the report (e.g., "E6252251")
- **EMPI**: Patient identifier number
- **Report_Description**: Brief description of the report type
- **Report_Type_Group**: Category of the report (e.g., "CT PE Protocol")
- **Report_Text**: The full text of the medical report (this is what reviewers will read)

### AI Model Prediction Columns
These columns contain the predictions from your AI models:
- **SVM_PE_Prediction**: SVM model prediction (0=No PE, 1=PE Present)
- **SVM_Probability**: SVM confidence score (0.0 to 1.0)
- **Regex_PE_Prediction**: Regex-based prediction (0=No PE, 1=PE Present)
- **LLM_PE_Binary**: Large Language Model prediction (0=No PE, 1=PE Present)
- **LLM_Confidence**: LLM confidence level (e.g., "high", "medium", "low")
- **LLM_Reasoning**: Explanation from the LLM
- **PE_Location**: LLM-predicted location (e.g., "Central", "Segmental")
- **PE_Acuity**: LLM-predicted acuity (e.g., "Acute", "Chronic")
- **PE_Laterality**: LLM-predicted side (e.g., "Right", "Left", "Bilateral")
- **PE_Clot_Burden**: LLM-predicted burden (e.g., "High", "Low")
- **Agreement_Pattern**: Pattern of agreement between models (optional)

### Manual Review Columns (Leave Empty Initially)
These columns will be filled in by reviewers using the application:
- **Manual_PE_Present**: Manual review result (will be filled by reviewer)
- **Manual_PE_Location**: Manual review location (will be filled by reviewer)
- **Manual_PE_Acuity**: Manual review acuity (will be filled by reviewer)
- **Manual_PE_Laterality**: Manual review laterality (will be filled by reviewer)
- **Manual_PE_Clot_Burden**: Manual review burden (will be filled by reviewer)
- **Reviewer_Confidence**: Reviewer confidence level (will be filled by reviewer)
- **Comments**: Optional reviewer comments (will be filled by reviewer)

## Important Notes

1. **Leave manual review columns empty** in your initial CSV file. The application will fill these in as reviewers complete their work.

2. **The application auto-saves** after each review to the same CSV file, so your work is never lost.

3. **File naming**: You can name your CSV file anything you want. Just update the `csv_file` setting in `config.ini` to match your filename.

4. **Example template**: See `csv_template.csv` in this folder for a properly formatted example.

## Preparing Your Data

If your CSV has different column names:
1. Add or rename columns to match the required format above
2. Make sure all required columns exist (even if some are empty)
3. Leave the Manual_* columns empty for reviewers to fill in
