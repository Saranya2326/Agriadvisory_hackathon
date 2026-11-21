import requests
from datetime import datetime, timezone


API_URL = "https://api.dharun.dev/v1/mandi"


def get_prices(commodity="", district=""):

    params = {"limit": 100}

    if commodity:
        params["commodity"] = commodity.strip()

    if district:
        params["district"] = district.strip()

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=20
        )

        print("API STATUS:", response.status_code)

        response.raise_for_status()

        result = response.json()

        print("API DATA:", result)

        if isinstance(result, list):
            prices = result

        elif isinstance(result, dict):
            prices = result.get("data", [])

            if not prices:
                prices = result.get("records", [])

        else:
            prices = []

        return {
            "success": True,
            "commodity": commodity or "All commodities",
            "district": district or "All India",
            "prices": prices,
            "total_records": len(prices),
            "message": (
                "Mandi prices fetched successfully."
                if prices
                else "API responded, but no price records were returned."
            ),
            "source": API_URL,
            "updated_at": datetime.now(timezone.utc).isoformat()
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "prices": [],
            "message": "API request timed out."
        }

    except requests.exceptions.RequestException as e:
        print("API ERROR:", str(e))

        return {
            "success": False,
            "prices": [],
            "message": "Unable to connect to Mandi API.",
            "error": str(e)
        }

    except ValueError as e:
        return {
            "success": False,
            "prices": [],
            "message": "Invalid JSON response from API.",
            "error": str(e)
        }