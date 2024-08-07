import base64

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from WebHistory.models import Event, DirectionLines, SideBoundaries

def first_page_start(request):
    return render(request, 'firstpage.html')

def choise_event_page(request):
    list_event = Event.objects.all().order_by('id')
    for event in list_event:
        event.path_img_map = f"data:image/svg+xml;base64,{bytes(event.path_img_map).decode()}"
        event.path_img = f"data:image/svg+xml;base64,{bytes(event.path_img).decode()}"
    return render(request, 'mainpage.html', context={"list_event": list_event})

def event_page(request, name_event):
    current_event = Event.objects.get(name_event=name_event.replace("_", " "))
    event_map = f"data:image/svg+xml;base64,{bytes(current_event.path_img_map).decode()}"
    list_direction_lines = DirectionLines.objects.filter(event=current_event.id)
    for line in list_direction_lines:
        line.path_img_line = f"data:image/svg+xml;base64,{bytes(line.path_img_line).decode()}"

    list_side_boundaries = SideBoundaries.objects.filter(event=current_event.id)
    for boundaries in list_side_boundaries:
        boundaries.path_img_boundaries = f"data:image/svg+xml;base64,{bytes( boundaries.path_img_boundaries).decode()}"
    return render(request, 'map_page.html', context={'name_event': name_event,
                                                     'list_direction_lines': list_direction_lines,
                                                     'event_map': event_map,
                                                     'list_side_boundaries': list_side_boundaries})

