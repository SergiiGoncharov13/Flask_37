from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

openweather_api_key = 'secret_key'

# https://www.fakemail.net
email = 'email_from_fakemail'
password = 'password_from_fakemail'


app = Flask(__name__)
CORS(app)


def extract_weather_data(weather_data):
   main = weather_data['main']
   extracted_data = {
       'temp': main['temp'],
       'feels_like': main['feels_like'],
       'temp_min': main['temp_min'],
       'temp_max': main['temp_max'],
       'weather_main': weather_data['weather'][0]['main'],
       'weather_description': weather_data['weather'][0]['description'],
       'wind_speed': weather_data['wind']['speed'],
       'clouds': weather_data['clouds']['all'],
       'dt_txt': weather_data['dt_txt']
   }
   return extracted_data


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather')
def get_weather():
   location = request.args.get('location')
   if location:
       url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweather_api_key}&units=metric'
       response = requests.get(url)
       data = response.json()
       return jsonify(data)
   else:
       return jsonify(error='Location not provided'), 400


@app.route('/get_weather_forecast')
def get_weather_forecast():
   location = request.args.get('location')
   if location:
       url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={openweather_api_key}&units=metric'
       response = requests.get(url)
       data = response.json()

       # get weather info for nearest few days
       forecast = []
       for entry in data['list']:
           extracted_data = extract_weather_data(entry)
           forecast.append(extracted_data)
       return jsonify(forecast)
   else:
       return jsonify(error='Location not provided'), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)



