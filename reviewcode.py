# -*- coding: utf-8 -*-
"""
Professional Medical Report Review Application
For manual verification of pulmonary embolism predictions
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import pandas as pd
import csv
from datetime import datetime
import configparser
import os
import sys


class MedicalReportReviewer(tk.Tk):
    """Elite medical report review interface"""

    def __init__(self):
        super().__init__()

        # Load configuration
        self.config = self.load_config()

        # Application setup
        self.title("Pulmonary Embolism Report Review System")
        window_width = self.config.getint('DISPLAY', 'window_width', fallback=1400)
        window_height = self.config.getint('DISPLAY', 'window_height', fallback=900)
        self.geometry(f"{window_width}x{window_height}")
        self.configure(bg="#f8f9fa")

        # Data
        self.csv_path = self.get_csv_path()
        self.df = None
        self.current_index = 0
        self.unsaved_changes = False

        # Colors - Modern clean theme
        self.colors = {
            'bg_dark': '#f8f9fa',        # Very light gray background
            'bg_medium': '#ffffff',      # Pure white
            'bg_light': '#f1f3f5',       # Light gray
            'bg_hover': '#e9ecef',       # Hover state
            'accent': '#2563eb',         # Modern blue
            'accent_hover': '#1d4ed8',   # Darker blue for hover
            'success': '#10b981',        # Modern green
            'warning': '#f59e0b',        # Amber warning
            'danger': '#ef4444',         # Red
            'text_primary': '#1f2937',   # Dark gray text
            'text_secondary': '#6b7280', # Medium gray text
            'border': '#e5e7eb',         # Light border
            'highlight_bg': '#fef3c7',   # Soft yellow highlight
            'highlight_text': '#92400e'  # Dark brown for highlighted text
        }

        # Form variables
        self.form_vars = {}

        # Load data and setup UI
        self.load_data()
        self.setup_styles()
        self.create_layout()
        self.bind_shortcuts()
        self.load_report(self.find_first_unreviewed())

    def load_config(self):
        """Load configuration from config.ini"""
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

        if not os.path.exists(config_path):
            messagebox.showerror(
                "Configuration Error",
                f"config.ini file not found!\n\n"
                f"Expected location: {config_path}\n\n"
                f"Please ensure config.ini is in the same folder as this program."
            )
            sys.exit(1)

        config.read(config_path)
        return config

    def get_csv_path(self):
        """Get CSV file path from config, with validation"""
        csv_file = self.config.get('DATA', 'csv_file', fallback='')

        if not csv_file:
            messagebox.showerror(
                "Configuration Error",
                "No CSV file specified in config.ini!\n\n"
                "Please edit config.ini and set the csv_file parameter."
            )
            sys.exit(1)

        # If it's not an absolute path, look in the same directory as the script
        if not os.path.isabs(csv_file):
            csv_file = os.path.join(os.path.dirname(__file__), csv_file)

        # Check if file exists
        if not os.path.exists(csv_file):
            messagebox.showerror(
                "File Not Found",
                f"CSV file not found:\n{csv_file}\n\n"
                f"Please check the csv_file setting in config.ini"
            )
            sys.exit(1)

        return csv_file

    def find_first_unreviewed(self):
        """Find the first report without manual review"""
        for idx in range(len(self.df)):
            pe_present = self.df.iloc[idx].get('Manual_PE_Present')
            # If Manual_PE_Present is NaN, empty, or not filled, it's unreviewed
            if pd.isna(pe_present) or str(pe_present).strip() == '':
                return idx
        # If all reviewed, start at beginning
        return 0

    def load_data(self):
        """Load CSV data"""
        try:
            self.df = pd.read_csv(self.csv_path)
            print(f"Loaded {len(self.df)} reports")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {str(e)}")
            self.destroy()

    def setup_styles(self):
        """Configure ttk styles for professional appearance"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configure frame styles
        style.configure('Dark.TFrame', background=self.colors['bg_dark'])
        style.configure('Medium.TFrame', background=self.colors['bg_medium'])
        style.configure('Light.TFrame', background=self.colors['bg_light'])

        # Configure label styles
        style.configure('Title.TLabel',
                       background=self.colors['bg_dark'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 16, 'bold'))

        style.configure('Heading.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 11, 'bold'))

        style.configure('Body.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 9))

        style.configure('Small.TLabel',
                       background=self.colors['bg_light'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 8))

        # Configure combobox
        style.configure('TCombobox',
                       fieldbackground=self.colors['bg_light'],
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text_primary'],
                       arrowcolor=self.colors['accent'])

        # Configure radiobutton
        style.configure('TRadiobutton',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 9))
        style.map('TRadiobutton',
                 background=[('active', self.colors['bg_light'])],
                 foreground=[('active', self.colors['accent'])])

    def create_layout(self):
        """Create the main UI layout"""
        # Main container with padding
        main_frame = ttk.Frame(self, style='Dark.TFrame', padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        self.create_header(main_frame)

        # Content area - two columns
        content_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        # Left column: Report display (60%)
        left_frame = ttk.Frame(content_frame, style='Medium.TFrame')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.create_report_display(left_frame)

        # Right column: Review form (40%)
        right_frame = ttk.Frame(content_frame, style='Medium.TFrame')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        self.create_review_form(right_frame)

        # Footer with navigation
        self.create_footer(main_frame)

    def create_header(self, parent):
        """Create header with title and progress"""
        header_frame = ttk.Frame(parent, style='Dark.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 10))

        # Title
        title = ttk.Label(header_frame,
                         text="Pulmonary Embolism Report Review",
                         style='Title.TLabel')
        title.pack(side=tk.LEFT)

        # Status and progress container
        right_header = ttk.Frame(header_frame, style='Dark.TFrame')
        right_header.pack(side=tk.RIGHT)

        # Statistics panel
        stats_frame = tk.Frame(right_header, bg=self.colors['bg_dark'])
        stats_frame.pack(side=tk.TOP, anchor=tk.E, pady=(0, 5))

        self.stats_label = tk.Label(stats_frame,
                                    text="",
                                    font=('Segoe UI', 9),
                                    bg=self.colors['bg_dark'],
                                    fg=self.colors['text_secondary'])
        self.stats_label.pack(side=tk.LEFT, padx=5)

        # Status indicator
        self.status_label = tk.Label(stats_frame,
                                    text="",
                                    font=('Segoe UI', 9, 'bold'),
                                    bg=self.colors['bg_dark'],
                                    fg=self.colors['success'])
        self.status_label.pack(side=tk.LEFT, padx=5)

        # Progress indicator
        self.progress_label = ttk.Label(right_header,
                                       text="Report 0 of 0",
                                       style='Title.TLabel')
        self.progress_label.pack(side=tk.TOP, anchor=tk.E)

        # Progress bar
        progress_frame = ttk.Frame(parent, style='Dark.TFrame')
        progress_frame.pack(fill=tk.X, pady=(0, 10))

        self.progress_bar = ttk.Progressbar(progress_frame,
                                           mode='determinate',
                                           style='TProgressbar')
        self.progress_bar.pack(fill=tk.X)

        # Keyboard shortcuts help
        shortcuts_frame = ttk.Frame(parent, style='Dark.TFrame')
        shortcuts_frame.pack(fill=tk.X, pady=(5, 0))

        shortcuts_text = "⌨ Shortcuts: 0=No PE | 1=PE Present | ←/→=Previous/Next | Ctrl+S=Save | Ctrl+K=Skip to Unreviewed"
        shortcuts_label = tk.Label(shortcuts_frame,
                                  text=shortcuts_text,
                                  font=('Segoe UI', 8),
                                  bg=self.colors['bg_dark'],
                                  fg=self.colors['text_secondary'])
        shortcuts_label.pack(pady=2)

    def create_report_display(self, parent):
        """Create the report text display area"""
        # Section header
        header = ttk.Label(parent, text="Report Text", style='Heading.TLabel')
        header.pack(anchor=tk.W, pady=(10, 5), padx=10)

        # Report info bar
        info_frame = ttk.Frame(parent, style='Light.TFrame')
        info_frame.pack(fill=tk.X, padx=10, pady=5)

        self.report_info = ttk.Label(info_frame,
                                    text="",
                                    style='Small.TLabel')
        self.report_info.pack(anchor=tk.W, padx=10, pady=5)

        # Text widget with scrollbar
        text_frame = ttk.Frame(parent, style='Medium.TFrame')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.report_text = tk.Text(text_frame,
                                  wrap=tk.WORD,
                                  font=('Segoe UI', 11),
                                  bg=self.colors['bg_medium'],
                                  fg=self.colors['text_primary'],
                                  insertbackground=self.colors['accent'],
                                  relief=tk.SOLID,
                                  borderwidth=1,
                                  highlightthickness=0,
                                  padx=20,
                                  pady=20,
                                  spacing1=2,
                                  spacing3=2,
                                  yscrollcommand=scrollbar.set)
        self.report_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.report_text.yview)

        # Reference predictions panel
        ref_frame = ttk.Frame(parent, style='Light.TFrame')
        ref_frame.pack(fill=tk.X, padx=10, pady=10)

        ref_label = ttk.Label(ref_frame,
                             text="AI Predictions (Reference Only)",
                             style='Heading.TLabel')
        ref_label.pack(anchor=tk.W, padx=10, pady=5)

        self.reference_text = tk.Text(ref_frame,
                                     height=4,
                                     wrap=tk.WORD,
                                     font=('Segoe UI', 9),
                                     bg=self.colors['bg_light'],
                                     fg=self.colors['text_secondary'],
                                     relief=tk.SOLID,
                                     borderwidth=1,
                                     highlightthickness=0,
                                     padx=12,
                                     pady=8)
        self.reference_text.pack(fill=tk.X, padx=10, pady=5)

    def create_review_form(self, parent):
        """Create the review form with all input fields"""
        # Scrollable form
        canvas = tk.Canvas(parent, bg=self.colors['bg_medium'],
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='Medium.TFrame')

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Form header
        form_header = ttk.Label(scrollable_frame,
                               text="Manual Review",
                               style='Heading.TLabel')
        form_header.pack(anchor=tk.W, pady=(10, 20), padx=15)

        # 1. PE Present (Required)
        self.create_field_section(
            scrollable_frame,
            "1. PE Present *",
            "Manual_PE_Present",
            "radio",
            options=[("No PE", "0"), ("PE Present", "1")],
            required=True
        )

        # 2. PE Location (conditional)
        self.create_field_section(
            scrollable_frame,
            "2. PE Location",
            "Manual_PE_Location",
            "dropdown",
            options=["", "Central", "Segmental", "Subsegmental", "Multiple", "Unknown"]
        )

        # 3. PE Acuity (conditional)
        self.create_field_section(
            scrollable_frame,
            "3. PE Acuity",
            "Manual_PE_Acuity",
            "dropdown",
            options=["", "Acute", "Chronic", "Acute-on-chronic", "Unknown"]
        )

        # 4. PE Laterality (conditional)
        self.create_field_section(
            scrollable_frame,
            "4. PE Laterality",
            "Manual_PE_Laterality",
            "dropdown",
            options=["", "Right", "Left", "Bilateral", "Unknown"]
        )

        # 5. PE Clot Burden (conditional)
        self.create_field_section(
            scrollable_frame,
            "5. PE Clot Burden",
            "Manual_PE_Clot_Burden",
            "dropdown",
            options=["", "High", "Low", "Unknown"]
        )

        # 6. Reviewer Confidence (Required)
        self.create_field_section(
            scrollable_frame,
            "6. Confidence *",
            "Reviewer_Confidence",
            "radio",
            options=[("High", "high"), ("Medium", "medium"), ("Low", "low")],
            required=True
        )

        # 7. Comments (Optional)
        self.create_comments_section(scrollable_frame)

        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_field_section(self, parent, label_text, field_name,
                            field_type, options=None, required=False):
        """Create a form field section"""
        section_frame = ttk.Frame(parent, style='Light.TFrame')
        section_frame.pack(fill=tk.X, padx=15, pady=10)

        # Label
        label = ttk.Label(section_frame,
                         text=label_text,
                         style='Heading.TLabel',
                         font=('Segoe UI', 10, 'bold'))
        label.pack(anchor=tk.W, pady=(5, 10), padx=10)

        if field_type == "radio":
            # Radio buttons
            var = tk.StringVar(value="")
            self.form_vars[field_name] = var

            for option_text, option_value in options:
                rb = ttk.Radiobutton(section_frame,
                                    text=option_text,
                                    variable=var,
                                    value=option_value,
                                    style='TRadiobutton')
                rb.pack(anchor=tk.W, padx=20, pady=3)

        elif field_type == "dropdown":
            # Combobox
            var = tk.StringVar(value="")
            self.form_vars[field_name] = var

            combo = ttk.Combobox(section_frame,
                                textvariable=var,
                                values=options,
                                state='readonly',
                                font=('Segoe UI', 9))
            combo.pack(fill=tk.X, padx=20, pady=5)

    def create_comments_section(self, parent):
        """Create comments text area"""
        section_frame = ttk.Frame(parent, style='Light.TFrame')
        section_frame.pack(fill=tk.X, padx=15, pady=10)

        label = ttk.Label(section_frame,
                         text="7. Comments (Optional)",
                         style='Heading.TLabel',
                         font=('Segoe UI', 10, 'bold'))
        label.pack(anchor=tk.W, pady=(5, 10), padx=10)

        self.comments_text = tk.Text(section_frame,
                                    height=4,
                                    wrap=tk.WORD,
                                    font=('Segoe UI', 9),
                                    bg=self.colors['bg_medium'],
                                    fg=self.colors['text_primary'],
                                    insertbackground=self.colors['accent'],
                                    relief=tk.SOLID,
                                    borderwidth=1,
                                    highlightthickness=0,
                                    padx=12,
                                    pady=10)
        self.comments_text.pack(fill=tk.X, padx=20, pady=5)

    def create_footer(self, parent):
        """Create navigation footer"""
        footer_frame = ttk.Frame(parent, style='Dark.TFrame')
        footer_frame.pack(fill=tk.X, pady=(20, 0))

        # Left side: Jump to report
        left_frame = ttk.Frame(footer_frame, style='Dark.TFrame')
        left_frame.pack(side=tk.LEFT)

        jump_label = ttk.Label(left_frame, text="Jump to:", style='Body.TLabel')
        jump_label.pack(side=tk.LEFT, padx=(0, 10))

        self.jump_var = tk.StringVar()
        jump_entry = tk.Entry(left_frame,
                             textvariable=self.jump_var,
                             width=8,
                             font=('Segoe UI', 10),
                             bg=self.colors['bg_medium'],
                             fg=self.colors['text_primary'],
                             insertbackground=self.colors['accent'],
                             relief=tk.SOLID,
                             borderwidth=1,
                             highlightthickness=0)
        jump_entry.pack(side=tk.LEFT, padx=(0, 10))
        jump_entry.bind('<Return>', lambda e: self.jump_to_report())

        jump_btn = self.create_button(left_frame, "Go", self.jump_to_report,
                                      bg=self.colors['accent'])
        jump_btn.pack(side=tk.LEFT)

        # Center: Quick actions
        center_frame = ttk.Frame(footer_frame, style='Dark.TFrame')
        center_frame.pack(side=tk.LEFT, padx=50)

        skip_btn = self.create_button(center_frame, "⏭ Skip to Next Unreviewed",
                                     self.skip_to_unreviewed,
                                     bg=self.colors['accent'])
        skip_btn.pack(side=tk.LEFT, padx=5)

        # Right side: Navigation buttons
        nav_frame = ttk.Frame(footer_frame, style='Dark.TFrame')
        nav_frame.pack(side=tk.RIGHT)

        prev_btn = self.create_button(nav_frame, "← Previous",
                                      self.previous_report,
                                      bg=self.colors['bg_light'])
        prev_btn.pack(side=tk.LEFT, padx=5)

        save_btn = self.create_button(nav_frame, "💾 Save",
                                      self.save_current,
                                      bg=self.colors['warning'])
        save_btn.pack(side=tk.LEFT, padx=5)

        next_btn = self.create_button(nav_frame, "Next →",
                                      self.next_report,
                                      bg=self.colors['success'])
        next_btn.pack(side=tk.LEFT, padx=5)

    def create_button(self, parent, text, command, bg=None):
        """Create a styled button"""
        if bg is None:
            bg = self.colors['accent']

        # Determine text color based on button background
        if bg in [self.colors['bg_light'], self.colors['bg_hover']]:
            fg_color = self.colors['text_primary']
        else:
            fg_color = '#ffffff'

        btn = tk.Button(parent,
                       text=text,
                       command=command,
                       font=('Segoe UI', 10, 'bold'),
                       bg=bg,
                       fg=fg_color,
                       activebackground=self.colors['accent_hover'],
                       activeforeground='#ffffff',
                       relief=tk.FLAT,
                       padx=20,
                       pady=10,
                       cursor='hand2',
                       borderwidth=0,
                       highlightthickness=0)

        # Hover effects with appropriate color
        hover_bg = self.colors['bg_hover'] if bg == self.colors['bg_light'] else self.colors['accent_hover']
        btn.bind('<Enter>', lambda e: btn.config(bg=hover_bg))
        btn.bind('<Leave>', lambda e: btn.config(bg=bg))

        return btn

    def format_report_text(self, text):
        """Format report text with paragraph breaks"""
        import re

        # Add double line break before ALL CAPS words followed by ":"
        # Pattern: word boundary, 2+ uppercase letters, optional spaces, colon
        formatted = re.sub(r'\b([A-Z]{2,}[A-Z\s]*?):', r'\n\n\1:', text)

        # Clean up multiple consecutive line breaks (max 2)
        formatted = re.sub(r'\n{3,}', '\n\n', formatted)

        # Remove leading/trailing whitespace
        formatted = formatted.strip()

        return formatted

    def highlight_keywords(self):
        """Highlight PE-related keywords in report text"""
        # Configure highlight tag
        self.report_text.tag_configure('highlight',
                                      background=self.colors['highlight_bg'],
                                      foreground=self.colors['highlight_text'],
                                      font=('Consolas', 10, 'bold'))

        # Keywords to highlight (case-insensitive)
        keywords = [
            'pulmonary embolism',
            'pulmonary emboli',
            'embolism',
            'emboli',
            'embolus',
            'thrombus',
            'thrombi',
            r'\bPE\b',  # Word boundary to avoid matching in other words
        ]

        # Get all text content
        content = self.report_text.get('1.0', tk.END)

        # Search and highlight each keyword
        for keyword in keywords:
            import re
            # Use regex for case-insensitive search
            pattern = re.compile(keyword, re.IGNORECASE)

            for match in pattern.finditer(content):
                start_idx = match.start()
                end_idx = match.end()

                # Convert string indices to Tkinter text indices
                start_pos = f"1.0 + {start_idx} chars"
                end_pos = f"1.0 + {end_idx} chars"

                # Apply highlight tag
                self.report_text.tag_add('highlight', start_pos, end_pos)

    def load_report(self, index):
        """Load report at given index"""
        if index < 0 or index >= len(self.df):
            messagebox.showwarning("Warning", "Invalid report index")
            return

        self.current_index = index
        row = self.df.iloc[index]

        # Clear status
        self.status_label.config(text="")

        # Update progress
        progress_pct = ((index + 1) / len(self.df)) * 100
        self.progress_bar['value'] = progress_pct
        self.progress_label.config(text=f"Report {index + 1} of {len(self.df)}")

        # Update report info
        info_text = f"Report #{row['Report_Number']} | {row['Report_Description']}"
        self.report_info.config(text=info_text)

        # Update report text with formatting and highlighting
        self.report_text.config(state=tk.NORMAL)
        self.report_text.delete('1.0', tk.END)
        formatted_text = self.format_report_text(str(row['Report_Text']))
        self.report_text.insert('1.0', formatted_text)
        self.highlight_keywords()
        self.report_text.config(state=tk.DISABLED)

        # Update reference predictions
        ref_text = (
            f"SVM: {row['SVM_PE_Prediction']} ({row['SVM_Probability']:.2f}) | "
            f"LLM: {row['LLM_PE_Binary']} ({row['LLM_Confidence']}) | "
            f"Regex: {row['Regex_PE_Prediction']}\n"
            f"LLM Location: {row['PE_Location']} | "
            f"Acuity: {row['PE_Acuity']} | "
            f"Laterality: {row['PE_Laterality']} | "
            f"Burden: {row['PE_Clot_Burden']}"
        )
        self.reference_text.config(state=tk.NORMAL)
        self.reference_text.delete('1.0', tk.END)
        self.reference_text.insert('1.0', ref_text)
        self.reference_text.config(state=tk.DISABLED)

        # Load existing manual review data
        self.load_existing_review(row)

        # Update statistics
        self.update_statistics()

        # Show AI agreement indicator
        self.show_ai_agreement(row)

        self.unsaved_changes = False

    def load_existing_review(self, row):
        """Load existing review data if present"""
        # PE Present
        pe_present = str(row.get('Manual_PE_Present', ''))
        if pe_present in ['0', '1', '0.0', '1.0']:
            self.form_vars['Manual_PE_Present'].set(str(int(float(pe_present))))
        else:
            self.form_vars['Manual_PE_Present'].set('')

        # PE Location
        pe_loc = str(row.get('Manual_PE_Location', ''))
        self.form_vars['Manual_PE_Location'].set('' if pd.isna(row.get('Manual_PE_Location')) else pe_loc)

        # PE Acuity
        pe_acuity = str(row.get('Manual_PE_Acuity', ''))
        self.form_vars['Manual_PE_Acuity'].set('' if pd.isna(row.get('Manual_PE_Acuity')) else pe_acuity)

        # PE Laterality
        pe_lat = str(row.get('Manual_PE_Laterality', ''))
        self.form_vars['Manual_PE_Laterality'].set('' if pd.isna(row.get('Manual_PE_Laterality')) else pe_lat)

        # PE Clot Burden
        pe_burden = str(row.get('Manual_PE_Clot_Burden', ''))
        self.form_vars['Manual_PE_Clot_Burden'].set('' if pd.isna(row.get('Manual_PE_Clot_Burden')) else pe_burden)

        # Confidence
        conf = str(row.get('Reviewer_Confidence', ''))
        self.form_vars['Reviewer_Confidence'].set('' if pd.isna(row.get('Reviewer_Confidence')) else conf)

        # Comments
        self.comments_text.delete('1.0', tk.END)
        comments = row.get('Comments', '')
        if not pd.isna(comments):
            self.comments_text.insert('1.0', str(comments))

    def update_statistics(self):
        """Update review statistics"""
        total = len(self.df)
        reviewed = self.df['Manual_PE_Present'].notna().sum()
        remaining = total - reviewed
        pct = (reviewed / total * 100) if total > 0 else 0

        stats_text = f"Reviewed: {reviewed}/{total} ({pct:.1f}%) • Remaining: {remaining}"
        self.stats_label.config(text=stats_text)

    def show_ai_agreement(self, row):
        """Show if AI predictions agree with manual review"""
        manual_pe = row.get('Manual_PE_Present')

        # Only show if manual review exists
        if pd.isna(manual_pe):
            return

        manual_pe = int(float(manual_pe))
        llm_pe = int(row.get('LLM_PE_Binary', -1))
        svm_pe = int(row.get('SVM_PE_Prediction', -1))

        agreements = []
        if llm_pe == manual_pe:
            agreements.append("LLM")
        if svm_pe == manual_pe:
            agreements.append("SVM")

        if len(agreements) == 2:
            msg = "✓ All AI models agree"
            color = self.colors['success']
        elif len(agreements) == 1:
            msg = f"⚠ Only {agreements[0]} agrees"
            color = self.colors['warning']
        else:
            msg = "✗ AI models disagree"
            color = self.colors['danger']

        # We could display this somewhere, but for now just store it
        # Could add to status_label or a separate indicator

    def skip_to_unreviewed(self):
        """Skip to next unreviewed report"""
        start_idx = self.current_index + 1
        for idx in range(start_idx, len(self.df)):
            pe_present = self.df.iloc[idx].get('Manual_PE_Present')
            if pd.isna(pe_present) or str(pe_present).strip() == '':
                self.load_report(idx)
                return

        # If no unreviewed found after current, search from beginning
        for idx in range(0, self.current_index):
            pe_present = self.df.iloc[idx].get('Manual_PE_Present')
            if pd.isna(pe_present) or str(pe_present).strip() == '':
                self.load_report(idx)
                return

        messagebox.showinfo("Complete", "All reports have been reviewed!")

    def validate_form(self):
        """Validate form before saving"""
        errors = []

        # Check PE Present
        pe_present = self.form_vars['Manual_PE_Present'].get()
        if not pe_present:
            errors.append("PE Present is required")

        # Check confidence
        confidence = self.form_vars['Reviewer_Confidence'].get()
        if not confidence:
            errors.append("Reviewer Confidence is required")

        # If PE present, check PE characteristics
        if pe_present == "1":
            if not self.form_vars['Manual_PE_Location'].get():
                errors.append("PE Location is required when PE is present")
            if not self.form_vars['Manual_PE_Acuity'].get():
                errors.append("PE Acuity is required when PE is present")
            if not self.form_vars['Manual_PE_Laterality'].get():
                errors.append("PE Laterality is required when PE is present")
            if not self.form_vars['Manual_PE_Clot_Burden'].get():
                errors.append("PE Clot Burden is required when PE is present")

        return errors

    def save_current(self):
        """Save current review to DataFrame"""
        errors = self.validate_form()

        if errors:
            messagebox.showwarning("Validation Error",
                                  "Please complete required fields:\n\n" +
                                  "\n".join(f"- {e}" for e in errors))
            return False

        # Update DataFrame
        self.df.at[self.current_index, 'Manual_PE_Present'] = int(self.form_vars['Manual_PE_Present'].get())

        pe_present = self.form_vars['Manual_PE_Present'].get()
        if pe_present == "1":
            self.df.at[self.current_index, 'Manual_PE_Location'] = self.form_vars['Manual_PE_Location'].get()
            self.df.at[self.current_index, 'Manual_PE_Acuity'] = self.form_vars['Manual_PE_Acuity'].get()
            self.df.at[self.current_index, 'Manual_PE_Laterality'] = self.form_vars['Manual_PE_Laterality'].get()
            self.df.at[self.current_index, 'Manual_PE_Clot_Burden'] = self.form_vars['Manual_PE_Clot_Burden'].get()
        else:
            # Clear PE characteristics if no PE
            self.df.at[self.current_index, 'Manual_PE_Location'] = ''
            self.df.at[self.current_index, 'Manual_PE_Acuity'] = ''
            self.df.at[self.current_index, 'Manual_PE_Laterality'] = ''
            self.df.at[self.current_index, 'Manual_PE_Clot_Burden'] = ''

        self.df.at[self.current_index, 'Reviewer_Confidence'] = self.form_vars['Reviewer_Confidence'].get()
        self.df.at[self.current_index, 'Comments'] = self.comments_text.get('1.0', tk.END).strip()

        # Save to CSV
        try:
            self.df.to_csv(self.csv_path, index=False)
            self.unsaved_changes = False
            self.show_status("✓ Saved", self.colors['success'])
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
            return False

    def next_report(self):
        """Navigate to next report"""
        if self.save_current():
            if self.current_index < len(self.df) - 1:
                self.load_report(self.current_index + 1)
            else:
                messagebox.showinfo("Complete",
                                   "You've reached the last report!\n\n" +
                                   "Great work completing the review!")

    def previous_report(self):
        """Navigate to previous report"""
        if self.current_index > 0:
            self.load_report(self.current_index - 1)

    def jump_to_report(self):
        """Jump to specific report number"""
        try:
            index = int(self.jump_var.get()) - 1
            if 0 <= index < len(self.df):
                self.load_report(index)
                self.jump_var.set('')
            else:
                messagebox.showwarning("Invalid",
                                      f"Please enter a number between 1 and {len(self.df)}")
        except ValueError:
            messagebox.showwarning("Invalid", "Please enter a valid number")

    def show_status(self, message, color=None):
        """Show a temporary status message"""
        if color is None:
            color = self.colors['success']

        self.status_label.config(text=message, fg=color)
        # Clear status after 2 seconds
        self.after(2000, lambda: self.status_label.config(text=""))

    def bind_shortcuts(self):
        """Bind keyboard shortcuts"""
        # Navigation shortcuts
        self.bind('<Control-s>', lambda e: self.save_current())
        self.bind('<Right>', lambda e: self.next_report())
        self.bind('<Left>', lambda e: self.previous_report())
        self.bind('<Control-k>', lambda e: self.skip_to_unreviewed())

        # Quick selection shortcuts
        # Press 0 for No PE, 1 for PE Present
        self.bind('0', lambda e: self.quick_select_pe('0'))
        self.bind('1', lambda e: self.quick_select_pe('1'))

    def quick_select_pe(self, value):
        """Quick select PE present/absent"""
        if hasattr(self, 'form_vars') and 'Manual_PE_Present' in self.form_vars:
            self.form_vars['Manual_PE_Present'].set(value)


def main():
    """Launch the application"""
    app = MedicalReportReviewer()
    app.mainloop()


if __name__ == "__main__":
    main()
