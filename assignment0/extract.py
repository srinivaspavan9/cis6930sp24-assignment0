from PyPDF2 import PdfReader

def extract_incidents(pdf_path):
    reader = PdfReader(pdf_path)
    incidents = []
    for page in reader.pages:
        text = page.extract_text()
        # Process the text to extract date/time, incident number, location, nature, incident ORI
        # This will likely involve regular expressions and string manipulation
        # Append extracted data to incidents list as a tuple or dictionary
    return incidents

# Example usage might require adapting depending on your PDF structure
# incidents = extract_incidents("path/to/incident_report.pdf")

