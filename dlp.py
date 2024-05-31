import os
import re
import docx
import PyPDF2
import openpyxl
from pptx import Presentation
from pdfminer.high_level import extract_text as extract_text_from_pdf
from colorama import Fore, Style

def load_ad_soyad_listesi(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        ad_soyad_listesi = [line.strip() for line in file.readlines()]
    return ad_soyad_listesi

def extract_text_from_docx(docx_path):
    try:
        doc = docx.Document(docx_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except docx.opc.exceptions.PackageNotFoundError:
        print(f"Hata: Dosya bulunamadı veya açılamadı: {docx_path}")
        return ""

def extract_text_from_pdf_path(pdf_path):
    try:
        return extract_text_from_pdf(pdf_path)
    except Exception as e:
        print(f"Hata: PDF dosyasından metin çıkarılamadı: {pdf_path}. Hata: {e}")
        return ""

def extract_text_from_excel(excel_path):
    try:
        wb = openpyxl.load_workbook(excel_path)
        full_text = []
        for sheet in wb.worksheets:
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value:
                        full_text.append(str(cell.value))
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Hata: Excel dosyasından metin çıkarılamadı: {excel_path}. Hata: {e}")
        return ""

def extract_text_from_pptx(pptx_path):
    try:
        prs = Presentation(pptx_path)
        full_text = []
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    full_text.append(shape.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Hata: PowerPoint dosyasından metin çıkarılamadı: {pptx_path}. Hata: {e}")
        return ""

def find_matches(text, regex_patterns, ad_soyad_listesi):
    matches = {}
    for label, regex in regex_patterns.items():
        found = re.findall(regex, text)
        if found:
            matches[label] = found

    # Ad Soyad araması
    ad_soyad_matches = []
    for ad_soyad in ad_soyad_listesi:
        if ad_soyad in text:
            ad_soyad_matches.append(ad_soyad)

    if ad_soyad_matches:
        matches["Ad Soyad"] = ad_soyad_matches

    return matches

def extract_text_from_file(file_path):
    if file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        return extract_text_from_pdf_path(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return extract_text_from_excel(file_path)
    elif file_path.endswith('.pptx'):
        return extract_text_from_pptx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

def find_files_with_regex(root_dir, regex_patterns, ad_soyad_listesi):
    matched_files = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.startswith('~$'):
                # Skip temporary files
                continue
            file_path = os.path.join(dirpath, filename)
            try:
                text = extract_text_from_file(file_path)
                if text:  # Only process if text extraction was successful
                    matches = find_matches(text, regex_patterns, ad_soyad_listesi)
                    if matches:
                        matched_files.append((file_path, matches))
            except (IOError, ValueError) as e:
                print(f"Hata: {file_path} dosyası işlenirken bir hata oluştu. Hata: {e}")
                continue

    return matched_files

def main():
    root_directory = input("Taranacak kök dizini girin: ")
    ad_soyad_listesi = load_ad_soyad_listesi("ad_soyad_listesi.txt")

    regex_patterns = {
        "E-posta": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "TCKN": r'\b[1-9][0-9]{10}\b',  # 11 haneli ve 0 ile başlamayan sayılar
       "Telefon": r'\b(\+90\s?)?(5\d{2}\s?\d{3}\s?\d{2}\s?\d{2}|5\d{2}-\d{3}-\d{2}-\d{2}|(\(5\d{2}\)\s?\d{3}\s?\d{2}\s?\d{2})|(\(5\d{2}\)-\d{3}-\d{2}-\d{2}))\b', 
        "Okul No": r'\b\d{10}\b'  # 9 haneli okul numaraları
    }

    matched_files = find_files_with_regex(root_directory, regex_patterns, ad_soyad_listesi)

    if matched_files:
        print(f"{Fore.GREEN}Belirtilen kalıplara uyan dosyalar:{Style.RESET_ALL}")
        for file_path, matches in matched_files:
            print(f"\nDosya: {file_path}")
            for label, found_matches in matches.items():
                print(f"{Fore.GREEN}  {label}:{Style.RESET_ALL}")
                for match in found_matches:
                    print(f"    {match}")
    else:
        print(f"{Fore.YELLOW}Hiçbir dosyada belirtilen kalıplara uyan içerik bulunamadı.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
