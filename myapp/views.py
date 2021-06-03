from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist, Item
from .forms import Createnew

# Create your views here.
def index(response, id):
	ls=Todolist.objects.get(id=id)
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for i in ls.item_set.all():
				if response.POST.get("c" + str(i.id)) == "clicked":
					i.complete=True
				else:
					i.complete=False

				i.save()

		elif response.POST.get("newitem"):
			txt = response.POST.get("new")

			if len(txt) > 2:
				ls.item_set.create(text=txt, complete=False)
			else:
				print("invalid")

	return render(response,"myapp/list.html",{"ls":ls})


def home(response):
	return render(response,"myapp/home.html",{})


def create(response):
	if response.method == "POST":
		form = Createnew(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = Todolist(name=n)
			t.save()
			response.user.todolist.add(t)

		return HttpResponseRedirect("/%i" %t.id)	
	else:
		form = Createnew()
	return render(response,"myapp/create.html",{"form":form})

def view(response):
	return render(response,"myapp/view.html",{})