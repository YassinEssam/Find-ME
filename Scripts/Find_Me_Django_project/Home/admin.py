# Ali_Sobeih
# #Aasdfghjkl2314

from django.contrib import admin
# from .models import User
from userdata.models import User

# # Register your models here.
admin.site.register(User)

# change the admin pannel design

admin.site.site_header = "Find Me Adminstration Pannel"
admin.site.site_title = "Find Me Admin"


# here we register the user table 
# now for adjust it's appearence we will make another class just for design and register it
class DesignAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'phone_number'] # to diplay this to attrbutes with the name
    list_editable = ['phone_number'] # to enable editing without enter to the object
    # note that this names should be the same as table in models

    search_fields = ['username']
    

# now register this class also
# Register your models here.
# admin.site.register(User, DesignAdmin)


