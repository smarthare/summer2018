#from flask import Flask, request
import requests
#app = Flask(__name__)
apiadd = 'https://api-ssl.bitly.com'
getr = '/v3/nsq/stats?topic=data_stream&access_token=29ec273e0984e4ca984c334fcb563b18ea250653'
url = apiadd + getr
print(url)
url2= 'https://api.coinmarketcap.com/v2/ticker/1/'
res_data = requests.get(url2)
ret = res_data.json()

for i in ret:
	print(ret[i])

"""url = apiadd + getr
@app.route('/', methods=['POST'])
def json_ex():
	req_data = requests.get(url)
	req=req_data.json()
	zep = []
	for i in req:
		zep.append(req[i])
	return str(zep[0])

# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='127.0.0.0', port=port)"""
