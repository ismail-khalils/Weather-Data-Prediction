from weather_data import WeatherData
from WeatherAPI import WeatherAPI

# Calculating the rest of the parameters for WeatherData using built-in python functions
weather_api = WeatherAPI()
temperatures = weather_api.get_mean_temp()
wind = weather_api.get_max_wind_speed()
precipitation = weather_api.get_precipitation_sum()

average_temp = sum(temperatures) / len(temperatures)
min_temp = min(temperatures)
max_temp = max(temperatures)

average_wind = sum(wind) / len(wind)
min_wind = min(wind)
max_wind = max(wind)

average_precipitation = sum(precipitation) / len(precipitation)
min_precipitation = min(precipitation)
max_precipitation = max(precipitation)

# Creating an instance of the WeatherData class using the variables I created above

weather_data = WeatherData(
    location_latitude=38.658707,
    location_longitude=-77.257919,
    month=7,
    day_of_month=4,
    year=2023,
    avg_temp=average_temp,
    min_temp=min_temp,
    max_temp=max_temp,
    avg_wind_speed=average_wind,
    min_wind_speed=min_wind,
    max_wind_speed=max_wind,
    sum_precipitation=average_precipitation,
    min_precipitation=min_precipitation,
    max_precipitation=max_precipitation
)

