from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Lostperson
from found.models import Foundperson
from datetime import datetime  # Import datetime for date handling
# Create your views here.
def found(request):
    print("Entering lost view function...")
    if request.method == 'POST':
        # Extract data from POST request
        print("Request method is POST, extracting form data...")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        age = request.POST.get('age')
        finder_name = request.POST.get('finder_name')
        city = request.POST.get('city')
        date_str = request.POST.get('date')
        # Parse date string to datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else None
        photo = request.FILES.get('image')  # Get uploaded image file

        try:
            # Create a new Lostperson instance and save to database
            data = Foundperson(
                name=first_name + ' ' + last_name,
                phone_number=phone_number,
                address=address,
                age=age,
                finder_name=finder_name,
                city=city,
                date=date,
                photo=photo
            )
            print("before save")
            data.save()
            print("after save")
            print("Data saved successfully:", data)
        except Exception as e:
            # Print error message if there's an exception during saving
            print("Error saving data:", e)

        # Redirect to a success URL after saving the data
        return HttpResponseRedirect(reverse('home'), {'Lostperson':Lostperson.objects.all(), 'Founded': Foundperson.objects.all()}) 

    print("Request method is not POST, rendering form...")
    # Render the template with an empty form for GET requests
    return render(request, 'found/found.html')
        
    # now when there is a post reqest from this rendered page the the data in post request from this templete
    # will save automaticcally in database 
    # to see it from admin pannel just register the class User in admin page.
    #return render(request, 'home/home.html', {'name':'ali mohamed abdelaty'})
    return render(request, 'found/found.html', {'Lostperson':Lostperson.objects.all(), 'Foundperson':Foundperson.objects.all()})#.filter(age__exact=20), 'aml': Lostperson.objects.get(name='aml')}) # this path start from template

    return render(request, 'found/found.html')