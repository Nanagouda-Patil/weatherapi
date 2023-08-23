from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)
    return render_template("index.html", weather_data=weather_data)

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    app.run(debug=True)
