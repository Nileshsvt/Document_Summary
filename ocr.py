import pytesseract
from pdf2image import convert_from_path

def extract_text_from_image(image_path):
    """Extracts text from an image file."""
    try:
        return pytesseract.image_to_string(image_path)
    except Exception as e:
        print(f"Error extracting text from image: {str(e)}")
        return ""

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        pages = convert_from_path(pdf_path)
        text = ''
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return ""
