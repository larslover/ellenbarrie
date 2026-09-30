from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('farming/', views.farming, name='farming'),
    path('children/', views.children, name='children'),
    path(
    'service-worker.js',
    views.service_worker,
    name='service_worker'
),
path("school/", views.school, name="school"),
]