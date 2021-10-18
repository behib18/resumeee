from projects.models import Project
from django.shortcuts import render

def index(request):
    # projects records
    projects = Project.objects.all()

    context =  {
        'projects': projects,
    }
    return render(request, 'projects/index.html', context)
