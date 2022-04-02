from django.db import models
from django.contrib.models import User
# Create your models here.

class Profile(models.Model):
    profile_pic=models.ImageField(default='default.jpg',upload_to='profile')
    bio=models.TextField(max_length=500)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()