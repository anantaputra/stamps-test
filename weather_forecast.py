import json
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen
from datetime import datetime

API_KEY = "5cdd4a52b1df0367a9a1ba57bc156392"
CITY = "Jakarta,ID"
UNITS = "metric"
DAYS = 5


def fetch_forecast():
    url = "https://api.openweathermap.org/data/2.5/forecast?" + urlencode(
        {"q": CITY, "appid": API_KEY, "units": UNITS}
    )
    with urlopen(url, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def pick_one_temp_per_day(data):
    chosen = {}
    ordered_days = []

    today = datetime.now().date()

    for item in data.get("list", []):
        dt_txt = item.get("dt_txt")
        temp = item.get("main", {}).get("temp")
        if not dt_txt or temp is None:
            continue

        date_str, time_str = dt_txt.split()
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        if date_obj < today:
            continue

        if date_str not in chosen:
            chosen[date_str] = (time_str, float(temp))
            ordered_days.append(date_str)
        elif time_str == "12:00:00" and chosen[date_str][0] != "12:00:00":
            chosen[date_str] = (time_str, float(temp))

    result = []
    for date_str in ordered_days[:DAYS]:
        result.append((date_str, chosen[date_str][1]))
    return result


def format_day(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%a, %d %b %Y")


def unit_suffix():
    if UNITS == "metric":
        return "°C"
    if UNITS == "imperial":
        return "°F"
    return "K"


def main():

    try:
        data = fetch_forecast()
    except Exception:
        print("Could not fetch weather data.")
        return

    if str(data.get("cod")) != "200":
        print(data.get("message", "API error"))
        return

    forecast = pick_one_temp_per_day(data)

    print("Weather Forecast:")
    suffix = unit_suffix()
    for date_str, temp in forecast:
        print(f"{format_day(date_str)}: {temp:.2f}{suffix}")


if __name__ == "__main__":
    main()
