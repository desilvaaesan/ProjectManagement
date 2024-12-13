from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.shortcuts import render, redirect
import logging
from .forms import SignupForm

logger = logging.getLogger(__name__)

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        logger.debug(f"Attempting login with email/username: {username_or_email}")

        user = None
        if '@' in username_or_email:  # Check if it's an email
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user = None
        else:  # Otherwise, look for a user by username
            user = User.objects.filter(username=username_or_email).first()

        if user:
            logger.debug(f"User found: {user.username}")
            user = authenticate(request, username=user.username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            # Check the user's role and redirect based on it
            if user.user_role == 'Manager':
                return redirect('manager-dashboard')
            elif user.user_role == 'Member':
                return redirect('member-dashboard')
            else:
                messages.error(request, 'Invalid user role.')
                return redirect('login')
        else:
            logger.debug("Authentication failed")
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'users/login.html')



# User registration view

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('login')  # Redirect to login page or wherever you want
    else:
        form = SignupForm()
    
    return render(request, 'users/register.html', {'form': form})




