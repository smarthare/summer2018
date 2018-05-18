from flask import Flask
app = Flask(__name__)
#from flask import Flask, request
import requests, json
#app = Flask(__name__)
apiadd = 'https://api-ssl.bitly.com'
getr = '/v3/nsq/stats?topic=data_stream&access_token=29ec273e0984e4ca984c334fcb563b18ea250653'
url = apiadd + getr
print(url)
url2= 'https://api.coinmarketcap.com/v2/ticker/1/'

@app.route("/")
def display():
	res_data = requests.get(url2)
	res_data = res_data.json()
	return json.dumps(res_data)
"""
	rel = res_data.json()
	ret = rel['data']
	cur = ret['name']
	sym = ret['symbol']
	web = ret['website_slug']
	rn = ret['rank']
	csup = ret['circulating_supply']
	tsup = ret['total_supply']
	msup = ret['max_supply']
	quot = ret['quotes']
	usd = quot['USD']
	prc = usd['price']
	vol = usd['volume_24h']
	mar = usd['market_cap']
	per1h = usd['percent_change_1h']
	per24h = usd['percent_change_24h']
	per7d = usd['percent_change_7d']
	lu = ret['last_updated']
	#for i in ret:
	#	print(ret[i])
	return '''
           
		\nName of currency: {}
		\nSymbol: {}
		\nWebsite slug: {}
		\nRank: {}
		\nCirculating Supply: {}
		\nTotal Supply: {}
		\nMax Supply: {}
		\nQuotes:
		\n	{} :
		\n		Price: {}
		\n		Volume in 24h: {}
		\n		Market Cap: {}
		\n		Percent Change in 1 hr: {}
		\n		Percentage Change in 24 hr: {}
		\n		Percentage Change in 7 days: {}
		\nLast Updated: {}'''.format(cur,sym,web,rn,csup,tsup,msup,'USD',prc,vol,mar,per1h,per24h,per7d,lu)
"""
