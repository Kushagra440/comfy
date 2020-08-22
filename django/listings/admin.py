from django.contrib import admin

# Register your models here.
from . models import Listing  #class listing made in models of listings

admin.site.register(Listing)
