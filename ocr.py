import pytesseract
from pdf2image import convert_from_path
import os

# Set the path to Tesseract if needed (uncomment and set your path if Tesseract is not detected automatically)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text_from_image(image_path):
    """
    Extracts text from an image file.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: Extracted text from the image.
    """
    try:
        # Check if the image file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(image_path)
        return text.strip()  # Strip whitespace for cleaner output
    except Exception as e:
        print(f"Error extracting text from image: {str(e)}")
        return ""

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Convert PDF pages to images
        pages = convert_from_path(pdf_path)
        
        # Use pytesseract to extract text from each page
        text = ""
        for i, page in enumerate(pages):
            print(f"Processing page {i + 1}/{len(pages)}")
            text += pytesseract.image_to_string(page) + "\n"
        
        return text.strip()  # Strip whitespace for cleaner output
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return ""
