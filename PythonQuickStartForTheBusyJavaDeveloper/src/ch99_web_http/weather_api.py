import requests

# https://openweathermap.org/api
# https://home.openweathermap.org/users/sign_in
api_key = "74e5520ecf1361c1de73decb5cc4a9c9"
city = input("Bitte geben Sie den Städtenamen für die Wetterabfrage ein: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

data = requests.get(url).json()
print(data)


def print_info(data, unit):
    temp = data["main"]["temp"]
    print("Temperatur in", unit, temp)
    humidity = data["main"]["humidity"]
    print("Feuchtigkeit:", humidity)


print_info(data, "°K:")

#For temperature in Fahrenheit use units=imperial
#For temperature in Celsius use units=metric

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

data = requests.get(url).json()
print_info(data, "°C:")