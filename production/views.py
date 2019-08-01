from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Detail, Product, Demand_Signal
# Create your views here.

def index(request):
    #Product.objects.all() read the table
    inventory = Product.objects.all()
    # name = ''
    # for p in inventory:
    #     name += (p.product_name + ", ")
    return render(request, 'views/index.html', {'inventory': inventory})

def product_detail_view(request, id): 
        detail = get_object_or_404(Detail,id=id)
        context = {'detail':detail,
                }
        return render(request, 'views/detail.html', context)

def event(request): 
        context = {}
        system = request.POST.get('system', None)
        context['system'] = system
        return render(request,'views/event.html', context)

def demand(request):
        catalog = Demand_Signal.objects.all()
        for m in catalog:
                name +=(m.demand_score)
        #return HttpResponse("<h1>Demand Module</h1>")  
        return render(request, 'views/demand.html', {})

def contact(request):
    return HttpResponse("<h1>Page under construction</h1>") #Session 1, 2:01:52