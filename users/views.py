from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
import logging
from .models import User
from .forms import SignupForm, UserProfileForm


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
            user = authenticate(request, username=username_or_email, password=password)

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
            form.save()  # Save the user with default 'Manager' role
            return redirect('login')  # Redirect to login page or wherever you want
    else:
        form = SignupForm()
      
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):  # Rename the function
    logout(request)  # Call the imported logout function
    return redirect('login')  # Redirect to the login page

@login_required
def profile_view(request):
    print("Profile view accessed")  # Debugging output
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    """Allow the user to update their profile."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  # Redirect to profile view after saving
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Update session so the user doesn't get logged out
            update_session_auth_hash(request, form.user)
            return redirect('users:profile')  # Redirect to profile view after password change
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'users/change_password.html', {'form': form})