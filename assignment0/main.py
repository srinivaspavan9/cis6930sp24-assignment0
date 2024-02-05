import argparse
from assignment0.download import download_pdf
from assignment0.extract import extract_incidents
from assignment0.database import create_db, insert_incidents
from assignment0.summarize import summarize_data

def main(url):
    # Download data
    pdf_path = "incident_report.pdf"
    download_pdf(url, pdf_path)

    # Extract data
    incidents = extract_incidents(pdf_path)

    # Create a new database
    db_path = "normanpd.db"
    create_db(db_path)

    # Insert data into the database
    insert_incidents(db_path, incidents)

    # Print incident counts
    summarize_data(db_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

