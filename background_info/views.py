from background_info.models import Background
import background_info
from django.shortcuts import render


def index(request):
    background_info = Background.objects.get()
    context = {
        'background_info': background_info,
    }
    return render(request, 'background_info/index.html', context)
