from weather_data import WeatherData
from WeatherAPI import WeatherAPI

# Getting the past 5 years data
data = WeatherAPI()
past_data = data.get_past_five_years_data()

# Extract the temperature, wind speed, and precipitation data
temperatures = [day['daily']['temperature_2m_mean'][0] for day in past_data]
wind_speeds = [day['daily']['wind_speed_10m_max'][0] for day in past_data]
precipitations = [day['daily']['precipitation_sum'][0] for day in past_data]

# Calculate the five-year averages
mean_temps = data.get_mean_temps(past_data)
average_wind_speed = sum(wind_speeds) / len(wind_speeds)
precipitation_sums = data.get_precipitation_sums(past_data)

# Find the five-year minimums
min_temperature = min(temperatures)
min_wind_speed = min(wind_speeds)
min_precipitation = min(precipitations)

# Find the five-year maximums
max_temperature = max(temperatures)
max_wind_speeds = data.get_max_wind_speeds(past_data)
max_precipitation = max(precipitations)

# Creating an instance of the WeatherData class using the variables I created above

weather_data = WeatherData(
    location_latitude=38.658707,
    location_longitude=-77.257919,
    month=7,
    day_of_month=4,
    year=2023,
    avg_temp=mean_temps,
    min_temp=min_temperature,
    max_temp=max_temperature,
    avg_wind_speed=average_wind_speed,
    min_wind_speed=min_wind_speed,
    max_wind_speed=max_wind_speeds,
    sum_precipitation=precipitation_sums,
    min_precipitation=min_precipitation,
    max_precipitation=max_precipitation
)
