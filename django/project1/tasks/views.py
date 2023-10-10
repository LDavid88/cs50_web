from django.shortcuts import render
from django import forms

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")

def index(request):
    if "items" not in request.session:
        request.session["items"] = []
    return render(request, "tasks/index.html", {
        "items": request.session["items"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["items"] += [task]
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
