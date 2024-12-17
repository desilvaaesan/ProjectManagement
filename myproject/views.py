# views.py
from django.shortcuts import render

def base_manager(request):
    return render(request, 'base.html', {'dashboard_title': 'Manager Dashboard', 'user': request.user})

def base_member(request):
    return render(request, 'base.html', {'dashboard_title': 'Member Dashboard', 'user': request.user})
