from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from .models import (
    HeroSection,
    HistoryEntry,
    FarmingHero,
    FarmingUpdate,
    Child
)


def home(request):
    hero = HeroSection.objects.filter(
        is_active=True
    ).first()

    return render(
        request,
        'core/home.html',
        {
            'hero': hero,
        }
    )


def history(request):
    entries = HistoryEntry.objects.all()

    return render(
        request,
        'core/history.html',
        {
            'entries': entries,
        }
    )


def farming(request):
    hero = FarmingHero.objects.filter(
        is_active=True
    ).first()

    updates = FarmingUpdate.objects.filter(
        is_active=True
    )

    return render(
        request,
        'core/farming.html',
        {
            'hero': hero,
            'updates': updates,
        }
    )
def children(request):
    children = Child.objects.filter(
        is_active=True
    )

    return render(
        request,
        'core/children.html',
        {
            'children': children,
        }
    )


def service_worker(request):

    sw = finders.find('service-worker.js')

    with open(sw, 'r') as file:
        content = file.read()

    return HttpResponse(
        content,
        content_type='application/javascript'
    )