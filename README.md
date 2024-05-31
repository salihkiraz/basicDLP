# basicDLP
A simple DLP tool scans text files according to some rules

This Python script scans files in a specified directory to find occurrences of names from a predefined list. It supports `.doc`,`.docx`, `.pdf`, `.xls`, `.xlsx`, `.ppt` and `.pptx` file formats.

## Prerequisites

Before you begin, ensure you have the following libraries installed:

```bash
pip install python-docx openpyxl python-pptx pdfminer.six
```

## Usage
Prepare the Name List:
Create a text file name_list.txt with the names you want to search for. Each name should be on a new line.

## Example name_list.txt:

Ahmet 
Mehmet 
Ayşe 
Fatma 
Ali 
Sefa 
Ahmet 
Tunahan 

## Modify the Script:
Ensure the path to your name list is correctly set in the script.


Run the Script:
Execute the script from your command line.

```bash

python dlp.py

```
You will be prompted to enter the root directory to scan. The script will then search for the specified names in all supported files within that directory.

## Script Details
The script performs the following actions:

## Load Names:
Reads the list of names from ad_soyad_listesi.txt.

## Extract Text:
Extracts text from .docx, .pdf, .xlsx, and .pptx files.

## Find Matches:
Searches for occurrences of the names in the extracted text.

## Display Results:
Prints the file paths and matched names if found.

## Example Output
Enter the root directory to scan: /path/to/directory

## Files containing specified names:

File: /path/to/directory/document1.docx
    Ahmet Yılmaz
    Fatma Şahin

File: /path/to/directory/document2.pdf
    Mehmet Demir
    Ayşe Kaya
## Notes
Ensure the name list file (name_list.txt) is correctly formatted and located at the specified path.
The script skips temporary files (starting with ~$).
## License
This project is licensed under the MIT License. 

