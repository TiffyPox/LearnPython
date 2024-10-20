from msvcrt import getch
import datetime as dt
import requests

def main():
    print("")

baseURL = "https://api.weatherapi.com/v1/current.json?"
apiKEY = ""
cityName = "Wrexham"

url = baseURL + "key=" + apiKEY + "&q=" + cityName

response = requests.get(url)

if response.status_code == 200:
    weatherData = response.json()  # Call .json() method here
    print(weatherData)
else:
    print(f"Error: {response.status_code} - {response.text}")

# format values
tempCelsius = weatherData['current']['temp_c']
tempFahrenheit = weatherData['current']['temp_f']

# hold Alt + 0176 to get the degree symbol
print(f"Celsius temperature in {cityName}: {tempCelsius:}°C")
print(f"Fahrenheit temperature in {cityName}: {tempFahrenheit:}°F")

if __name__ == "__main__":
    main()
