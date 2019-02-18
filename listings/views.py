from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choice import price_choices,bedroom_choices,state_choices                                                                                                                 

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_Published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context ={
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context ={
        'listing':listing
    }
    return render(request, 'listings/listing.html',context)
def search(request):
    queryset_list = Listing.objects.order_by('-list_data')
    #keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
    #city
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)   
    #state
    if 'state' in request.GET:
        state= request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state)                  
     #Bedroom
    if 'bedrooms' in request.GET:
        bedrooms= request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms) 
     #price
    if 'price' in request.GET:
        price= request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)                 
    context = {
        
        'state_choices':state_choices,    
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html',context)

