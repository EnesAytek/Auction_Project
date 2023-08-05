from django.contrib import admin
from django.urls import path
from .views import index, all_auctions, auction_detail, stake, login_view, my_auctions, logout_view,register


urlpatterns = [
    path('', index, name='index' ),
    path('all-auctions/', all_auctions, name='all_auctions'),
    path('my-auctions/', my_auctions, name='my_auctions'),
    path('auction/<slug:auction_slug>/', auction_detail, name='auction_detail'),
    path('stake/<int:auction_id>/', stake, name='stake'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
