from pdf2image import convert_from_path

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

from PIL import Image
import pytesseract
import utility

POPPLER_PATH = r'C:\poppler-25.12.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path, file_format):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    for page in pages:
        processed_image = utility.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang = 'eng')
        document_text += '\n' + text

    # print(document_text)
    # return document_text
    # step 2: extract fields from text

    if file_format == "prescription":
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == "patient_details":
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid file format : {file_format}")
        
    return extracted_data
if __name__ == "__main__":
    data = extract('../resources/prescription/pre_2.pdf', 'prescription')
    print(data)

