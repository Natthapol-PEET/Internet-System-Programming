from flask import Flask, render_template
import http.client
import json

app = Flask(__name__)

conn = http.client.HTTPSConnection("pm251.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "pm251.p.rapidapi.com",
    'x-rapidapi-key': "6f73945e84mshb3e8648c84bbe99p169009jsne326a686053e"
    }

conn.request("GET", "/aqi?lat=13.72&lon=100.63", headers=headers)

res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")
data_dict = json.loads(data)
data_formatted_str = json.dumps(data_dict, indent=2)

hour = [(data_dict['forecasts'][i+1]['date'].split('T'))[1][:5] for i in range(6)]
values = [(data_dict['forecasts'][i+1]['values'][0]['value']) for i in range(6)]

@app.route('/')
def index():
    return render_template('index.html', hour=hour, values=values)

if __name__ == "__main__":
    app.run(debug=True)