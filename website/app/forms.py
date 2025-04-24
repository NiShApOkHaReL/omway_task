from django import forms
from .models import Company, News, PriceHistory

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'address', 'description']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['company', 'news_title', 'news_date', 'news_image', 'news_body']

class PriceHistoryForm(forms.ModelForm):
    class Meta:
        model = PriceHistory
        fields = ['company', 'date', 'open_price', 'high_price', 'low_price', 'close_price']
