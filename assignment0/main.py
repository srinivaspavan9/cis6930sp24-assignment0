import argparse
import sqlite3
import requests
from pypdf import PdfReader
import os

# from PyPDF2 import PdfReader


# Database functions
def create_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
                   date_time TEXT, 
                   incident_number TEXT, 
                   location TEXT, 
                   nature TEXT, 
                   incident_ori TEXT)''')
    conn.commit()
    conn.close()

def insert_incidents(db_path, incidents):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for incident in incidents:
        query = f"INSERT INTO incidents (date_time, incident_number, location, nature, incident_ori) " \
                f"VALUES ('{incident[0]}', '{incident[1]}', '{incident[2]}', '{incident[3]}', '{incident[4]}')"
        cur.execute(query)
    conn.commit()
    conn.close()

# Download function
def download_pdf(url):
    save_path="./docs/incident_report.pdf"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

# Extract function
def extract_incidents(pdf_path):
    reader = PdfReader(pdf_path)
    # page=reader.pages[0]
    # return page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
    newincidents = []
    incidents = []
    for page in reader.pages:
        text = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
        lines = text.split('\n')  # Split text into lines
        incidents.extend(lines)  # Append each line to the incidents list
    del incidents[:3]
    del incidents[-1]
    for row in incidents:
            # Split each line by "more than 2 spaces"
            row_data = [cell.strip() for cell in row.split('  ') if cell.strip()]
            newincidents.append(row_data)
    return newincidents

# Status function 
def summarize_data(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''SELECT nature, COUNT(*) as count 
                   FROM incidents 
                   GROUP BY nature 
                   ORDER BY count DESC, nature''')
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}|{row[1]}")
    conn.close()


# Main function
def main(url):
    # Download data
    pdf_path = "./docs/incident_report.pdf"
    download_pdf(url)

    # Extract data
    incidents = extract_incidents(pdf_path)

    # Create a new database
    db_path = "./normanpd.db"
    create_db(db_path)

    # Insert data into the database
    insert_incidents(db_path, incidents)

    # Print incident counts
    summarize_data(db_path)

# Entry point of the script
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)