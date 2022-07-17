# Crypto_Converter

# นำเข้า from binance.client import Client
# ติดตั้งผ่าน pip pip install python-binance
# https://python-binance.readthedocs.io/en/latest/
from binance.client import Client
from clint.textui import colored

#ใส่ api_key balance
api_key = "WhHT1kGHGFH2Q2xEPEPvzZoqHGUJtGCALtimIU8koAUUM4HFGHFGHyl9kVrHimZTn" 
#ใส่ api_secret balance
api_secret = "tcOh7mHFHrmAzx20XGhWQPHFHFb9xK9vPKHGztyszEpswWhPgdpKdyuFHFHADSpg"
client = Client(api_key, api_secret)


def Converter_USDT(leverage,symbol,quantity):

    info = client.futures_exchange_info()
    for x in info['symbols']:
        if x['symbol'] == symbol:
            minQty = float(x['filters'][1]['minQty'])
            i = 0
            loop = 0
            while True:
                if i >= minQty:
                    if loop >= 10 and loop <100:
                        Price = client.get_symbol_ticker(symbol=symbol)
                        Quantity_USDT = quantity
                        Quantity =  round(1 / float(Price['price'])*float(quantity*int(leverage)),3)
                        print(colored.green(str(Quantity_USDT)+' '+'USDT'+' '+'= '+str(Quantity)+' '+symbol))
                        return Quantity

                    if loop >= 100 and loop <1000:
                        Price = client.get_symbol_ticker(symbol=symbol)
                        Quantity =  round(1 / float(Price['price'])*float(quantity*int(leverage)),2)
                        Quantity_USDT = quantity
                        print(colored.green(str(Quantity_USDT)+' '+'USDT'+' '+'= '+str(Quantity)+' '+symbol))
                        return Quantity
                        

                    if loop >= 1000 and loop <10000:
                        Price = client.get_symbol_ticker(symbol=symbol)
                        Quantity =  round(1 / float(Price['price'])*float(quantity*int(leverage)),1)
                        Quantity_USDT = quantity
                        print(colored.green(str(Quantity_USDT)+' '+'USDT'+' '+'= '+str(Quantity)+' '+symbol))
                        return Quantity


                    if loop >= 10000 and loop <100000:
                        Price = client.get_symbol_ticker(symbol=symbol)
                        Quantity =  round(1 / float(Price['price'])*float(quantity*int(leverage)))
                        Quantity_USDT = quantity
                        print(colored.green(str(Quantity_USDT)+' '+'USDT'+' '+'= '+str(Quantity)+' '+symbol))
                        return Quantity

                    break

                else:
                    i = i + 0.0001
                    loop = loop + 1
                    loop = loop + 1

     
# leverage
leverage = 20
# symbol
symbol = 'ETHUSDT'
# Quantity USDT
quantity = 10

Converter_USDT(leverage,symbol,quantity)

# FACEBOOK
# https://www.facebook.com/SrangSrrkh/
# YOUTUBE
# Meew Punk
# https://www.youtube.com/channel/UCb69wD525BeeK9WFb8AiLGw
# Github
# https://github.com/MeewPunk
