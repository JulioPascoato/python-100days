import requests
from twilio.rest import Client


MY_LAT = -23.489448
MY_LONG = -46.726063

api_key = "038362a26a2c8b946ebe0d68e7d5d96b"
account_sid = "AC39e5059fc9ec307342322ceaa4d16a4f"
auth_token = "b3fd52abd30569db1f0cfddb3485bc3e"



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

weathers = [weather_data["hourly"][number]["weather"][0]["id"] for number in range(0, 12)]

will_rain = False

for weather in weathers:
    if int(weather) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+13343397721',
        to='+5511989453584'
    )
    print(message.status)

