from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from userdata.models import User
from lost.models import Lostperson
from found.models import Foundperson
# Create your views here.

def home(request):
    # return render(request, 'home/home.html')
    # return HttpResponse("Home app , index function response")

    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # phone_number = request.POST.get('phone_number')
    # email = request.POST.get('email')
    # data = User(username=username, password=password, email=email, phone_number=phone_number)
    # data.save()

    # user = authenticate(request, username=username, password=password)
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home/home.html')  # Redirect to dashboard or home page after login
    #     else:
    #         return render(request, 'home/home.html', {'error_message': 'Invalid username or password.'})
    # else:
    #     return render(request, 'home/home.html')

    # now when there is a post reqest from this rendered page the the data in post request from this templete
    # will save automaticcally in database 
    # to see it from admin pannel just register the class User in admin page.
    return render(request, 'home/home.html', {'Lostperson':Lostperson.objects.all(), 'Foundperson': Foundperson.objects.all()})
    # def lost(request):
    #     return render(request, 'lost/lost.html')
    # def found(request):
    #     return render(request, 'found/found.html')

# def register_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')

#         # Check if the username is available
#         if User.objects.filter(username=username).exists():
#             return render(request, 'login.html', {'error_message': 'Username already exists. Please choose a different one.'})

#         # Create a new user
#         user = User.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
#         login(request, user)
#         return redirect('home/home.html')  # Redirect to dashboard or home page after registration
#     else:
#         return render(request, 'register.html')  # Render the registration form
