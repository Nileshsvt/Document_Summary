# from flask import Flask, request, render_template
# import os
# from ocr import extract_text_from_image, extract_text_from_pdf
# from summarizer import summarize_text
# from keypoints import extract_key_points

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def home():
#     return render_template('upload.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['file']
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)

#     # OCR Processing
#     if file.filename.endswith('.pdf'):
#         text = extract_text_from_pdf(file_path)
#     else:
#         text = extract_text_from_image(file_path)

#     # Summarization
#     summary = summarize_text(text)

#     # Key Point Extraction
#     key_points = extract_key_points(text)

#     return render_template('result.html', text=text, summary=summary, key_points=key_points)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template, url_for
# import os
# from ocr import extract_text_from_image, extract_text_from_pdf
# from summarizer import summarize_text
# from keypoints import extract_key_points
# from werkzeug.utils import secure_filename
# import uuid

# app = Flask(__name__)

# # Define the upload folder
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure the uploads directory exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def home():
#     """
#     Render the upload page.
#     """
#     return render_template('upload.html')


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     """
#     Handle file upload, process the file (OCR, summarization, key point extraction),
#     and render the result page.
#     """
#     if 'file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['file']
#     filename = secure_filename(file.filename)
#     unique_filename = f"{uuid.uuid4().hex}_{filename}"
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
#     file.save(file_path)

#     # Determine file type for preview
#     file_url = url_for('static', filename=f"uploads/{unique_filename}", _external=True)
#     file_type = 'image' if filename.lower().endswith(('png', 'jpg', 'jpeg')) else 'pdf' if filename.lower().endswith('pdf') else 'unknown'

#     # OCR Processing
#     if file_type == 'pdf':
#         text = extract_text_from_pdf(file_path)
#     elif file_type == 'image':
#         text = extract_text_from_image(file_path)
#     else:
#         return render_template('result.html', file_url=file_url, file_type=file_type, text="Unsupported file type.", summary="", key_points=[])

#     # Validate extracted text
#     if not text.strip():
#         return render_template('result.html', file_url=file_url, file_type=file_type, text="No text could be extracted from the document.", summary="", key_points=[])

#     # Summarization
#     summary = summarize_text(text)

#     # Key Point Extraction
#     key_points = extract_key_points(text)

#     # Render the result page
#     return render_template('result.html', file_url=file_url, file_type=file_type, text=text, summary=summary, key_points=key_points)


# @app.route('/health', methods=['GET'])
# def health_check():
#     """
#     Health check endpoint to ensure the application is running.
#     """
#     return "Document Summary Assistant is running!", 200


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template, url_for
# import os
# from ocr import extract_text_from_image, extract_text_from_pdf
# from summarizer import summarize_text
# from keypoints import extract_key_points
# from werkzeug.utils import secure_filename
# import uuid

# app = Flask(__name__)

# # Define the upload folder
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure the uploads directory exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def home():
#     """
#     Render the upload page.
#     """
#     return render_template('upload.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     """
#     Handle file upload, process the file (OCR, summarization, key point extraction),
#     and render the result page.
#     """
#     if 'file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['file']
#     filename = secure_filename(file.filename)
#     unique_filename = f"{uuid.uuid4().hex}_{filename}"
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
#     file.save(file_path)

#     # Determine file type for preview
#     file_url = url_for('static', filename=f"uploads/{unique_filename}", _external=True)
#     file_type = 'image' if filename.lower().endswith(('png', 'jpg', 'jpeg')) else 'pdf' if filename.lower().endswith('pdf') else 'unknown'

#     # OCR Processing
#     if file_type == 'pdf':
#         text = extract_text_from_pdf(file_path)
#     elif file_type == 'image':
#         text = extract_text_from_image(file_path)
#     else:
#         return render_template('result.html', file_url=file_url, file_type=file_type, text="Unsupported file type.", summary="", key_points=[])

#     # Validate extracted text
#     if not text.strip():
#         return render_template('result.html', file_url=file_url, file_type=file_type, text="No text could be extracted from the document.", summary="", key_points=[])

#     # Summarization
#     summary = summarize_text(text)

#     # Key Point Extraction
#     key_points = extract_key_points(text)

