from django.urls import path
from . import views # from here (my working directory) import views file 

# the context is a dictionary
urlpatterns =[
    path('', views.found, name = 'foundpage'),
]