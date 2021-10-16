from summary.models import Summary
from background_info.models import Background
from django.shortcuts import render
from person_information.models import PersonInfo
from education.models import Education


def index(request):
    # background_info record
    background_info = Background.objects.get()
    # person_info record
    person_info = PersonInfo.objects.get()
    # summary record
    summary = Summary.objects.get()
    # educations record
    educations = Education.objects.all()

    context = {
        'background_info': background_info,
        'person_info': person_info,
        'summary': summary,
        'educations': educations,
    }
    return render(request, 'background_info/index.html', context)
