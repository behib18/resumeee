from contact.models import Contact
from django.shortcuts import render
from person_information.models import PersonInfo
from .forms import NewContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    # person_info record
    person_info = PersonInfo.objects.get()
    # Contact record
    contact = Contact.objects.get()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # user_form = form.save(commit = False)
            form.save()
            messages.success(request, 'The Message was sent successfully')
            # redirect to a new URL:
            # return redirect(request, 'contact/index.html')
            return HttpResponseRedirect('/contact/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewContactForm()

    context = {
        'person_info': person_info,
        'form': form,
        'contact': contact,
    }
    return render(request, 'contact/index.html', context)
