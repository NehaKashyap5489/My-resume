from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    context={'home':'active'}
    return render (request,'core/home.html',context)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        con=Contact(name=name,email=email,subject=subject,message=message)
        con.save()
    context={'contact':'active'}
    return render (request,'core/contact.html',context)
