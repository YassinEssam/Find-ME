from django.db import models

# # Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=100, default="", blank=True, null=True)
#     #  password = models.OneToOneField(Hashedpassword, on_delete="CASCADE")
#     password = models.CharField(max_length=50, default="", blank=True, null=True)
#     email = models.CharField(max_length=100, default="", blank=True, null=True)
#     phone_number = models.IntegerField(default=1, blank=True, null=True)
#     # user_id = models.UniqueConstrain

#     def __str__(self):
#         return self.username
    
#     class Meta:
#         ordering = ['username']


# # class Hashedpassword(models.Model):
# #     hashedvalue = models.CharField(max_length=128)
