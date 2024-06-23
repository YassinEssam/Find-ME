from django.db import models
from datetime import datetime
# from Home.models import User
from lost.models import Lostperson

# Create your models here.

class Foundperson(models.Model):
    name = models.CharField(max_length=100, blank=True, default="empty", null=True)
    phone_number = models.CharField(max_length=100, default="empty", null=True)
    address = models.CharField(max_length=50, blank=True, default="egypt", null=True)
    age = models.FloatField(default=10, blank=True, null=True)
    finder_name = models.CharField(max_length=100, default="ali", null=True)
    city = models.CharField(max_length=15, null=True, blank=True, default="empty")
    date = models.DateField(default=datetime.now, null=True)
    photo = models.ImageField(upload_to="photos/%y/%m/%d", default="photos/%y/%m/%1")
    # time = models.TimeField(null= True, blank=True, default=datetime.now)
    # current_date_time = models.DateTimeField(null= True, default=datetime.now)

    def __str__(self):
        return self.name if self.name else 'Unnamed Person'
    
    class Meta:
        ordering = ['name'] # the order of objects