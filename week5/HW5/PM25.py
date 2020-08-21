# https://rapidapi.com/airmine-ai-aqi/api/pm251/details

import http.client
import json

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

# µg / m3 

# print( data_dict['meta']['dateIssued'] )
# print( data_dict['location'] )
# print( data_dict['forecasts'] )

count = 0

reg_date = 'None'

for i in range(len(data_dict['forecasts'])):
    # print( data_dict['forecasts'][i] )
    # if '2020-08-19' in str(data_dict['forecasts'][i]):
    #     print( data_dict['forecasts'][i] )

    #     count += 1

    date = data_dict['forecasts'][i]['date']
    date = date.split('T')

    # if reg_date != date[0]:
    #     reg_date = date[0]
    #     print( date[0] )

# print( count )

hour = [(data_dict['forecasts'][i]['date'].split('T'))[1][:5] for i in range(6)]
values = [(data_dict['forecasts'][i]['values'][0]['value']) for i in range(6)]

print(hour)
print(values)