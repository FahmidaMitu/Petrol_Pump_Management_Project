from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.


def home(request):
    emenities = Emenities.objects.all()
    context = {'emenities': emenities}
    return render(request, 'home.html', context)


def cart(request):
    return render(request, 'cart.html')


def payment(request):
    return render(request, 'payment.html')


def api_gas(request):
    gas_objs = Gas.objects.all()
    available_amount = request.GET.get('available_amount')
    if available_amount:
        gas_objs = gas_objs.filter(available_amount__lte=available_amount)

    emenities = request.GET.get('emenities')
    if emenities:
        emenities = emenities.split(',')
        em = []
        for e in emenities:
            try:
                em.append(int(e))
            except Exception as e:
                pass
        gas_objs = gas_objs.filter(emenities__in=em).distinct()

    payload = []
    for gas_obj in gas_objs:
        result = {}
        result['pump_name'] = gas_obj.pump_name
        result['pump_image'] = gas_obj.pump_image
        result['pump_address'] = gas_obj.pump_address
        result['available_amount'] = gas_obj.available_amount
        payload.append(result)
    return JsonResponse(payload, safe=False)
