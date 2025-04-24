from django.db import models
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name 
    
class News(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='news')
    news_title = models.CharField(max_length=200)
    news_date = models.DateField()
    news_image = models.ImageField(upload_to='news_images/')
    news_body = models.TextField()

    def __str__(self):
        return f"{self.news_title} ({self.company.name})"

class PriceHistory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='price_histories')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Price History for {self.company.name} on {self.date}"
