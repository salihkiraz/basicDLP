# basicDLP
A simple DLP tool scans text files according to some rules


This Python script scans files in a specified directory to find occurrences of names from a predefined list. It supports .docx, .pdf, .xlsx, and .pptx file formats.

Prerequisites
Before you begin, ensure you have the following libraries installed:

bash
Kodu kopyala
pip install python-docx openpyxl python-pptx pdfminer.six
Usage
Prepare the Name List:
Create a text file ad_soyad_listesi.txt with the names you want to search for. Each name should be on a new line.

Example ad_soyad_listesi.txt:

Kodu kopyala
Ahmet Yılmaz
Mehmet Demir
Ayşe Kaya
Fatma Şahin
Ali Çelik
Sefa Gözel
Ahmet Günal
Tunahan Efe
Modify the Script:
Ensure the path to your name list is correctly set in the script.

python
Kodu kopyala
def main():
    root_directory = input("Enter the root directory to scan: ")
    ad_soyad_dosyasi = 'path/to/ad_soyad_listesi.txt'  # Set the path to your name list file
    ad_soyad_listesi = load_ad_soyad_listesi(ad_soyad_dosyasi)
    
    matched_files = find_files_with_ad_soyad(root_directory, ad_soyad_listesi)

    if matched_files:
        print("Files containing specified names:")
        for file_path, matches in matched_files:
            print(f"\nFile: {file_path}")
            for match in matches:
                print(f"    {match}")
    else:
        print("No files containing the specified names were found.")
Run the Script:
Execute the script from your command line.

bash
Kodu kopyala
python your_script_name.py
You will be prompted to enter the root directory to scan. The script will then search for the specified names in all supported files within that directory.

Script Details
The script performs the following actions:

Load Names:
Reads the list of names from ad_soyad_listesi.txt.

Extract Text:
Extracts text from .docx, .pdf, .xlsx, and .pptx files.

Find Matches:
Searches for occurrences of the names in the extracted text.

Display Results:
Prints the file paths and matched names if found.

Example Output
plaintext
Kodu kopyala
Enter the root directory to scan: /path/to/directory

Files containing specified names:

File: /path/to/directory/document1.docx
    Ahmet Yılmaz
    Fatma Şahin

File: /path/to/directory/document2.pdf
    Mehmet Demir
    Ayşe Kaya
Notes
Ensure the name list file (ad_soyad_listesi.txt) is correctly formatted and located at the specified path.
The script skips temporary files (starting with ~$).
License
This project is licensed under the MIT License. See the LICENSE file for details.

