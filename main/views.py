from django.shortcuts import render

from .models import Partner


def index(request):

    return render(request, 'index.html', {'partners': Partner.objects.all()})
