
import requests

def get_weather_forecasts(location, api_key):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    querystring = {"location": location, "format": "json", "u": "c"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        forecasts = data.get('forecasts', [])
        forecast_list = []

        for forecast in forecasts:
            day = forecast.get('day')
            high = forecast.get('high')
            low = forecast.get('low')
            text = forecast.get('text')
            forecast_list.append({'day': day, 'high': high, 'low': low, 'text': text})

        return forecast_list
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code}")