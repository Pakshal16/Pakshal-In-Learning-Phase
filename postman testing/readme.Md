# 🌟 Flask API for File Upload and Text Submission 🌟

Welcome to the guide for setting up and using a Flask API for submitting text and uploading PNG screenshots. This project demonstrates how to build a simple API using Flask, with instructions for setting up a virtual environment, creating the Flask app, and testing it.

## 🛠️ Setup and Configuration

### 1. Open Command Prompt or PowerShell

To start, you need to open either Command Prompt or PowerShell:

- **Command Prompt**: Press `Win + R`, type `cmd`, and hit `Enter`.
- **PowerShell**: Press `Win + R`, type `powershell`, and hit `Enter`.

### 2. Navigate to Your Project Directory

Change to the directory where you want to create your virtual environment:

```bash
cd path\to\your\project
Replace path\to\your\project with the actual path to your project directory.
```

3. Create a Virtual Environment
Create a virtual environment to isolate your project dependencies:

```bash
Copy code
python -m venv venv
```
python is the Python interpreter.
-m venv specifies the module to create the virtual environment.
venv is the directory where the virtual environment will be created.

4. Activate the Virtual Environment
Activate the virtual environment using the appropriate command:

```bash
venv\Scripts\activate
```
5. Install Flask

Install Flask and other required dependencies:
```bash
pip install flask
```

6. Run the Flask Application

Start the Flask development server:
```bash
flask run
```
The server will start running on http://127.0.0.1:5000.

🧪 Testing the API with Postman
1. Open Postman
Ensure Postman is installed and open it.

2. Create a New Request
Set the request method to POST.
Enter the following URL: http://127.0.0.1:5000/api/submit/.

3. Configure the Request Body
Go to the Body tab.
Select form-data.
Add the following key-value pairs:
Key: text, Type: Text, Value: sample text
Key: screenshot, Type: File, Value: (select your PNG file)
4. Send the Request
Click the Send button to submit the request.

5. Check the Response
If successful, you will receive a JSON response with the text and the path to the uploaded screenshot.

⚠️ Handling Common Issues
405 Method Not Allowed: Ensure you are using a POST request, not GET.
Invalid File Format: Ensure the uploaded file is a valid PNG.
🔔 Notes
This application is intended for development and testing purposes. For production use, consider using a production WSGI server like gunicorn.
Ensure the uploads/ directory exists and is writable by the Flask application.