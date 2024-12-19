from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class ItemList(models.Model):
    category_name = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    

# def ImageUrl(self):
#         if self.image:
#             return self.image.url
#         else:
#             return ""

# def image_tag(self):
#         return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
# image_tag.short_description = 'Image'


# list_display = ['id','title','image_tag', 'status', 'created_at', 'updated_at']


    
class Items(models.Model):
    item_name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    category =  models.ForeignKey(ItemList, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name
    
    

class AboutUs(models.Model):
    description = models.CharField(blank=True, max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description
    
    

class Feedback(models.Model):
    user_name = models.CharField(blank=True, max_length=50)
    description = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='feedback/',blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_name
    
    

class Book(models.Model):
    name = models.CharField(blank=True, max_length=50)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    total_person = models.IntegerField(default=0)
    booking_date = models.DateField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    