from django.contrib import admin
from .models import Auction, Product

class AuctionAdmin(admin.ModelAdmin):
     list_display = [
        'name',
        'current_price',
        'start_auction',
        'finish_auction',
        'is_active'
    ]
     
class ProductAdmin(admin.ModelAdmin):
     list_display = [
        'name',
        'image'
    ]     

admin.site.register(Auction, AuctionAdmin)
admin.site.register(Product, ProductAdmin)


