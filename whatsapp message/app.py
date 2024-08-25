from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Load environment variables (make sure to create a .env file with your Twilio credentials)
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.environ.get('TWILIO_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    data = request.json
    to_number = data['to']
    message_body = data['message']

    try:
        message = client.messages.create(
            body=message_body,
            from_=f'whatsapp:{twilio_whatsapp_number}',
            to=f'whatsapp:{to_number}'
        )
        return jsonify({'status': 'Message sent', 'message_sid': message.sid}), 200
    except Exception as e:
        return jsonify({'status': 'Failed to send message', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
