import requests
import json

#Creating the WeatherAPI class to get the data from the weather api on my specified day and five years before
class WeatherAPI:
    def __init__(self):
        self.api = 'https://archive-api.open-meteo.com/v1/archive?latitude=38.658707&longitude=-77.257919&start_date=2018-07-04&end_date=2023-07-04&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York'
        response = requests.get(self.api)
        self.data = json.loads(response.text)

    def get_mean_temp(self):
        mean_temp = self.data['daily']['temperature_2m_mean']
        return mean_temp

    def get_max_wind_speed(self):
        max_wind_speed = self.data['daily']['wind_speed_10m_max']
        return max_wind_speed

    def get_precipitation_sum(self):
        precipitation_sum = self.data['daily']['precipitation_sum']
        return precipitation_sum

