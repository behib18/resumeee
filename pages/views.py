from django.shortcuts import render
import datetime

from person_information.models import PersonInfo


def index(request):

    person_info = PersonInfo.objects.get()
    context = {
        'person_info': person_info
    }
    return render(request, 'pages/index.html', context)


def about(request):
    person_info = PersonInfo.objects.get()
    today = datetime.date.today().year
    print(type(today))
    print(type(person_info.birthday.year))
    age = today - person_info.birthday.year
    print(age)

    context = {
        'person_info': person_info,
        'age': age,
    }
    return render(request, 'pages/about.html', context)
