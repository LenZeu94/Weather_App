from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import config

api_key = config.api_key
app = Flask(__name__)
app.config["DEBUG"]=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)


class city(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable = False) 

db.create_all()



@app.route('/')
def index():
    city = 'Berlin'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    r = requests.get(url).json()

    weather = {
        'city': city,
        'temp': "{:.2f}".format(r['main']['temp']-273.15),
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
        }

    return render_template('weather.html', weather=weather)



if __name__ == '__main__':
    app.run(debug=True)









