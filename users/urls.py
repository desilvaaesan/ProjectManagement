from django.urls import path
from . import views

app_name = 'users'  # Set namespace for this app


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'), 
    path('profile/', views.profile_view, name='profile'), 
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/change_password/', views.change_password, name='change_password'),

]
