from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_enquiry', methods=['POST'])
def send_enquiry():
    data = request.get_json()
    name = data.get('name', '')
    phone = data.get('phone', '')
    service = data.get('service', '')
    message = data.get('message', '')

    # Optional: configure email sending here
    # For now just return success
    print(f"New Enquiry — Name: {name}, Phone: {phone}, Service: {service}, Message: {message}")
    return jsonify({'status': 'success', 'message': 'Enquiry received!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
