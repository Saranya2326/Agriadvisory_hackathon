import requests
from datetime import datetime

def get_weather(district):
    if not district:
        return {
            "summary": "Please provide a district name.",
            "source": "Open-Meteo"
        }

    try:
        # Find district coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_response = requests.get(
            geo_url,
            params={
                "name": district,
                "count": 1,
                "language": "en",
                "format": "json",
                "countryCode": "IN"
            },
            timeout=15
        )
        geo_response.raise_for_status()
        locations = geo_response.json().get("results", [])

        if not locations:
            return {
                "summary": f"Location not found: {district}",
                "source": "Open-Meteo"
            }

        location = locations[0]

        # Get live weather and forecast
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_response = requests.get(
            weather_url,
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": (
                    "temperature_2m,relative_humidity_2m,"
                    "precipitation,weather_code,wind_speed_10m"
                ),
                "daily": (
                    "temperature_2m_max,temperature_2m_min,"
                    "precipitation_probability_max"
                ),
                "timezone": "Asia/Kolkata",
                "forecast_days": 3
            },
            timeout=15
        )
        weather_response.raise_for_status()
        data = weather_response.json()

        current = data["current"]
        daily = data["daily"]

        return {
            "district": location["name"],
            "temperature_c": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "precipitation_mm": current["precipitation"],
            "wind_speed_kmh": current["wind_speed_10m"],
            "weather_code": current["weather_code"],
            "forecast": {
                "dates": daily["time"],
                "max_temperature": daily["temperature_2m_max"],
                "min_temperature": daily["temperature_2m_min"],
                "rain_probability": daily["precipitation_probability_max"]
            },
            "summary": (
                f"Temperature: {current['temperature_2m']}°C | "
                f"Humidity: {current['relative_humidity_2m']}% | "
                f"Rain: {current['precipitation']} mm | "
                f"Wind: {current['wind_speed_10m']} km/h"
            ),
            "source": "Open-Meteo",
            "updated_at": current["time"]
        }

    except requests.RequestException as e:
        return {
            "summary": "Unable to fetch weather data. Please try again.",
            "source": "Open-Meteo",
            "error": str(e)
        }
    except (KeyError, IndexError, ValueError):
        return {
            "summary": "Weather data format could not be read.",
            "source": "Open-Meteo"
        }