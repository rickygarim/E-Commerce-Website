from django.db import models

# Create your models here.
# write me a model for a user

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.username
    
    
    
    
