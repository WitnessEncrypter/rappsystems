
from django.shortcuts import render,redirect
from .models import Stock
from .forms import AddStock
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='../')
def index(request):
	stock=Stock.objects.all()
	form = AddStock()
	return render(request, 'stock/index.html',{'form':form,'stock':stock})



def add_stock_view(request):
	if request.method == 'POST':
		form = AddStock(request.POST)
		if form.is_valid():
			
			new_stock = Stock(stock_name=request.POST['stock_name'],
							stock_category=request.POST['stock_category'],
							purchase_price=request.POST['purchase_price'],
							client_id=str(request.user),
							stock_quantity=request.POST['stock_quantity'],
							stock_unit=request.POST['stock_unit'],
							selling_price_per_unit=request.POST['selling_price_per_unit'])
			new_stock.save()
			return redirect('index')
