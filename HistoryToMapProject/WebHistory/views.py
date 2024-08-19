import base64

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from WebHistory.APIRequests.requests import get_events, get_info_events, get_event_areas
from WebHistory.models import Event, DirectionLines, SideBoundaries


def first_page_start(request):
    return render(request, 'firstpage.html')

def choise_event_page(request):
    list_event = get_events()
    for event in list_event:
        event['path_img_map'] = f"data:image/svg+xml;base64,{event['path_img_map']}"
        event['path_img'] = f"data:image/svg+xml;base64,{event['path_img']}"
    return render(request, 'mainpage.html', context={"list_event": list_event})

def event_page(request, name_event):
    current_event = get_info_events(name_event, "http://127.0.0.1:8001/event_operathion/event/")
    event_map = f"data:image/svg+xml;base64,{current_event['path_img_map']}"
    list_direction_lines = get_info_events(name_event, "http://127.0.0.1:8001/event_operathion/line/")
    for line in list_direction_lines:
        line['path_img_line'] = f"data:image/svg+xml;base64,{line['path_img_line']}"

    list_side_boundaries = get_info_events(name_event, "http://127.0.0.1:8001/event_operathion/boundaries/")
    for boundaries in list_side_boundaries:
        boundaries['path_img_boundaries'] = f"data:image/svg+xml;base64,{boundaries['path_img_boundaries']}"

    list_event_area = get_event_areas(name_event)
    return render(request, 'map_page.html', context={'name_event': name_event,
                                                     'list_direction_lines': list_direction_lines,
                                                     'event_map': event_map,
                                                     'list_side_boundaries': list_side_boundaries,
                                                     'list_event_area': list_event_area})

