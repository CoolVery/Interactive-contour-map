from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from WebHistory.models import Event


def first_page_start(request):
    return render(request, 'firstpage.html')


def choise_event_page(request):
    list_event = Event.objects.all()
    for event in list_event:
        event.name_event = event.name_event.upper()
        event.save()
    print(list_event)
    return render(request, 'mainpage.html', context={"list_event": list_event})
