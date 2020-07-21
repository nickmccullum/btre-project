from django.shortcuts import render

def index(request):
    return render(request, 'templates/listings/listings.html')

def listing(request):
    return render(request, 'templates/listings/listing.html')

def search(request):
    return render(request, 'templates/listings/search.html')