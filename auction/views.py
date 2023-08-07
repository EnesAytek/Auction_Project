from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Auction
from .forms import LoginForm, RegisterForm
from django.contrib import messages


def index(request):
    auctions = Auction.objects.filter(is_active=True).order_by('-start_auction')[:2]
    context = dict(
        auctions=auctions,
        )
    return render(request, 'index.html', context)

def all_auctions(request):
    auctions = Auction.objects.filter(is_active=True)
    context = dict(
        auctions=auctions,
        )

    return render (request, 'all_auctions.html', context)




def my_auctions(request):
    user = request.user
    auctions = user.auction_joined.all()
    context = dict(auctions=auctions)
    return render(request,'my_auctions.html',context)

def my_last_bids(request):
    user = request.user
    auctions = user.winner.all()
    context = dict(auctions=auctions)
    return render(request,'my_last_bids.html', context)


def auction_detail(request, auction_slug):
    auctions = Auction.objects.filter(slug=auction_slug)
    context = dict(auctions=auctions)
    return render(request, 'auction_detail.html', context)


    


def stake(request, auction_id):
    if request.method == 'POST':
        auction = Auction.objects.get(id=auction_id)
        user = request.user
        auction.current_price += auction.increase_price
        auction.user.add(user)
        auction.save()
    
    return redirect('my_auctions')






def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=username, 
                password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect ('index')
                else:
                    messages.info(request,'Disabled Account')
        else:
            messages.info((request,'Chech Your Username and Password'))
    else:
        form = LoginForm()

    return render(request,'login.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})



