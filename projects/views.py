from projects.models import Photo, Project
from person_information.models import PersonInfo
from django.shortcuts import get_object_or_404, render


def index(request):
    # projects records
    projects = Project.objects.all()

    # person_info record
    person_info = PersonInfo.objects.get()

    context = {
        'projects': projects,
        'person_info': person_info,
    }
    return render(request, 'projects/index.html', context)


def project(request, project_id):
    # projects records
    project = get_object_or_404(Project, pk=project_id)

    # person_info record
    person_info = PersonInfo.objects.get()

    # image records
    images = Photo.objects.filter(project__pk=project_id)

    context = {
        'project': project,
        'person_info': person_info,
        'images': images,
    }
    return render(request, 'projects/project.html', context)
