# CIS 6930 Spring 2024 Assignment 0 - Incident Report Analysis

## Author
Srinivas Pavan Singh Runval

## Overview
This project automates the extraction and organization of incident report data from PDFs provided by the Norman, Oklahoma police department. It focuses on parsing these documents, extracting relevant information, and storing it in a SQLite database for analysis.

## Installation Instructions
1. **Clone the repository:** Clone or download this repository to your local machine.
2. **Install pipenv:** If not already installed, use `pip install pipenv` to install pipenv.
3. **Set up the environment:**
   - Navigate to the project directory.
   - Run `pipenv install` to create a virtual environment and install dependencies: argparse, sqlite3, requests, pypdf2, and ensure `os` module is available (comes with Python).

## Running the Project
Execute the project with the following command:
```bash
pipenv run python assignment0/main.py --incidents <URL>
```

## Project Functions

### `create_db()`
- **Purpose:** Initializes the SQLite database, creating an `incidents` table.
- **Process:** Sets up the database schema for storing extracted data.

### `download_pdf(url)`
- **Parameters:** `url` - The URL for downloading incident PDFs.
- **Process:** Ensures the directory exists for storing PDFs, then downloads the file.
- **Return:** Saves the PDF to a local path; returns nothing.

### `extract_incidents()`
- **Process:** Identifies and extracts data from PDF tables using an adaptive strategy.
- **Return:** Organizes data into a list of lists, each representing an incident.

### `insert_incidents()`
- **Process:** Inserts data from `extract_incidents()` into the database.
- **Return:** Data is stored; returns nothing.

### `summarize_data()`
- **Process:** Counts and sorts incident types from the database.
- **Return:** Prints a summary of incidents by type with counts.

**Note:** This project uses an adaptive PDF parsing approach, enhancing flexibility and efficiency. No demo is currently available.

## How to Use
- **Setup:** Follow installation instructions to prepare the environment.
- **Execution:** Use the command with the specific URL to process incident reports.
- **Support:** For further information, consult the assignment guidelines or contact the author.
