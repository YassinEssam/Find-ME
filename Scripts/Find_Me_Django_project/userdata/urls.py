from django.urls import path
from . import views # from here (my working directory) import views file 
from Home import views as homeviews


# the context is a dictionary
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', homeviews.home , name='home'),

    # Add more URL patterns as needed...
]