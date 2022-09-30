import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import mariadb

data = []

def currency_scraper():

	url = "https://finance.yahoo.com/quote/EURUSD%3DX/history?p=EURUSD%3DX"
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                         "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                         "Version/15.4 Safari/605.1.15"}
	res = requests.get(url, headers=headers)
	pprint(res)
	soup = BeautifulSoup(res.text, 'html.parser')
	rows = soup.select('tr')[1:6]

	conn = mariadb.connect(
    user="278874",
    password="Dani2020.",
    host="mysql-testjfpldb.alwaysdata.net",
    database="testjfpldb_scrap")
	cur = conn.cursor() 

	for idx, item in enumerate(rows):
		cells = item.select("td")

		date = cells[0].select("span")[0].getText()			
		open_price = cells[1].select("span")[0].getText()			
		high_price = cells[2].select("span")[0].getText()			
		low_price = cells[3].select("span")[0].getText()			
		close_price = cells[4].select("span")[0].getText()			
		adj_close_price = cells[5].select("span")[0].getText()

		cur.execute("SELECT date FROM scrap WHERE open=? and date=? and close=? and adj_close=? and high=? and low=?", (open_price,date,close_price,adj_close_price,high_price,low_price)) 
		if(cur.rowcount == 0 and idx < 5):
			#insert information 
			try: 
				cur.execute("SELECT * FROM scrap WHERE date=%s", [(date)])
				if(cur.rowcount == 0):
					cur.execute("INSERT INTO scrap (date,open,close,adj_close,high,low) VALUES (?,?,?,?,?,?)", (date,open_price,close_price,adj_close_price,high_price,low_price)) 
					data.append({
						"date": date,
						"open": open_price,
						"close": close_price,
						"adj_close": adj_close_price,
						"high": high_price,
						"low": low_price
					})
				else:
					cur.execute("UPDATE scrap SET date=%s,open=%s,close=%s,adj_close=%s,high=%s,low=%s WHERE date=%s", (date,open_price,close_price,adj_close_price,high_price,low_price,date))
			except mariadb.Error as e: 
				print(f"Error: {e}")
			conn.commit() 

	conn.close()
	with open('eur_usd_data.json', 'w') as outfile:
	    json.dump(data, outfile)

	return data


# pprint.pprint(currency_scraper());	