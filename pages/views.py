from django.shortcuts import render
from django.http import HttpResponse
from listings.choice import price_choices,bedroom_choices,state_choices                                                                                                                 
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_Published=True)[:3]
    context = {
        'listings': listings,
        'state_choices':state_choices,    }
        'bedroom_choice':bedroom_choices,
        'price_choice':price_choices
    return render(request, 'pages/index.html', context)
def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    #Get Mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html',context)   
    
    

# Create your views here.
