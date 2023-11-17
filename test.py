import unittest
from WeatherAPI import WeatherAPI

# Creating 3 unit test cases, one for each method


class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.api = WeatherAPI()

    def test_get_mean_temps(self):
        past_data = self.api.get_past_five_years_data()
        result = self.api.get_mean_temps(past_data)
        self.assertIsInstance(result, list)

    def test_get_max_wind_speeds(self):
        past_data = self.api.get_past_five_years_data()
        result = self.api.get_max_wind_speeds(past_data)
        self.assertIsInstance(result, list)

    def test_get_precipitation_sums(self):
        past_data = self.api.get_past_five_years_data()
        result = self.api.get_precipitation_sums(past_data)
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
