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
- **Purpose:** function initializes the SQLite database and sets up the table structure necessary for storing the extracted data. It specifically creates a table named incidents with columns designed to hold data about the date and time of the incident, incident number, location, nature of the incident, and the incident ORI. This function lays the foundation for data storage, ensuring a structured format is in place for the incoming parsed data from incident reports.

### `download_pdf(url)`
- **Parameters:** `url` - The URL for downloading incident PDFs.
- **Process:** function actively engages with a specified URL to fetch and download incident report PDFs. Upon receiving the URL, it first verifies or creates a designated directory for storing these PDFs. If the directory doesn't exist, the function takes the initiative to create it, ensuring a structured file storage system. It then proceeds to download the PDF file from the provided URL, saving it within the established directory. This methodical approach ensures that all necessary documents are readily available for the subsequent parsing process.
- **Return:** Saves the PDF to a local path; returns nothing.

### `extract_incidents()`
- **Process:** function, we tackle the challenge of extracting information from complex PDF files containing incident reports. Here's how we do it:

     **Scanning Pages**: We start by scanning each page of the PDF to locate the tables containing incident data.

     **Identifying Structure**: Once we find a table, we analyze its structure to understand how the data is organized. This involves looking for patterns or clues that indicate where each piece of information is located.

     **Adaptive Parsing**: Instead of using rigid rules or patterns (like regex), we adopt an adaptive approach. This means we dynamically adjust our parsing strategy based on what we see in each table. We don't assume that the data will           always be in the same format; instead, we adapt to the specific layout of each table.

     **Line-by-Line Analysis**: We carefully analyze each line of text in the table, looking for clues about which column it belongs to. For example, we might look for keywords or patterns that indicate the start of a new column.
   
     **Column Identification**: By analyzing the position and content of each line, we determine which column each piece of information belongs to. This allows us to accurately separate the data into the correct categories, such as                 date/time, incident number, location, nature of the incident, and incident ORI.

     **Structured Output**: Once we've processed all the lines in the table, we organize the extracted data into a structured format. This typically involves creating a list of lists, where each inner list represents one incident and                contains the relevant information in the correct order..
- **Return:** Organizes data into a list of lists, each representing an incident.

### `insert_incidents()`
- **Process:**  function, we take the structured incident data extracted from the extract_incidents() function and insert it into the incidents table of our SQLite database. Here's how we do it:

     **Structured Data Input:** We receive structured incident data in the form of a list of lists, where each inner list represents one incident and contains the relevant information in the correct order.

     **Database Insertion:** We iterate through each incident in the structured data and insert it into the incidents table of our SQLite database. This involves mapping each piece of extracted information to the corresponding column in 
     the database table.

     **Data Integrity:** By mapping the data fields to the correct columns, we ensure data integrity and consistency within our database. This allows for easy retrieval and analysis of the incident data later on.

     **Efficient Storage:** The structured approach to data insertion ensures efficient storage of incident information in our database. This organized approach facilitates quick access to the data for subsequent analysis and reporting.
- **Return:** Data is stored; returns nothing.

### `summarize_data()`
- **Process:** Counts and sorts incident types from the database.
- **Return:** Prints a summary of incidents by type with counts.

**Note:** This project uses an adaptive PDF parsing approach, enhancing flexibility and efficiency. No demo is currently available.

### How i tested the code 
- **Process:** To thoroughly test all the functions locally, I meticulously created a comprehensive testing environment within the project directory. Firstly, I established temporary folders to emulate the download directory structure where incident PDFs would typically be stored. Within these folders, I strategically placed a variety of pre-downloaded PDF files, each representing different types of incident reports. This step ensured that the project could handle diverse scenarios and data formats effectively. Subsequently, I executed each function individually using the mock data from the PDFs to verify their behavior and functionality. Specifically, I validated the download_pdf() function by providing it with local file paths instead of URLs, ensuring that it correctly retrieved and saved the PDF files. Additionally, I systematically tested the extract_incidents() and insert_incidents() functions to confirm their ability to parse and insert data accurately into the SQLite database. Finally, I executed the summarize_data() function to generate summaries of the incidents stored in the database and cross-checked them with the expected results. This rigorous testing approach facilitated the identification of any potential issues or discrepancies, ensuring the robustness and reliability of all project functions.

## How to Use
- **Setup:** Follow installation instructions to prepare the environment.
- **Execution:** Use the command with the specific URL to process incident reports.
- **Support:** For further information, consult the assignment guidelines or contact the author.
