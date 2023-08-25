from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='login_view')
def ai_doctors_views(request):
    return render(request, 'ai_doctors/ai_doctors.html')
