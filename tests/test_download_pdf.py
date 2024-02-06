# test_download_pdf.py
import os
import requests
from assignment0.main import download_pdf

def test_download_pdf(tmpdir):
    # Replace with a valid URL to test
    url = 'https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-01_daily_incident_summary.pdf'

    # Call the download_pdf() function
    download_pdf(url)

    # Check if the PDF file was downloaded successfully
    pdf_path = "./docs/incident_report.pdf"
    assert os.path.exists(pdf_path)

    # Clean up the downloaded PDF file
    os.remove(pdf_path)
