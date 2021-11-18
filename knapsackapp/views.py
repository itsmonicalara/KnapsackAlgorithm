from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory 
import json
from . import forms
from knapsackapp.scripts.item import Item
from knapsackapp.scripts.knapsack import Knapsack
from knapsackapp.scripts.tabulated import tabulated
# Create your views here.
def index(request):
    return render(request, 'knapsackapp/index.html')

def aboutus(request):
    return render(request, 'knapsackapp/aboutus.html')

def input(request):
    items_formset_factory = formset_factory(forms.ItemsForm, extra=0)
    if request.method == 'POST':
        form = request.POST
        print(form)
        knapsack = Knapsack(form.get('capacity'), len(form.getlist('names')))
        list_items = list(map(lambda w,v,n: Item(w,v,n), form.getlist('weights'), form.getlist('values'), form.getlist('names')))
        tabulated(knapsack, list_items)
        #Should implement the is_valid function from Django, not a good practice
        
        return render(request, 'knapsackapp/results.html', {'knapsack': knapsack})
      
    return render(request, 'knapsackapp/input.html', {'form': items_formset_factory})

def results(request):
    return render(request, 'knapsackapp/results.html')