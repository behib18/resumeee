from contact.models import Contact
from django.shortcuts import render
from person_information.models import PersonInfo
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    # person_info record
    person_info = PersonInfo.objects.last()
    # Contact record
    contact = Contact.objects.last()



    context = {
        'person_info': person_info,
        'contact': contact,
    }
    return render(request, 'contact/index.html', context)
