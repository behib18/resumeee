from django.shortcuts import render
from person_information.models import PersonInfo
from .forms import ContactForm

def index(request):
    # person_info record
    person_info = PersonInfo.objects.get()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            pass

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    context = {
        'person_info': person_info,
        'form': form,
    }
    return render(request, 'contact/index.html', context)
