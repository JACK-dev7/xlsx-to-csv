
import sys
import os
import re

import pandas as pd
import requests


def download_google_sheet(url):
    """Download a Google Sheet as an Excel file."""

    match = re.search(r"/d/([a-zA-Z0-9_-]+)", url)

    if not match:
        raise ValueError("Invalid Google Sheets URL")

    spreadsheet_id = match.group(1)

    download_url = (
        f"https://docs.google.com/spreadsheets/d/"
        f"{spreadsheet_id}/export?format=xlsx"
    )

    response = requests.get(download_url, timeout=30)
    response.raise_for_status()

    downloaded_file = spreadsheet_id + ".xlsx"

    with open(downloaded_file, "wb") as file:
        file.write(response.content)

    print("Google Sheet downloaded successfully!")

    return downloaded_file


def convert_excel_to_csv(input_file):
    """Convert every sheet in an Excel workbook into separate CSV files."""

    if not os.path.exists(input_file):
        raise FileNotFoundError("File does not exist!")

    if not input_file.lower().endswith(".xlsx"):
        raise ValueError("Please provide an XLSX file")

    excel_file = pd.ExcelFile(input_file)

    output_dir = os.path.splitext(input_file)[0]
    os.makedirs(output_dir, exist_ok=True)

    for sheet in excel_file.sheet_names:

        df = pd.read_excel(excel_file, sheet_name=sheet)

        safe_sheet_name = re.sub(r'[<>:"/\\|?*]', "_", sheet)

        csv_path = os.path.join(
            output_dir,
            safe_sheet_name + ".csv"
        )

        df.to_csv(csv_path, index=False)

        print(f"Converted: {sheet}")

    excel_file.close()

    print("Conversion completed successfully!")
    print(f"Output directory: {output_dir}")


def main():
    """Handle command-line input and execute conversion."""

    if len(sys.argv) != 2:
        print("Usage: python converter.py <file_path_or_google_sheet_url>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        if input_file.startswith(
            "https://docs.google.com/spreadsheets/"
        ):
            print("Google Sheets link detected")
            input_file = download_google_sheet(input_file)

        else:
            print("Local Excel file detected")

        convert_excel_to_csv(input_file)

    except (
        ValueError,
        FileNotFoundError,
        requests.exceptions.RequestException,
        OSError,
        ImportError,
    ) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
