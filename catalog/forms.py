'''
Created on Dec 10, 2013

@author: Yelei
'''
from django import forms
from catalog.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model=Product
    
    def clean_price(self):
        if self.cleaned_data['price']<=0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_date['price']
    