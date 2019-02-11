from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
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
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')

