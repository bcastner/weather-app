import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        wind = weather_data["wind"]
        weather_desc = weather_data["weather"][0]["description"]

        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]

        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {temperature} degrees Celsius:")
        print(f"Weather: {weather_desc}:")
        print(f"Humidity: {humidity}%:")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"City {city.capitalize()} not found.")


def main_menu():
    api_key = "17b6a8f97d0d8781ed24d72e64ca1330"
    city = input("Enter city name: ")
    get_weather(api_key, city)


main_menu()
