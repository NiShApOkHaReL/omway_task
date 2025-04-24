from django.shortcuts import render, redirect
from .forms import CompanyForm, NewsForm, PriceHistoryForm
from .models import PriceHistory


def home(request):
    return render(request, 'home.html')

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


def add_price_history(request):
    if request.method == 'POST':
        form = PriceHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PriceHistoryForm()
    return render(request, 'add_price_history.html', {'form': form})



def view_price_history(request):
    price_histories = PriceHistory.objects.all()  
    return render(request, 'view_price_history.html', {'price_histories': price_histories})


