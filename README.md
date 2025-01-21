
# Document Summary Assistant

The **Document Summary Assistant** is a Flask-based web application that processes uploaded documents (images or PDFs) to extract and summarize text. It provides users with a summarized version of the extracted text along with key points, making it easier to comprehend large amounts of information.

---

## Features

### 1. Document Upload
- Supports the upload of **images** (JPEG, PNG) and **PDFs**.
- Ensures secure handling of files with unique filenames.

### 2. Text Extraction
- Utilizes **Tesseract OCR** for extracting text from images and PDFs.
- Processes multi-page PDFs seamlessly.

### 3. Summarization
- Generates concise summaries of the extracted text using **natural language processing (NLP)**.
- Summaries are tailored based on the text content.

### 4. Key Points Extraction
- Extracts and displays key points from the summarized text for quick insights.

---

## Technical Stack

### Backend
- **Flask**: Web framework for handling routes and file processing.
- **Tesseract OCR**: For text extraction from images and PDFs.
- **Python Libraries**:
  - `transformers`: For text summarization.
  - `pytesseract`: Python wrapper for Tesseract OCR.
  - `pdf2image`: Converts PDF pages into images for OCR.

### Frontend
- **HTML5/CSS3**: For the user interface.
- **JavaScript**: For interactivity and dynamic behavior.

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Tesseract OCR installed on the system.
- A virtual environment for Python is recommended.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nileshsvt/Document_Summary.git
   cd Document_Summary
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR**:
   - For Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install -y tesseract-ocr
     ```
   - For Windows:
     Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open your browser and navigate to: `http://127.0.0.1:5000/`

---

## Usage

1. **Upload a File**:
   - Navigate to the home page and upload an image or PDF.

2. **View Extracted Text**:
   - The application will display the text extracted from the uploaded document.

3. **Summary and Key Points**:
   - A summarized version of the text along with key points will be displayed.

---

## Evaluation Points

- **Accuracy**:
  - High-quality text extraction using Tesseract OCR.
  - Meaningful summaries and key points based on advanced NLP models.

- **Efficiency**:
  - Handles large documents and multi-page PDFs effectively.

- **User Experience**:
  - Simple and intuitive UI for uploading documents and viewing results.

---

## Future Enhancements

- Support for **multi-language OCR** and summarization.
- Integration with **cloud-based OCR services** for enhanced accuracy.
- Real-time **API support** for third-party integrations.
- **Dark mode** and additional UI enhancements.
