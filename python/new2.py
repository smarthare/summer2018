import psycopg2
from configcust import config
from flask import Flask
import requests, json

def insertdata(datastream):
	""" insert multiple vendors into the vendors table  """
	sql1 = "INSERT INTO currency(cur_id, cur_name, cur_sym, web_slg, rank, last_updated) VALUES(%s, %s, %s, %s, %s, %s)"
	sql2 = "INSERT INTO supply(cur_id, circulating_supply, total_supply, max_supply) VALUES(%s, %s, %s, %s)"
	sql3 = "INSERT INTO quotes(quote_id,cur_id, quote_name) VALUES(%s, %s, %s)"
	sql4 = "INSERT INTO quote_info(quote_id, cur_id, price, volume, market_cap, percent_change_1h, percent_change_24h, percent_change_7d) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
	conn = None
	sqdata1 = []
	sqdata2 = []
	sqdata3 = []
	sqdata4 = []
	l = len(datastream)
	print(datastream)
	for i in range(l):
		#  0   1   2   3  4   5    6    7     8    9  10  11   12     13    14   15
		#[ids,cur,sym,web,rn,csup,tsup,msup,'USD',prc,vol,mar,per1h,per24h,per7d,lu]
		sqdata1.append((datastream[i][0],datastream[i][1],datastream[i][2],datastream[i][3],datastream[i][4],datastream[i][15]))
		sqdata2.append((datastream[i][0],datastream[i][5],datastream[i][6],datastream[i][7]))
		sqdata3.append((i,datastream[i][0],datastream[i][8]))
		sqdata4.append((i,datastream[i][0],datastream[i][9],datastream[i][10],datastream[i][11],datastream[i][12], datastream[i][13],datastream[i][14]))
	sqdata1 = tuple(sqdata1)
	sqdata2 = tuple(sqdata2)
	sqdata3 = tuple(sqdata3)
	sqdata4 = tuple(sqdata4)
	try:
        # read database configuration
		params = config()
        # connect to the PostgreSQL database
		conn = psycopg2.connect(**params)
        # create a new cursor
		cur = conn.cursor()
        # execute the INSERT statement
		print("1" , sqdata1, sqdata2, sqdata3, sqdata4)
		cur.executemany(sql1,sqdata1)
		print("2")
		cur.executemany(sql2,sqdata2)
		print("3")
		cur.executemany(sql3,sqdata3)
		print("4")
		cur.executemany(sql4,sqdata4)
        # commit the changes to the database
		conn.commit()
        # close communication with the database
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

app = Flask(__name__)
#from flask import Flask, request

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
	rel = res_data
	ret = rel['data']
	ids = ret['id']
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
	insertdata([[ids,cur.encode("utf-8"),sym.encode("utf-8"),web.encode("utf-8"),rn,csup,tsup,msup,'USD',prc,vol,mar,per1h,per24h,per7d,lu]])
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
