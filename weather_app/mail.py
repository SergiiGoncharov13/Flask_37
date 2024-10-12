from flask import Flask, jsonify, request
from flask_mail import Mail, Message

import time
import requests
import json

from database import create_subscription, get_all_emails

# https://www.fakemail.net
email = 'email_from_fakemail'
password = 'password_from_fakemail'


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.ukr.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_DEFAULT_SENDER'] = email
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
app.app_context().push()


def create_mail_with_data_from_api():
    response = requests.get('http://localhost:5000/get_weather?location=lviv')
    raw_content = response.content

    json_string = raw_content.decode('utf-8')
    weather_data = json.loads(json_string)

    email_text = f"Weather Update for {weather_data['name']}:\n"
    email_text += f"Temperature: {weather_data['main']['temp']}°C\n"
    email_text += f"Feels Like: {weather_data['main']['feels_like']}°C\n"
    email_text += f"Pressure: {weather_data['main']['pressure']} hPa\n"
    email_text += f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
    email_text += f"Cloudiness: {weather_data['clouds']['all']}%\n"
    email_text += f"{weather_data['weather'][0]['description']}\n"
    email_text += f"Visibility: {weather_data['visibility']} meters\n"
    
    return email_text

def send_email():
    msg = Message('Event reminder', recipients=get_all_emails())
    msg.body = 'Your daily weather'
    msg.html = create_mail_with_data_from_api()
    mail.send(msg)
    print('Email sent')


@app.route('/create_subscription', methods=['POST'])
def subscription():
    email = request.form.get('email')
    if email:
        create_subscription(email)
        return jsonify(message='Subscription add successufully')
    else:
        return jsonify(error='Email not provided'), 400



if __name__ == '__main__':
    app.run(port=3000)
