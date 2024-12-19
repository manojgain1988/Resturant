
from django.urls import path
from Bast_App  import views

urlpatterns = [
   path('', views.Home, name='home'),
   path('about/', views.About, name='about'),
   path('menu/', views.Menu, name='menu'),
   path('book/', views.BookTable, name='book'),
   path('feedback/', views.feedback, name='feedback'),
  
]