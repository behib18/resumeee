from background_info.models import Background
from django.shortcuts import render
from person_information.models import PersonInfo


def index(request):
    background_info = Background.objects.get()
    # person_info record
    person_info = PersonInfo.objects.get()
    context = {
        'background_info': background_info,
        'person_info': person_info,
    }
    return render(request, 'background_info/index.html', context)
