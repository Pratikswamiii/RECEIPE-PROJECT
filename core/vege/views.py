from django.shortcuts import render, redirect 
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def receipes(req):
    if req.method=="POST":
        data=req.POST

        receipe_name=data.get('receipe_name')
        receipe_image=req.FILES.get('receipe_image')
        receipe_description=data.get('receipe_description')
              


 

        Receipe.objects.create (
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )
         
  

        


    queryset=Receipe.objects.all()

    if req.GET.get('search'):
            queryset=queryset.filter(receipe_name__icontains=req.GET.get('search'))
           

    context={'receipes':queryset}
    
    return render(req,"receipes.html",context)


def update_receipe(req,id):
    queryset=Receipe.objects.get(id =id)
    context ={'receipe':queryset}

    if req.method=="POST":
        data=req.POST

        receipe_image=req.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image

            queryset.save(),
            return redirect('/receipes/')
        
        

    context={'receipe':queryset}
    return render(req,'update_receipe.html',context)


def delete_receipe(req,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")


def login_page(req):
    return render(req,'login.html')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def register_page(req):
    if req.method == "POST":
        first_name = req.POST.get("first_name")
        last_name = req.POST.get("last_name")
        username = req.POST.get("username")
        password = req.POST.get("password")

        # Username check
        if User.objects.filter(username=username).exists():
            messages.error(req, "Username already exists!")
            return render(req, "register.html")

      

        # Create user
        user = User.objects.create(
            username=username,
            
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(req, "Account created successfully!")
        return redirect('/receipes/')

    # GET request
    return render(req, "register.html")

