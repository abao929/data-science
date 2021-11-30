from bs4 import BeautifulSoup as bs
import requests
import sqlite3

### IEX TRADING API METHODS ###
IEX_TRADING_URL = "https://cloud.iexapis.com/stable/stock/"


### YAHOO FINANCE SCRAPING
MOST_ACTIVE_STOCKS_URL = "https://cs1951a-s21-brown.github.io/resources/stocks_scraping_2021.html"

### Register at IEX to receive your unique token
TOKEN = 'pk_ae767f1c13474defabc62bc5194d6ee3'

# TODO: Use BeautifulSoup and requests to collect data required for the assignment.
req = requests.get(MOST_ACTIVE_STOCKS_URL)
html = bs(req.content, 'html.parser')
table = html.find('table')
rows = table.find_all('tr')[1:]
data_table = []
for row in rows:
    row_info = []
    cols = row.find_all('td')[1:]
    row_info.append(cols[0].text)
    row_info.append(cols[1].text.strip())
    row_info.append(cols[2].text.replace(',', ''))
    row_info.append(float(cols[4].text.split('%')[0]))
    num = cols[5].text
    num = num.replace('.', '')
    num = num.replace('M', '0000')
    num = num.replace('K', '0')
    row_info.append(int(num))
    row_info.append(cols[6].text.lower().strip())
    data_table.append(row_info)
# TODO: Save data below.

#TODO: Use IEX trading API to collect sector and news data. 
may_25 = 1621900800000
symbols = [row[1] for row in data_table]
for x in range (0, len(symbols)):
    chart_url = f'{IEX_TRADING_URL}/{symbols[x]}/chart/5d/?chartCloseOnly=true&token={TOKEN}'
    chart = requests.get(chart_url)
    print(f'cycle {x+1}: {chart.status_code}')
    if chart.status_code in range(200, 299) and len(chart.json()) > 0:
        data = chart.json()
        sum = 0.0
        for day in data:
            sum += day['close']
        data_table[x].append(sum/len(data))
    else:
        data_table[x].append(None)
    news_url = f'{IEX_TRADING_URL}/{symbols[x]}/news/last/50/?token={TOKEN}'
    news = requests.get(news_url)
    if news.status_code in range(200, 299) and len(news.json()) > 0:
        data = news.json()
        data = list(filter(lambda x: x['datetime'] > may_25, data))
        data_table[x].append(len(data))
    else:
        data_table[x].append(None)
        
for row in data_table:
    if None in row:
        data_table.remove(row)

# Create connection to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create connection to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "companies";')
c.execute('DROP TABLE IF EXISTS "quotes";')

#TODO: Create tables in the database and add data to it. REMEMBER TO COMMIT
c.execute('CREATE TABLE companies(symbol text not null, name text, location text)')
c.execute('CREATE TABLE quotes(symbol text not null, price float, avg_price float, num_articles int, volume int, change_pct float)')
for row in data_table:
    c.execute('INSERT INTO companies(symbol, name, location) VALUES (?, ?, ?)', (row[1], row[0], row[5]))
    c.execute('INSERT INTO quotes(symbol, price, avg_price, num_articles, volume, change_pct) VALUES (?, ?, ?, ?, ?, ?)', (row[1], row[2], row[6], row[7], row[4], row[3]))
conn.commit()