from tech_skills.models import TechSkills
from django.shortcuts import render

from person_information.models import PersonInfo


def index(request):

    person_info = PersonInfo.objects.get()
    context = {
        'person_info': person_info
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # person_info record
    person_info = PersonInfo.objects.get()
    
    # tech_skills records
    tech_skills = TechSkills.objects.all()

    context = {
        'person_info': person_info,
        'tech_skills': tech_skills,
    }
    return render(request, 'pages/about.html', context)
