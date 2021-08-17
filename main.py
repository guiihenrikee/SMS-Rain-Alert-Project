import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
apy_key = os.environ.get("OWM_KEY")
account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_ACC_TOKEN")

parameters = {
    "lat": -23.312180,  # Change to your location
    "lon": -51.161530,  # Change to your location
    "exclude": "current,minutely,daily,alerts",
    "appid": apy_key
}
request = requests.get(OWM_Endpoint, params=parameters)
request.raise_for_status()
data = request.json()
i = 0
will_rain = False
while i < 12:
    for weather in (data["hourly"][i]["weather"]):
        if int(weather["id"]) < 700:
            will_rain = True
        i += 1
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring an umbrella.",
                         from_="API_PHONE",  # CHANGE THIS
                         to="YOUR_PHONE"  # CHANGE THIS
                    )
    print(message.status)
