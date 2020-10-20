from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.create_listing, name="createlisting"),
    path("newListing", views.new_listing_view, name="newlisting"),
    path("placingBid", views.place_bid, name="placingbid"),
    path("placeBid/<int:listingID>", views.place_bid_view, name="placebid"),
]
