from tech_skills.models import OtherTechSkills, TechSkills
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
    order = ['expert','advance','upper intermediate', 'intermediate', 'lower intermediate','basic' ]
    tech_skills = sorted(tech_skills, key=lambda x: order.index(x.quality))

    # tech_skills records
    other_skills = OtherTechSkills.objects.all()

    context = {
        'person_info': person_info,
        'tech_skills': tech_skills,
        'other_skills': other_skills,
    }
    return render(request, 'pages/about.html', context)
