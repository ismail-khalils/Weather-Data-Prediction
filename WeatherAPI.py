import requests
import json
from datetime import datetime, timedelta

# Creating the WeatherAPI class and including a method to get the data for the past five years on my chose date


class WeatherAPI:
    def __init__(self):
        self.api = ('https://archive-api.open-meteo.com/v1/archive?latitude=38.658707&'
                    'longitude=-77.257919&start_date=2018-07-04&end_date=2023-07-04&'
                    'daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&'
                    'ind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York')

    def get_mean_temps(self, past_data):
        mean_temps = [day['daily']['temperature_2m_mean'][0] for day in past_data]
        return mean_temps

    def get_max_wind_speeds(self, past_data):
        max_wind_speeds = [day['daily']['wind_speed_10m_max'][0] for day in past_data]
        return max_wind_speeds

    def get_precipitation_sums(self, past_data):
        precipitation_sums = [day['daily']['precipitation_sum'][0] for day in past_data]
        return precipitation_sums

    def get_past_five_years_data(self):
        past_data = []
        for i in range(1, 6):
            past_date = (datetime.strptime('2023-07-04', "%Y-%m-%d") - timedelta(days=i * 365)).strftime("%Y-%m-%d")
            api = (('https://archive-api.open-meteo.com/v1/archive?latitude=38.658707'
                   '&longitude=-77.257919&start_date=') + past_date + '&end_date=' + past_date +
                   ('&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&'
                    'temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
                    '&timezone=America%2FNew_York'))
            response = requests.get(api)
            past_data.append(json.loads(response.text))
        return past_data

