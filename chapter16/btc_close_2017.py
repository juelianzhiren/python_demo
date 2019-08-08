from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
	#Python 2.x 版本
	from urllib2 import urlopen
except ImportError:
	#Python 3.x 版本
	from urllib.request import urlopen
import json

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response = urlopen(json_url)
#读取数据
req = response.read()
#将数据写入文件
with open("btc_close_2017_urllib.json", "wb") as f:
	f.write(req)
	
#加载json格式
file_urllib = json.loads(req)

filename="btc_close_2017_urllib.json"
with open(filename) as f:
	btc_data=json.load(f)
	
for btc_dict in btc_data:
	date=btc_dict["date"]
	month=int(btc_dict["month"])
	week=int(btc_dict["week"])
	weekday=btc_dict["weekday"]
	close=int(float(btc_dict["close"]))
	print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))
