from flask import (
    Flask, 
    request, 
    jsonify, 
    send_file
)
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/api/submit/', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        text = request.form.get('text')
        screenshot = request.files.get('screenshot')

        if screenshot:
            print(f"Received file: {screenshot.filename}, Content-Type: {screenshot.content_type}")
            
            if screenshot.content_type == 'image/png':
                screenshot_path = os.path.join(app.config['UPLOAD_FOLDER'], screenshot.filename)
                screenshot.save(screenshot_path)

                return jsonify({'status': 'success', 'text': text, 'screenshot_path': screenshot_path})
            else:
                print("Invalid file format received.")
                return jsonify({'status': 'error', 'message': 'Invalid file format. Please upload a PNG file.'})

        return jsonify({'status': 'error', 'message': 'No file received.'})
    else:
        return jsonify({'status': 'error', 'message': 'Only POST requests are allowed.'})


@app.route('/api/upload_excel/', methods=['POST'])
def upload_excel():
    if 'excel_file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part in the request'})

    excel_file = request.files['excel_file']

    if excel_file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'})

    # Check if the file is an Excel file (XLSX or XLS)
    if excel_file and excel_file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
        excel_file_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_file.filename)
        excel_file.save(excel_file_path)
        print(f"Saved Excel file: {excel_file.filename}")

        # Send the Excel file back to the user
        return send_file(excel_file_path, as_attachment=True)
    
    return jsonify({'status': 'error', 'message': 'Invalid file format. Please upload an Excel file (.xlsx or .xls).'})


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
