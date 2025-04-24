from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-company/', views.create_company, name='create_company'),
    path('add-news/', views.add_news, name='add_news'),
    path('add-price-history/', views.add_price_history, name='add_price_history'),
    path('view-price-history/', views.view_price_history, name='view_price_history'),

]
