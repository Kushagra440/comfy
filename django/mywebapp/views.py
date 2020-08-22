from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

from listings.choices import price_choices,bedroom_choices,state_choices

from django.http import HttpResponse


# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[0:3]

    context={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
        }
    #return HttpResponse('<h1>Hello from Home page</h1>')    #can write html code 
    return render(request,'mywebapp/index.html',context)

def about(request):
    realtors=Realtor.objects.order_by('-hire_date')

    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
        }
    

    
    #return HttpResponse('<h2>Hello from About Page</h2>')
    return render(request,'mywebapp/about.html',context)
