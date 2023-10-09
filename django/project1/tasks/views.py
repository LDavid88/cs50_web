from django.shortcuts import render
from django import forms

# Create your views here.
items = ["apples", "carrots", "bananas"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")

def index(request):
    return render(request, "tasks/index.html", {
        "items": items
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            items.append(task)
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
