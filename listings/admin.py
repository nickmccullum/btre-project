from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') #What data is displayed
    list_display_links = ('id', 'title') #What data contains links to detailed view
    list_filter = ('realtor',) #What data appears in the right sidebar for filtering purposes
    list_editable = ('is_published',)
admin.site.register(Listing, ListingAdmin)