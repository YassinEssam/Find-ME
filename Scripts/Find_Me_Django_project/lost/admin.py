from django.contrib import admin
from .models import Lostperson

# Register your models here.
admin.site.register(Lostperson)

# class DesignAdmin(admin.ModelAdmin):
#     list_display = ['name','age', 'date'] # to diplay this to attrbutes with the name
#     list_editable = ['age'] # to enable editing without enter to the object
#     # note that this names should be the same as table in models

#     search_fields = ['name']
#     # list_filter = ['']
#     pass
    

# now register this class also
# Register your models here.
# admin.site.register(Lostperson, DesignAdmin)
