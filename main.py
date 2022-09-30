from flask import Flask, jsonify, request

from eur_usd_scraper import currency_scraper

import json
import requests
from pprint import pprint

from flask_cors import CORS
import mariadb

app = Flask(__name__)
CORS(app)

def hit_webhook(data):
	requests.post("https://webhook.site/8bb140f1-4bf1-4c39-b975-6235b358dd9e", data=json.dumps(
            data, sort_keys=True, default=str), headers={'Content-Type': 'application/json'})

@app.route('/scrape_currency', methods=['GET'])
def scrape_currency():
    currency = currency_scraper()
    hit_webhook(currency)
    return jsonify({'EURUSDInsert': currency})

@app.route('/currency', methods=['GET'])
def get_currency():
	data = []
	conn = mariadb.connect(
    user="278874",
    password="Dani2020.",
    host="mysql-testjfpldb.alwaysdata.net",
    database="testjfpldb_scrap")
	cur = conn.cursor() 
	#retrieving information 
	cur.execute("SELECT * FROM scrap order by date desc") 
	for idx, item in enumerate(cur):
		data.append({
			"date": item[1],
			"open": item[2],
			"close": item[3],
			"adj_close": item[4],
			"high": item[5],
			"low": item[6]
		})

	conn.close()
	hit_webhook(data)
	return jsonify({'EURUSDQuery': data})

if __name__ == '__main__':
    app.run(debug=True)