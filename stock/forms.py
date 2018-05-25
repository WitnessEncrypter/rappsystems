from django import forms


class AddStock(forms.Form):
    stock_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Stock Item Name'}))
    stock_category = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Category'}))
    purchase_price = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Stock Price'}))
    client_id = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Client ID'}))
    stock_quantity = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Stock Quantity'}))
    stock_unit = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Stock Unit'}))
    selling_price_per_unit = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Stock Selling Price'}))

