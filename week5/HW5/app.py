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

timeZone = data_dict['location']['timeZone']
date = ((data_dict['forecasts'][0]['date']).split('T'))[0]
time = ((data_dict['forecasts'][0]['date']).split('T'))[1][:5]
pm25 = (data_dict['forecasts'][0]['values'][0]['value'])
data = [date, time, timeZone, pm25]

date_set = [((data_dict['forecasts'][i]['date']).split('T'))[0] for i in range(len(data_dict['forecasts']))]
date_set = list(dict.fromkeys(date_set))
data_val = 0
count = 0
pm25_avg = []

for x in date_set:
    for y in data_dict['forecasts']:
        if x in y['date']:
            data_val += y['values'][0]['value']
            count += 1
    data_val = round(data_val / count, 2)
    if data_val < 25:
        pm25_avg.append([0, x, data_val])
    elif data_val < 37:
        pm25_avg.append([1, x, data_val])
    elif data_val < 50:
        pm25_avg.append([2, x, data_val])
    elif data_val < 90:
        pm25_avg.append([3, x, data_val])
    else:
        pm25_avg.append([4, x, data_val])
    data_val = 0
    count = 0

@app.route('/')
def index():
    return render_template('index.html', hour=hour, values=values, data=data, pm25_avg=pm25_avg)

if __name__ == "__main__":
    app.run(debug=True)