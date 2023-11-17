from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from main import (mean_temps, min_temperature, max_temperature, average_wind_speed, min_wind_speed, max_wind_speeds,
precipitation_sums, min_precipitation, max_precipitation)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from WeatherAPI import WeatherAPI

Base = declarative_base()

# Creating second class in SQLite that uses the SQLAlchemy ORM module
class WeatherTable(Base):
    __tablename__ = 'weathertable'
    primary_key = Column(Integer, primary_key=True, autoincrement= True)
    location_latitude = Column(Float, nullable=False)
    location_longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day_of_month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    avg_temp = Column(Float, nullable=False)
    min_temp = Column(Float, nullable=False)
    max_temp = Column(Float, nullable=False)
    avg_wind_speed = Column(Float, nullable=False)
    min_wind_speed = Column(Float, nullable=False)
    max_wind_speed = Column(Float, nullable=False)
    sum_precipitation = Column(Float, nullable=False)
    min_precipitation = Column(Float, nullable=False)
    max_precipitation = Column(Float, nullable=False)

    def __repr__(self):
        return (f"<WeatherTable(location_latitude={self.location_latitude}, location_longitude={self.location_longitude},"
                f" month={self.month}, day_of_month={self.day_of_month}, year={self.year}, avg_temp={self.avg_temp}, "
                f"min_temp={self.min_temp}, max_temp={self.max_temp}, avg_wind_speed={self.avg_wind_speed}, "
                f"min_wind_speed={self.min_wind_speed}, max_wind_speed={self.max_wind_speed}, "
                f"sum_precipitation={self.sum_precipitation}, min_precipitation={self.min_precipitation}, "
                f"max_precipitation={self.max_precipitation})>")

engine = create_engine('sqlite:///weather_data.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Creating function to query table
def query_weather_data():
    # Create a new session
    session = Session()

    # Query the WeatherTable
    weather_data = session.query(WeatherTable).all()

    # Close the session
    session.close()

    return weather_data

# Create a new session
session = Session()

# Create a new WeatherTable object
weather = WeatherTable(
    location_latitude=38.658707,
    location_longitude=-77.257919,
    month=7,
    day_of_month=4,
    year=2023,
    avg_temp=sum(mean_temps) / len(mean_temps),
    min_temp=min_temperature,
    max_temp=max_temperature,
    avg_wind_speed=average_wind_speed,
    min_wind_speed=min_wind_speed,
    max_wind_speed=max(max_wind_speeds),
    sum_precipitation=sum(precipitation_sums),
    min_precipitation=min_precipitation,
    max_precipitation=max_precipitation
)

# Check if an entry with the same data already exists
existing_entry = session.query(WeatherTable).filter_by(
    location_latitude=weather.location_latitude,
    location_longitude=weather.location_longitude,
    month=weather.month,
    day_of_month=weather.day_of_month,
    year=weather.year
).first()

# If no such entry exists, add the new object to the session
if existing_entry is None:
    session.add(weather)
    session.commit()

print(query_weather_data())
