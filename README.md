# Tortured Phrase Spotter

A tool for searching and highlighting "tortured" phrases in text with recommendations for replacement.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install openpyxl flask PyPDF2
   ```

## Usage

1. Place the text to analyze in the `sample.txt` file (UTF-8) or prepare a `.pdf` file.
2. Make sure the phrases and recommendations file is named `🤷_tortured.csv` and is in the project root.
3. Run the tool:
   ```
   python3 src/run_spotter.py
   ```
   or for the web interface:
   ```
   python3 src/app.py
   ```
4. Results will appear in the console and in the files `report.html` and `report.txt` (or in the web interface).

## Project Structure

- `src/` — source code
- `🤷_tortured.csv` — CSV file with phrases to search and recommendations (1st column — search, 2nd — recommend)
- `sample.txt` — text for analysis
- `report.html` — HTML report with highlighted phrases and recommendations
- `report.txt` — text report with results

## Editing the Phrase List

1. Open the `🤷_tortured.csv` file in a spreadsheet editor (Excel, Numbers, LibreOffice, etc.).
2. Enter the phrases to search for in the first column.
3. Enter the replacement recommendations in the second column.
4. Save the file as CSV (UTF-8).

## Example of 🤷_tortured.csv

```
"Fingerprint - Tortured Phrase","Expected Text"
"tortured phrase","simple phrase"
"complex expression","simple expression"
```

## Example sample.txt

```
This is a tortured phrase. Here is a complex expression.
```

## Example Report

- `report.html` — open in a browser to view highlighted phrases and recommendations.
- `report.txt` — text version of the report for quick review.
