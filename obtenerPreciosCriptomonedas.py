import requests
import time

headers = {
        'X-CMC_PRO_API_KEY': 'TU_API',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '6',
        'convert': 'USD'
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = params, headers = headers).json()

coins =  json['data']

while True:
    print("Obteniendo Datos")
    for coin in coins:
        if coin['symbol'] == 'BTC':
            file = open("./BTC.txt","w")
            file.write(str(round(coin['quote']['USD']['price'],5) ) + "\n" )
        if coin['symbol'] == 'ETH':
            file = open("./ETH.txt","w")
            file.write(str(round(coin['quote']['USD']['price'],5) ) + "\n" )
        if coin['symbol'] == 'USDT':
            file = open("./USDT.txt","w")
            file.write(str(round(coin['quote']['USD']['price'],5) ) + "\n" )
        if coin['symbol'] == 'BNB':
            file = open("./BNB.txt","w")
            file.write(str(round(coin['quote']['USD']['price'],5) ) + "\n" )
        if coin['symbol'] == 'ADA':
            file = open("./ADA.txt","w")
            file.write(str(round(coin['quote']['USD']['price'],5) ) + "\n" )
        if coin['symbol'] == 'DOGE':
            file = open("./DOGE.txt","w")
            file.write(str(round(coin['quote']['USD']['price'],5) ) + "\n" )
    print("Datos obtenidos")
    time.sleep(60)
