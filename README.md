# XLSX to CSV Converter

A Python script that converts Excel workbooks (`.xlsx`) into individual CSV files. It supports both local Excel files and publicly accessible Google Sheets links.

## Features

- Supports local `.xlsx` files.
- Supports Google Sheets URLs.
- Downloads Google Sheets as Excel files.
- Converts every sheet in a workbook into a separate CSV file.
- Automatically creates an output directory named after the input file.
- Preserves column headers.
- Handles invalid input and download errors.

## Requirements

- Python 3.x
- pandas
- openpyxl
- requests

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd xlsx-to-csv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

**1. Convert a local Excel file**

```bash
python converter.py employees.xlsx
```

**2. Convert a Google Sheet**

```bash
python converter.py "https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit"
```

Note: Google Sheets must be publicly accessible for the download functionality to work.

## Output Structure

For an Excel workbook named `employees.xlsx` containing three sheets:

```text
employees.xlsx
```

The script creates:

```text
employees/
├── Employees.csv
├── Departments.csv
└── Projects.csv
```

Each sheet is exported as an individual CSV file inside the output directory.

## Project Structure

```text
xlsx-to-csv/
├── converter.py
├── requirements.txt
└── README.md
```

## Technologies Used

- **Python** – Core programming language.
- **Pandas** – Reading Excel workbooks and exporting CSV files.
- **Requests** – Downloading Google Sheets.
- **OS** – File and directory management.
- **Regex** – Extracting spreadsheet IDs from Google Sheets URLs.

## Error Handling

The script handles:
- Missing input files.
- Invalid Google Sheets URLs.
- Unsupported file formats.
- HTTP and download errors.
- Missing command-line arguments.

## Author

Developed as a Python assignment to practice file handling, data conversion, command-line arguments, and working with external APIs.