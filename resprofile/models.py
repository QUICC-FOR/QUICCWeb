from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    firstname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60,primary_key=True,unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    grade = models.CharField(max_length= 100,null=True)
    university= models.CharField(max_length=100,null=True)
    proj_title = models.CharField(max_length=60,null=True)
    proj_abstract = models.TextField(max_length=1000,null=True)
    keywords = models.CharField(max_length = 100,null=True)
    pers_website = models.URLField(null=True)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

