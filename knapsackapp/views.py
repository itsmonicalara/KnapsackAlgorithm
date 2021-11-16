from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory 
from . import forms
# Create your views here.
def index(request):
    return render(request, 'knapsackapp/index.html')

def aboutus(request):
    return render(request, 'knapsackapp/aboutus.html')

def input(request):
    
    items_formset_factory = formset_factory(forms.ItemsForm, extra=0)
    
    if request.method == 'POST':
        form = request.POST
        print(form['capacity'])
        print(form)
        


        
      
    return render(request, 'knapsackapp/input.html', {'form': items_formset_factory})

def results(request):
    return render(request, 'knapsackapp/results.html')