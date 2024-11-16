import requests

api_key = '3e8b535b08151cfd065f048c3526b0ef'

user_input = input("enter city: ")

weather_data = requests.get(
    f"https://api.openweatherapp.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.status_code)
