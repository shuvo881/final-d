from django.urls import path
from .views import dashboard_view

pathpattern = [
    path('', dashboard_view, name='dashboard_view')
]