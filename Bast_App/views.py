from django.shortcuts import render
from Bast_App.models import *

# Create your views here.

def Home(request):
    list =ItemList.objects.all()
    menus = Items.objects.all()
    review = Feedback.objects.all()
    context = {
        'list': list,
        'menus': menus,
        'review': review,
    }
    return render(request,'home.html',context)


def About(request):
    about_data = AboutUs.objects.all()
    context = {
        'about_data': about_data,
    }
    return render(request,'about.html',context)




def Menu(request):
    list =ItemList.objects.all()
    menus = Items.objects.all()
    context = {
        'list': list,
        'menus': menus
    }
    return render(request,'menu.html',context)




def BookTable(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        total_person = request.POST['total_person']
        booking_date = request.POST['booking_date']
        
        
    
        book_data = Book(name=name,phone=phone,email=email,total_person=total_person,booking_date=booking_date)
        book_data.save()
        
    return render(request,'book.html')





def feedback(request):
    
    return render(request,'feedback.html')





