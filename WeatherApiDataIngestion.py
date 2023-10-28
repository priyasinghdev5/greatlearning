from pyowm import OWM
import json
import boto3
import datetime

kinesis = boto3.client('kinesis', region_name="us-east-1")

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=2)


def get_weather_api_data(latitude, longitude):
    owm = OWM('0f8b321c68552dff33eeb5625f971c39')
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=latitude, lon=longitude)
    current_data = json.dumps(one_call.current.__dict__)
    #info = current_data.info
    #print(f"Weather Data for given lat and long: {info}")
    print(f"Weather Data for given lat and long: {current_data}")