#     # Render the result page
#     return render_template('result.html', file_url=file_url, file_type=file_type, text=text, summary=summary, key_points=key_points)

# @app.route('/health', methods=['GET'])
# def health_check():
#     """
#     Health check endpoint to ensure the application is running.
#     """
#     return "Document Summary Assistant is running!", 200

# if __name__ == '__main__':
#     app.run(debug=True)



# long pdf-->

# from flask import Flask, request, render_template, url_for
# import os
# from ocr import extract_text_from_image, extract_text_from_pdf
# from summarizer import summarize_text
# from keypoints import extract_key_points
# from werkzeug.utils import secure_filename
# import uuid

# app = Flask(__name__)

# # Define the upload folder
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure the uploads directory exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def home():
#     """
#     Render the upload page.
#     """
#     return render_template('upload.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     """
#     Handle file upload, process the file (OCR, summarization, key point extraction),
#     and render the result page.
#     """
#     if 'file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['file']
#     filename = secure_filename(file.filename)
#     unique_filename = f"{uuid.uuid4().hex}_{filename}"
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
#     file.save(file_path)

#     # Determine file type for preview
#     file_url = url_for('static', filename=f"uploads/{unique_filename}", _external=True)
#     file_type = 'image' if filename.lower().endswith(('png', 'jpg', 'jpeg')) else 'pdf' if filename.lower().endswith('pdf') else 'unknown'

#     # OCR Processing
#     try:
#         if file_type == 'pdf':
#             text = extract_text_from_pdf(file_path)
#         elif file_type == 'image':
#             text = extract_text_from_image(file_path)
#         else:
#             return render_template('result.html', file_url=file_url, file_type=file_type, text="Unsupported file type.", summary="", key_points=[])

#         # Validate extracted text
#         if not text.strip():
#             return render_template('result.html', file_url=file_url, file_type=file_type, text="No text could be extracted from the document.", summary="", key_points=[])

#         # Summarization
#         summary = summarize_text(text)

#         # Key Point Extraction
#         key_points = extract_key_points(text)

#         # Render the result page
#         return render_template('result.html', file_url=file_url, file_type=file_type, text=text, summary=summary, key_points=key_points)
#     except Exception as e:
#         return f"An error occurred while processing the file: {str(e)}", 500

# @app.route('/health', methods=['GET'])
# def health_check():
#     """
#     Health check endpoint to ensure the application is running.
#     """
#     return "Document Summary Assistant is running!", 200

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template, url_for
import os
from ocr import extract_text_from_image, extract_text_from_pdf
from summarizer import summarize_text
from keypoints import extract_key_points
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    """
    Render the upload page.
    """
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload, process the file (OCR, summarization, key point extraction),
    and render the result page.
    """
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{filename}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(file_path)

    # Determine file type for preview
    file_url = url_for('static', filename=f"uploads/{unique_filename}", _external=True)
    file_type = 'image' if filename.lower().endswith(('png', 'jpg', 'jpeg')) else 'pdf' if filename.lower().endswith('pdf') else 'unknown'

    # OCR Processing
    try:
        if file_type == 'pdf':
            text = extract_text_from_pdf(file_path)
        elif file_type == 'image':
            text = extract_text_from_image(file_path)
        else:
            return render_template('result.html', file_url=file_url, file_type=file_type, text="Unsupported file type.", summary="", key_points=[])

        # Validate extracted text
        if not text.strip():
            return render_template('result.html', file_url=file_url, file_type=file_type, text="No text could be extracted from the document.", summary="", key_points=[])

        # Summarization
        try:
            summary = summarize_text(text)
        except Exception as e:
            summary = f"Error summarizing text: {str(e)}"

        # Key Point Extraction
        try:
            key_points = extract_key_points(text)
        except Exception as e:
            key_points = [f"Error extracting key points: {str(e)}"]

        # Render the result page
        return render_template('result.html', file_url=file_url, file_type=file_type, text=text, summary=summary, key_points=key_points)
    except Exception as e:
        return f"An error occurred while processing the file: {str(e)}", 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to ensure the application is running.
    """
    return "Document Summary Assistant is running!", 200

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))  # Default to port 5000 if not set
    app.run(host='0.0.0.0', port=port, debug=True)
