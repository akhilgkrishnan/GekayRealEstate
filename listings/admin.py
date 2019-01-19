from django.contrib import admin

from .models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' , 'is_Published' , 'price' , 'state', 'list_data' , 'realtor')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_Published',)
    search_fields=('title','description','address','city','state','zipcode')
admin.site.register(Listing,ListingAdmin)

# Register your models here.
