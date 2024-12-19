from django.contrib import admin
from Bast_App.models import *

# Register your models here.

admin.site.site_header = 'Resturant | Manoj Gain'
admin.site.site_title = 'ShuvraMoni Gain'
admin.site.index_title = 'Resturant Project'  



class ItemListAdmin(admin.ModelAdmin):
    list_display=['id','category_name','create_at','update_at']
admin.site.register(ItemList, ItemListAdmin)


class ItemsAdmin(admin.ModelAdmin):
    list_display=['id','item_name','category','price','create_at','update_at']
admin.site.register(Items, ItemsAdmin)   


class AboutUsAdmin(admin.ModelAdmin):
    list_display=['id','create_at','update_at']
admin.site.register(AboutUs, AboutUsAdmin)   



class FeedbackAdmin(admin.ModelAdmin):
    list_display=['id','user_name','description','rating','create_at','update_at']
admin.site.register(Feedback, FeedbackAdmin)   


class BookAdmin(admin.ModelAdmin):
    list_display=['id','name','phone','email','total_person','create_at','update_at']
admin.site.register(Book, BookAdmin)   