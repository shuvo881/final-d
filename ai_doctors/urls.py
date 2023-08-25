from django.urls import path
from .views import ai_doctors_views
urlpatterns = [
    path('', ai_doctors_views, name='ai_doctors_views')
]
