from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone,dateformat



class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return str(self.name)


class Auction(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Mezat Adı')
    user = models.ManyToManyField(User, blank=True, null=True,related_name='auction_joined')
    product = models.ManyToManyField(Product, blank=True,null=True)
    content = models.TextField(verbose_name='Ürün Açıklama',)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    increase_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_auction = models.DateTimeField(default=timezone.now)
    finish_auction = models.DateTimeField()
    is_active = models.BooleanField()
    slug = AutoSlugField(populate_from='name')



    def __str__(self):
        return str(self.finish_auction)
  
