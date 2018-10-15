import requests

# URLs to use
url = 'https://api.coinmarketcap.com/v2/global'
url_list = 'https://api.coinmarketcap.com/v2/listings/'
url_coin = 'https://api.coinmarketcap.com/v2/ticker/'

continuation = 1

while True:
    while continuation == 1:
        response = requests.get(
            url,
            headers={'Accept':'application/json'}
            )

        response_list = requests.get(
            url_list,
            headers={'Accept':'application/json'}
            )

        # General marketcap data
        data = response.json()
        data_sp = data['data']
        data_quotes = data_sp['quotes']
        data_usd = data_quotes['USD']
        data_usd_total = data_usd['total_market_cap']
        data_usd_vol = data_usd['total_volume_24h']

        # Listings data
        data_list = response_list.json()
        data_list_sp = data_list['data']

        print('Crypto-board v0.2\n')
        print('BTC market percentage is {} %'.format(data_sp['bitcoin_percentage_of_market_cap']))
        print('Total market cap is {} billions USD with a 24h volume of {} billions USD\n'.format(round(data_usd_total/1000000000, 2), round(data_usd_vol/1000000000, 2)))

        # Getting ticker for coin
        user_input = input('What coin are you looking for? ' ).upper()

        # Creating new list for matching ticker, containing 1 dict
        element_list = [element for element in data_list_sp if element['symbol'] == user_input]

        # Accesing dict keys
        coin_id = str(element_list[0].get('id'))
        coin_name = str(element_list[0].get('name'))

        url_coin_complete = 'https://api.coinmarketcap.com/v2/ticker/{}'.format(coin_id)

        response_coin = requests.get(
            url_coin_complete,
            headers={'Accept':'application/json'}
            )

        # Coin data
        data_coin = response_coin.json()
        data_sp_coin = data_coin['data']
        data_quotes_coin = data_sp_coin['quotes']
        data_rank_coin = data_sp_coin['rank']
        data_usd_coin = data_quotes_coin ['USD']
        data_usd_price_coin = data_usd_coin['price']
        data_usd_vol_coin = data_usd_coin['volume_24h']
        data_usd_change_24h_coin = data_usd_coin['percent_change_24h']

        print('{} ranks {} with a price of {} USD\nLast 24h volume has been {} USD with a {} % change in price\n'.format(coin_name, data_rank_coin, data_usd_price_coin, data_usd_vol_coin, data_usd_change_24h_coin))
        continuation = 'n'
    player = input('Wanna ask for another cryptocurrency? y/n ')
    if player == 'y':
        continuation = 1
    else:
        print('Thanks for stoping by')
        break
exit()

