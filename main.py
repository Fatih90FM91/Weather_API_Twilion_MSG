
import requests

import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = '2c6afb17e1d2c433dbeaa0ea2990e88e'





#-ctd2Vf3snf1rcXGcI9mlclzlosr1-EE5oQEDGNr
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'YOUR_API_KEY'

weather_params = {
    'lat': 52.078880,
    'lon': 4.400310,
    'appid': api_key,
    'exclude':'current, minutely, daily'

}

response = requests.get(OWM_Endpoint, params=weather_params)

print(response.status_code)

weather_data = response.json()
weather_hourly_datas = weather_data['hourly'][:12]
# print(weather_hourly_datas)
# print(weather_data['hourly'][0]['weather'])

is_situation = False
for hourly_data in weather_hourly_datas:
    data = hourly_data['weather'][0]['id']
    print(hourly_data['weather'][0]['id'])
    if int(data) < 700:
        is_situation = True
        print('Please bring your umbrella beside you..!!')

print(is_situation)
if is_situation:
    print('Please bring your umbrella beside you..!!')
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                         body="It's going to rain Today.Please Bring your umbrella beside you..!! ☂️",
                         from_='+14092544142',
                         to='+31683502720'
                     )
    print(message.status)
