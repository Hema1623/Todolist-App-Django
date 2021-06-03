from django.shortcuts import render,redirect
from .forms import Register
# Create your views here.
def register(response):
    if response.method=="POST":
        form = Register(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = Register()
    return render(response,"register/register.html",{"form" : form})