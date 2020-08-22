from django.urls import path,include
from . import views

urlpatterns= [
    path('',views.index,name='listings'),
    path('<int:listing_id>',views.listing,name='lisitng'),
    path('search',views.search,name='search')
    #path('about',views.about,name='about')
]
