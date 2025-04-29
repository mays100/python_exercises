import requests
import json
import os
from datetime import datetime, timedelta

# הגדרות גלובליות עבור מטמון בזיכרון
in_memory_cache = {}
CACHE_DURATION_MINUTES = 30
CACHE_FILE = 'weather_cache.json'

def fetch_weather_data(location, api_key):
    """
    אחזור נתוני מזג אוויר מ-OpenWeatherMap API.

    ארגומנטים:
        location (str): המיקום שעבורו נרצה לקבל נתוני מזג אוויר.
        api_key (str): מפתח ה-API שלך עבור OpenWeatherMap.

    החזרות:
        dict or None: מילון המכיל נתוני מזג אוויר, או None אם נכשלה האחזור.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        if data["cod"] != "404":
            weather_data = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": datetime.now().isoformat()
            }
            return weather_data
        else:
            print(f"שגיאה: לא נמצא מיקום {location}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"שגיאה באחזור נתוני מזג אוויר: {e}")
        return None

def perform_analysis(weather_data_list):
    """
    ביצוע ניתוח סטטיסטי על רשימת נתוני מזג אוויר.

    ארגומנטים:
        weather_data_list (list): רשימה של מילוני נתוני מזג אוויר.

    החזרות:
        dict or None: מילון המכיל את תוצאות הניתוח, או None אם הרשימה ריקה.
    """
    if not weather_data_list:
        return None

    temperatures = [data["temperature"] for data in weather_data_list]
    humidities = [data["humidity"] for data in weather_data_list]
    wind_speeds = [data["wind_speed"] for data in weather_data_list]

    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    avg_humidity = sum(humidities) / len(humidities)
    avg_wind_speed = sum(wind_speeds) / len(wind_speeds)

    analysis_results = {
        "average_temperature": avg_temp,
        "max_temperature": max_temp,
        "min_temperature": min_temp,
        "average_humidity": avg_humidity,
        "average_wind_speed": avg_wind_speed
    }
    return analysis_results

def display_results(analysis_results, location):
    """
    הצגת תוצאות הניתוח.

    ארגומנטים:
        analysis_results (dict): מילון המכיל את תוצאות הניתוח.
        location (str): המיקום שעבורו הוצגו התוצאות.
    """
    if analysis_results:
        print(f"\nתוצאות ניתוח מזג האוויר עבור {location}:")
        print(f"  טמפרטורה ממוצעת: {analysis_results['average_temperature']:.2f}°C")
        print(f"  טמפרטורה מקסימלית: {analysis_results['max_temperature']:.2f}°C")
        print(f"  טמפרטורה מינימלית: {analysis_results['min_temperature']:.2f}°C")
        print(f"  לחות ממוצעת: {analysis_results['average_humidity']:.2f}%")
        print(f"  מהירות רוח ממוצעת: {analysis_results['average_wind_speed']:.2f} מטר/שנייה")
    else:
        print(f"אין תוצאות ניתוח להצגה עבור {location}.")

def save_results(location, analysis_results, strategy='memory'):
    """
    שמירת תוצאות הניתוח באמצעות אסטרטגיות מטמון שונות.

    ארגומנטים:
        location (str): המיקום שעבורו נשמרות התוצאות.
        analysis_results (dict): מילון המכיל את תוצאות הניתוח.
        strategy (str): אסטרטגיית המטמון ('memory' או 'file').
    """
    if analysis_results:
        timestamp = datetime.now().isoformat()
        cached_data = {
            "timestamp": timestamp,
            "results": analysis_results
        }

        if strategy == 'memory':
            in_memory_cache[location.lower()] = cached_data
            print(f"התוצאות נשמרו במטמון הזיכרון עבור {location}.")
        elif strategy == 'file':
            try:
                if os.path.exists(CACHE_FILE):
                    with open(CACHE_FILE, 'r') as f:
                        try:
                            cache_data = json.load(f)
                        except json.JSONDecodeError:
                            cache_data = {}
                else:
                    cache_data = {}

                cache_data[location.lower()] = cached_data

                with open(CACHE_FILE, 'w') as f:
                    json.dump(cache_data, f, indent=4)
                print(f"התוצאות נשמרו בקובץ המטמון ({CACHE_FILE}) עבור {location}.")
            except IOError as e:
                print(f"שגיאה בשמירת מטמון הקובץ: {e}")
        else:
            print(f"אסטרטגיית מטמון לא חוקית: {strategy}")

def load_cached_results(location, strategy='memory'):
    """
    טעינת תוצאות מטמון עבור מיקום נתון.

    ארגומנטים:
        location (str): המיקום שעבורו נרצה לטעון תוצאות מהמטמון.
        strategy (str): אסטרטגיית המטמון ('memory' או 'file').

    החזרות:
        dict or None: מילון המכיל את תוצאות המטמון, או None אם אין נתונים במטמון
                      או שהנתונים ישנים מדי.
    """
    if strategy == 'memory':
        cached_data = in_memory_cache.get(location.lower())
    elif strategy == 'file':
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r') as f:
                    cache_data = json.load(f)
                    cached_data = cache_data.get(location.lower())
            except (IOError, json.JSONDecodeError) as e:
                print(f"שגיאה בטעינת מטמון הקובץ: {e}")
                return None
        else:
            return None
    else:
        print(f"אסטרטגיית מטמון לא חוקית: {strategy}")
        return None

    if cached_data:
        timestamp_str = cached_data.get("timestamp")
        if timestamp_str:
            cached_time = datetime.fromisoformat(timestamp_str)
            time_difference = datetime.now() - cached_time
            if time_difference <= timedelta(minutes=CACHE_DURATION_MINUTES):
                print(f"טוען תוצאות ממטמון ה-{strategy} עבור {location}.")
                return cached_data["results"]
            else:
                print(f"נתוני המטמון עבור {location} ישנים מדי ({int(time_difference.total_seconds() / 60)} דקות).")
                return None
        else:
            return None
    return None

if __name__ == "__main__":
    # **החלף את 'YOUR_API_KEY' במפתח ה-API שלך מ-OpenWeatherMap**
    API_KEY = "39ea867bde6d976126aee6308e591d50"

    location = input("הזן את המיקום שעבורו תרצה נתוני מזג אוויר: ")

    # ניסיון לטעון נתונים מהמטמון (קודם זיכרון, אחר כך קובץ)
    analysis_results = load_cached_results(location, strategy='memory')
    if analysis_results is None:
        analysis_results = load_cached_results(location, strategy='file')

    if analysis_results:
        display_results(analysis_results, location)
    else:
        print(f"מאחזר נתוני מזג אוויר חדשים עבור {location}...")
        weather_data = fetch_weather_data(location, API_KEY)

        if weather_data:
            # כדי להדגים "עיבוד נקודות נתונים מרובות", נעביר רשימה עם נקודת הנתונים הנוכחית.
            # ביישום מורכב יותר, ניתן היה לאחזר נתוני תחזית לכמה ימים ולהעביר אותם כאן.
            weather_data_list = [weather_data]
            analysis_results = perform_analysis(weather_data_list)

            if analysis_results:
                display_results(analysis_results, location)
                # שמירת התוצאות במטמון (גם זיכרון וגם קובץ)
                save_results(location, analysis_results, strategy='memory')
                save_results(location, analysis_results, strategy='file')
            else:
                print(f"לא ניתן היה לבצע ניתוח סטטיסטי עבור {location}.")
        else:
            print(f"לא ניתן היה לאחזר נתוני מזג אוויר עבור {location}.")

    print("\nהסתיימה התוכנית.")