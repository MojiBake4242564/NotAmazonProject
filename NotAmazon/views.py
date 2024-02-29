from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


# Create your views here.
def index(request):
    context = {} #dictionary. This is optional information that we can pass from the view
    context["Title"] = "I have the power, there can be only one!"
    return render(request, "home.html", context)


def products(request):
    return render(request, "products.html", {})



def shop(request):
    # Create a list of items in the Item table
    item_list = Item.objects.all()
    
    # Our context dictionary
    context = {"item_list":item_list}
    return render(request, "shop.html", context)
