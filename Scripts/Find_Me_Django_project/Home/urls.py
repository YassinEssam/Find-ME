from django.urls import path
# from django.conf.urls import urls, include
from . import views # from here (my working directory) import views file 
from lost import views as lostviews
from found import views as foundviews 
from userdata import views as userviews
# the context is a dictionary
urlpatterns =[
    path('', views.home, name = 'homepage'),
    path('register', userviews.register, name = 'register'),
    path('login', userviews.login, name = 'login'),
    path('lostpage', lostviews.lost, name = 'lostpage'),
    path('foundpage', foundviews.found, name = 'foundpage'),
]

# the name is used when we want to acces this url (that direct to view then direct to html page) from templete files
#                               to access the same path from template so the same function for this line can be 
#                               made by using this name in url tag in dtl in template files
# briefly the name is used to get the views.home but from template files not from url in the site



# path('lost', views.lost, name = 'lostpage'),
# path('found', views.found, name = 'foundpage'),