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
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
