import requests 
import configparser

from requests import api
from flask import Flask 
from flask import render_template  
from flask import request

#take in a zip code and API key and return the result of calling the API
#calling and parsing the weather api

app = Flask(__name__) 

@app.route('/')
def weather_dashboard(): 
    return render_template('home.html')

@app.route('/results', methods = ['POST'])
def render_results(): 
    zip_code = request.form['zipCode']

    api_key = get_api_key()
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html', location=location, 
    temp = temp, feels_like = feels_like, weather = weather)

    #return "Zip Code: "  + zip_code

def get_api_key(): 
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_results(zip_code, api_key): 
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()

print(get_weather_results("95129", "f05bdba02d87d4b7e9f45fd1601e9460"))

if __name__ == '__main__':
    app.run() 


