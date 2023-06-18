from django.shortcuts import render

# Create your views here.
def experience(request):
    context={'experience':'active'}
    return render (request,'exp/experience.html',context)
