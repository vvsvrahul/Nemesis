from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class BlogContent(models.Model):
#         user = models.OneToOneField(User,on_delete=models.CASCADE)
#         Title = models.CharField(max_length = 20)
#         content = models.CharField(max_length=5000)
#         def __str__():
#             return self.user.username
#


class UserAddress(models.Model):
        user  = models.OneToOneField(User,related_name='stories',on_delete=models.CASCADE)
        address = models.CharField(max_length=5000,null=True)
        def __str__(self):
            return self.user.username



