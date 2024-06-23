# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        national_id = request.POST['national_id']
        email = request.POST['email']
        address = request.POST['address']

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('register')

        # Create new user
        new_user = User(username=username, password=password, phone_number=phone_number,
                        national_id=national_id, email=email, address=address)
        new_user.save()
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if username and password match
        try:
            user = User.objects.get(username=username, password=password)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to home page after successful login
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'login.html')

# node that with render we write the .html extensoin while redirect not bec it like urls it use urls