from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def home (req):
#     return HttpResponse("<h1> Hey i am django server </h1>" "<p> ho welocomewahgdvaghdvgahsvdgasvdghasvdgahdgsvaghdasvzgh </p>")

def home(req):
    peoples=[
        {'name': 'pratik swami','age':25},
        {'name': 'virat kohli','age':34},
        {'name': 'yash dayal','age':30},
        {'name': 'roman reigins','age':45},
        {'name': 'anuv jain','age':28},

    ]
    return render(req,"home/index.html",context={'peoples':peoples})

def about(req):
 
    return render(req,"home/about.html",context={'page':'contact'})

def contact(req):
 
    return render(req,"home/contact.html",context={'page':'about'})



