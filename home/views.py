from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def health_benefits(request):
    """ A view to return the health and benefits page """

    return render(request, 'home/health_benefits.html')
