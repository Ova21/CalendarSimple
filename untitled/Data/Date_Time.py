import urllib.request
import json
from datetime import datetime  # Built-in, works offline!

def date():
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"]

    try:
        #Online
        data = json.loads(urllib.request.urlopen("https://timeapi.io/api/time/current/zone?timeZone=Europe/London", timeout=2).read())
        day_num = str(data["day"])
        month_num = str(data["month"])
        current_month_text = months[int(month_num) - 1]
        print("Fetched time ONLINE")
        return current_month_text, day_num

    except Exception:
        #Offline
        now = datetime.now()
        day_num = str(now.day)            # e.g., "14"
        current_month_text = months[now.month - 1]  # e.g., "JUNE"
        print("No Wi-Fi. Fetched time OFFLINE from PC")
        return current_month_text, day_num