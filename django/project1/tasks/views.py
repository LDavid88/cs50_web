from django.shortcuts import render

# Create your views here.
items = ["apples", "carrots", "bananas"]

def index(request):
    return render(request, "tasks/index.html", {
        "items": items
    })