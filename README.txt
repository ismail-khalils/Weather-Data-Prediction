Weather Data Analysis

This program collects and analyzes weather data for Woodbridge, VA on July 4th over the past five years.
It uses the WeatherAPI to get the data, calculates various statistics, and stores the data in a SQLite
database using SQLAlchemy ORM. The database and table are created and queried in the sqlitedatabase.py script.
The program also includes unit tests for the methods in the WeatherAPI.

Please note that in the program, weather variables are abbreviated and do not explicitly mention ‘5 years’ in their
names. However, when you come across a variable like average_wind_speed, it’s actually referring to the average
wind speed over the past 5 years.

Running the Program

Run the main.py script to collect the weather data and calculate the statistics.
This script also creates an instance of the WeatherData class using the variables defined in the file.
Run the sqlitedatabase.py script to create the database, table, add the weather data to the table, and run the query.
The output of this script is a list printed to the console.
Run the test.py script to run the unit tests for the WeatherAPI. This script outputs the results of three unit tests.

Dependencies
All the dependencies needed to run the program successfully are listed in the requirements.txt file.
Make sure to install them before running the program.
