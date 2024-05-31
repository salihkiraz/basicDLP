# Basic DLP (Data Loss Prevention) Tool
This Python application provides a basic Data Loss Prevention (DLP) functionality by scanning files within a specified directory for sensitive information patterns. It supports various file formats such as .docx, .pdf, .xlsx, .pptx, and .txt.

# Installation
To use this tool, follow these steps:

# Clone or download the repository to your local machine.
Ensure you have Python installed on your system.
Install the required dependencies by running:


pip install python-docx openpyxl python-pptx pdfminer.six colorama tqdm

# Usage
Running the Application

Run the application by executing the dlp_tool.py file using Python. This will open a GUI (Graphical User Interface) window.


python dlp_tool.py

Scanning Files
Select Directory: Click on the "Browse" button to select the directory you want to scan.
Start Scan: Click on the "Start Scan" button to begin the scan process.
View Results: The tool will display any files containing sensitive information patterns in the scrolled text area.
Supported Patterns
The tool searches for the following sensitive information patterns:

E-mail: Matches email addresses.
TCKN: Matches Turkish ID numbers (TCKN).
Telephone: Matches Turkish phone numbers.
Student No: Matches 10-digit school numbers.

# Developer Information
This application is developed by Salih KİRAZ. For any inquiries or feedback, you can reach out via email at salihk06@gmail.com.

