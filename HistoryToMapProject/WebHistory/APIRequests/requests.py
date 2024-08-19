import requests

def get_events():
    url = "http://127.0.0.1:8001/event_operathion/events/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
def get_info_events(name_event, url):
    url = url
    params = {
        "name_event": name_event.replace("_", " ")
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
def get_event_areas(name_event):
    url = "http://127.0.0.1:8001/event_area_operathion/"
    params = {
        "name_event": name_event.replace("_", " ")
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()