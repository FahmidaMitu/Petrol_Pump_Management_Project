from typing import ContextManager
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactModelForm
from .models import Contact


def contact(request):
    return render(request, 'cat.html') 



def preview(request):
    context = {
        'items': Contact.objects.all()
    } 
    return render(request, 'book_view.html', context) 



def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        fuel_type = request.POST['fuel_type']
        fuel_amount = request.POST['fuel_amount']
        password = request.POST['password']
        if fuel_type == 'petrol':
            price = int(int(fuel_amount) * 52)
        elif fuel_type == 'octane':  
            price = int(int(fuel_amount) * 95)
        elif fuel_type == 'diesel':
            price = int(int(fuel_amount) * 65) 
        elif fuel_type == 'natural_gas': 
            price = int(int(fuel_amount) * 64)
        else:
            price = int(int(fuel_amount) * 42)   


        book = Contact.objects.create(name=name, password=password, fuel_type=fuel_type, fuel_amount=fuel_amount, price=price)
        book.save()
        return redirect('preview')
    else:
        return render(request, 'cat.html')