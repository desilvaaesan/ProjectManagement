from django.shortcuts import render

def base_manager(request):
    return render(request, 'base_manager.html')

def base_member(request):
    return render(request, 'base_member.html')
