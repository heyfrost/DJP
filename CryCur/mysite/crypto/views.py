from django.shortcuts import render
import json
import requests


def home(request):
    # news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    # price data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,ADA,USDT,MIOTA,"
        "TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method =='POST':
        quote=request.POST['quote']
        quote=quote.upper()
        q_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD,EUR")
        q = json.loads(q_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto':q})
    else:
        notfound="Enter Crypto Currency Symbol in Search and search"
        return render(request, 'prices.html', {'notfound': notfound})
