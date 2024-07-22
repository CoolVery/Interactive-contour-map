from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from WebHistory.models import Event, DirectionLines, SideBoundaries


def first_page_start(request):
    return render(request, 'firstpage.html')


def choise_event_page(request):
    list_event = Event.objects.all().order_by('id')
    return render(request, 'mainpage.html', context={"list_event": list_event})

def event_page(request, name_event):
    current_event = Event.objects.get(name_event=name_event.replace("_", " "))
    list_direction_lines = DirectionLines.objects.filter(event=current_event.id)
    list_side_boundaries = SideBoundaries.objects.filter(event=current_event.id)
    return render(request, 'map_page.html', context={'name_event': name_event,
                                                     'list_direction_lines': list_direction_lines,
                                                     'event_map': current_event.path_img_map,
                                                     'list_side_boundaries': list_side_boundaries})