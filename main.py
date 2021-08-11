import pdb
import requests
import json
import csv
import datetime

def read_stock_symbols():
    with open('stock_list.txt') as stock_file:
        return stock_file.read().splitlines()

stocks = read_stock_symbols()
output = {}

def current_date():
    return datetime.datetime.now().strftime('%x %X')

def yahoo_url(stock):
    return f"https://query1.finance.yahoo.com/v8/finance/chart/{stock}?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"

def write_last_update(csv):
    csv.writerow(["Last Updated", current_date()])

for stock in stocks:
    headers = {'user-agent': 'python-script'}
    source = requests.get(yahoo_url(stock), headers=headers).json()
    output[stock] = source['chart']['result'][0]['meta']['regularMarketPrice']

print(current_date(), ': ', output)

with open('/home/dan/repos/stock-scraper/stocks.csv', 'w', newline='') as csvfile:
    stock_csv = csv.writer(csvfile)
    write_last_update(stock_csv)
    for record in output:
        stock_csv.writerow([record, output[record]])
