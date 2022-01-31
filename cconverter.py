import requests

currency_code = input()

url = f'http://www.floatrates.com/daily/{currency_code.lower()}.json'
r = requests.get(url).json()

cache = {}

if currency_code.lower() != 'usd':
    cache['usd'] = float(r['usd']['rate'])
if currency_code.lower() != 'eur':
    cache['eur'] = float(r['eur']['rate'])

while True:
    currency_receive = input()
    if currency_receive == '':
        exit()
    money = float(input())
    print('Checking the cache...')
    rate = float(r[currency_receive.lower()]['rate'])
    if currency_receive.lower() in cache.keys():
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[currency_receive.lower()] = rate

    outcome = round(money * rate, 2)
    print(f'You received {outcome} {currency_receive.upper()}.')
