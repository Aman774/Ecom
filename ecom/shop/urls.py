from django.contrib import admin
from django.urls import path
import include
from . import views

urlpatterns = [
    path('',views.index,name="shopHome"),

    path('about/',views.about,name="AboutPage"),

    path('products/<int:myid>',views.products,name="product page"),
    path('contactPage/',views.contactUs,name="ContactPage"),
    path('checkoutPage/',views.checkout,name="checkoutPage"),
    path('tracker/',views.tracker,name="trackerPage"),
    path('search/',views.search,name="SearchPage"),
    path('contactSubmitResponse/',views.contactResponse,name="contactResponse")
]
