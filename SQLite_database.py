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

