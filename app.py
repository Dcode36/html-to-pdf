from flask import Flask, request, send_from_directory, jsonify
from weasyprint import HTML
import os
import uuid

app = Flask(__name__)

# Folder to store generated PDFs
PDF_FOLDER = 'pdfs'
os.makedirs(PDF_FOLDER, exist_ok=True)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    html = request.get_data(as_text=True)
    if not html:
        return jsonify({'error': 'No HTML provided'}), 400

    # Create a unique filename
    file_id = str(uuid.uuid4())
    filename = f"{file_id}.pdf"
    filepath = os.path.join(PDF_FOLDER, filename)

    try:
        # Generate PDF using WeasyPrint
        print(f"Creating PDF from HTML: {html[:100]}...")
        html_doc = HTML(string=html)
        html_doc.write_pdf(target=filepath)
        print(f"PDF created successfully at {filepath}")
    except Exception as e:
        print(f"Error creating PDF: {str(e)}")
        return jsonify({'error': f"PDF generation failed: {str(e)}"}), 500

    # Return a public URL to access the PDF
    pdf_url = f"{request.host_url}pdf/{filename}"
    return jsonify({'pdf_url': pdf_url})

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    return send_from_directory(PDF_FOLDER, filename)

@app.route('/')
def index():
    return "HTML to PDF Server is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
