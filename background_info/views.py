from .models import Experience, Language, Licence, Summary, Education, Experience
from background_info.models import Background
from django.shortcuts import render
from person_information.models import PersonInfo


def index(request):
    # background_info record
    background_info = Background.objects.last()
    # person_info record
    person_info = PersonInfo.objects.last()
    # summary record
    summary = Summary.objects.last()
    # educations record
    educations = Education.objects.all().order_by('-id')

    # experiences record
    experiences = Experience.objects.all().order_by('-id')

    # Licence record
    licences = Licence.objects.all()

    # experiences record
    languages = Language.objects.all()

    context = {
        'background_info': background_info,
        'person_info': person_info,
        'summary': summary,
        'educations': educations,
        'experiences': experiences,
        'languages': languages,
        'licences': licences,
    }
    return render(request, 'background_info/index.html', context)
