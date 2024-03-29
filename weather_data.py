# Creating the WeatherData class that will be used to hold the Weather API data
class WeatherData:
    def __init__(self, location_latitude, location_longitude, month, day_of_month, year, avg_temp, min_temp,
                 max_temp, avg_wind_speed, min_wind_speed, max_wind_speed, sum_precipitation, min_precipitation,
                 max_precipitation):
        self.location_latitude = location_latitude,
        self.location_longitude = location_longitude,
        self.month = month,
        self.day_of_month = day_of_month,
        self.year = year,
        self.avg_temp = avg_temp,
        self.min_temp = min_temp,
        self.max_temp = max_temp,
        self.avg_wind_speed = avg_wind_speed,
        self.min_wind_speed = min_wind_speed,
        self.max_wind_speed = max_wind_speed,
        self.sum_precipitation = sum_precipitation,
        self.min_precipitation = min_precipitation,
        self.max_precipitation = max_precipitation

    def __repr__(self):
        return (f"<WeatherTable(location_latitude={self.location_latitude}, location_longitude={self.location_longitude},"
                f" month={self.month}, day_of_month={self.day_of_month}, year={self.year}, avg_temp={self.avg_temp}, "
                f"min_temp={self.min_temp}, max_temp={self.max_temp}, avg_wind_speed={self.avg_wind_speed}, "
                f"min_wind_speed={self.min_wind_speed}, max_wind_speed={self.max_wind_speed}, "
                f"sum_precipitation={self.sum_precipitation}, min_precipitation={self.min_precipitation}, "
                f"max_precipitation={self.max_precipitation})>")