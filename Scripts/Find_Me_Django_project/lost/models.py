from django.db import models
from datetime import datetime
# from Home.models import User

# Create your models here.
class Lostperson(models.Model):
    name = models.CharField(max_length=100, blank=True, default="empty")
    phone_number = models.CharField(max_length=100, default="empty", null=True)
    address = models.CharField(max_length=50, blank=True, default="egypt", null=True)
    age = models.FloatField(default=10, blank=True, null=True)
    finder_name = models.CharField(max_length=100, default="ali", null=True)
    city = models.CharField(max_length=15, null=True, blank=True, default="empty")
    date = models.DateField(default=datetime.now, null=True)
    photo = models.ImageField(upload_to="photos/%y/%m/%d", default="photos/%y/%m/%1")

    
    # name = first_name # + last_name
    # phone_number = request.POST.get('phone_number')
    # address = request.POST.get('address')
    # age = request.POST.get('age')
    # finder_name = request.POST.get('finder_name')
    # city = request.POST.get('city')
    # date = request.POST.get('date')
    # photo = request.POST.get('photo')
    # type = models.CharField(max_length=50, default='', blank= True , choices= [('lost','lost'),('finded','finded')])
    # choices field is a list of tuples, each category is a tuple, is is tuple bec one value is for admin panel and 
    # the other is for data base
    # time = models.TimeField(null= True, blank=True, default=datetime.now)
    # current_date_time = models.DateTimeField(null= True, default=datetime.now)
    # relation = models.OneToOneField()

    # to make object name appear in admin panel for each object istead ( class object )
    def __str__(self):
        return self.name if self.name else 'Unnamed Person'
    class Meta:
        #verbose_name = 'Losts' # the title for all objects ( for this class ) the name of class instead "Lostperson"
        ordering = ['name'] # the order of objects
