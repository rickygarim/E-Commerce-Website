from django.db import models
import os
def get_image_upload_path(instance, filename):
    app_label = instance._meta.app_label
    print(os.path.join(app_label, "images", filename))
    return os.path.join(app_label, "images", filename)

class Product(models.Model): 
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    images = models.ImageField(upload_to=get_image_upload_path)
    colors_types = models.JSONField(models.CharField(max_length=100), default=list)  
    description = models.TextField()
    home_page = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.name


class Shopper(models.Model): # TODO FIX THIS 
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    items = models.CharField(max_length=10000)
    
    def add_numbers(self, number):
        all_numbers = Shopper.objects.all()
        self.items += (number + ',')
        
    def get_numbers(self):
        return self.items.rsplit(",")
    
    def remove_numbers(self, number):
        numbers = self.items.rsplit(",")
        ans = []
        for num in numbers: 
            if num != number: 
                ans.append(num)
        return ans 
            

        
        
         