from msvcrt import getch
#import datetime as dt
import requests
import pandas as pd

def main():
    print("")

baseURL = "https://api.weatherapi.com/v1/current.json?"

# enter personal API key:
apiKEY = ""

# enter chosen city name:
cityName = "Wrexham"

url = baseURL + "key=" + apiKEY + "&q=" + cityName

response = requests.get(url)

if response.status_code == 200:
    weatherData = response.json()  # Call .json() method here
    print(weatherData)
else:
    print(f"Error: {response.status_code} - {response.text}")

# Format values
tempCelsius = weatherData['current']['temp_c']
tempFahrenheit = weatherData['current']['temp_f']

# hold Alt + 0176 to get the degree symbol
print(f"Celsius temperature in {cityName}: {tempCelsius:}°C")
print(f"Fahrenheit temperature in {cityName}: {tempFahrenheit:}°F")

# List of cities we want to collect the data of
cities = ["London", "Birmingham", "Glasgow", "Liverpool", "Bristol", "Manchester", "Sheffield", "Leeds", "Edinburgh", "Leicester"]

citiesList = []

# For each city, we access the data using the Weather API
for city in cities:
    # Final Url:
    finalUrl = baseURL + "key=" + apiKEY + "&q=" + city

    response = requests.get(finalUrl)

    if response.status_code == 200:
        cityData = response.json()  # Call .json() method here
        citiesList.append([cityData['location'], cityData['current']])
    else:
        print(f"Error: {response.status_code} - {response.text}")

dataset = pd.DataFrame(citiesList)
print(dataset.head())

if __name__ == "__main__":
    main()
