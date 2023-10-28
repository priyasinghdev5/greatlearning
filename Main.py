import WeatherApiDataIngestion as weatherApiDataIngestion
from datetime import datetime

latitude = 28.5355
longitude = 77.3910
weatherApiDataIngestion.get_weather_api_data(latitude, longitude)
