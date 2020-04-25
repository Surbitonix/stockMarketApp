from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm
import requests
import json

def home(request):
	#call the api

	if request.method == "POST":
		#this ticker is the name of the input field on home.html
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_64d33541d37842c09159ce45739811d4")
		errorMessage= "Request failed - " +ticker.upper()+ " is not a valid ticker or quote is not available"
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Request failed"
			
		return render(request, 'home.html', {'api':api,'errorMessage':errorMessage})
	else:
		return render(request, 'home.html', {'ticker':"Enter a symbol ticker..."})

def about(request):
	return render(request, 'about.html',{})


def add_stock(request):
	
	#call the api

	if request.method == "POST":
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, "Stock has been susccessfully added")
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		#loop through tickers to request them back from the api
		ticker_list = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_64d33541d37842c09159ce45739811d4")
			try:
				api = json.loads(api_request.content)
				ticker_list.append(api)
			except Exception as e:
				api = "Request failed"


		return render(request,'add_stock.html',{'ticker':ticker, 'ticker_list':ticker_list})


def delete_stock(request,item_id):
	item = Stock.objects.get(pk=item_id)
	item.delete()
	messages.success(request,"Stock susccessfully removed from portfolio")
	return redirect('remove_stock')


def remove_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'remove_stock.html',{'ticker':ticker})




		