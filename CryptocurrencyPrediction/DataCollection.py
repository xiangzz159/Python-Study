#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/26 9:38

@desc: poloniex 数据抓取

'''

import json
import numpy as np
import os
import pandas as pd
import urllib
import time

ts = {
    '2015': 1420041600,
    '2016': 1451577600,
    '2017': 1483200000,
    '2018': 1514736000,
}
t = 31536000
period = 7200 # 300, 900, 1800, 7200, 14400, and 86400

t1 = time.time()
for key in ts:
    try:
        url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=%d&end=%d&period=%d' % (ts[key], ts[key] + t, period)
        print('URL: %s' % url)
        openUrl = urllib.request.urlopen(url)
        r = openUrl.read()
        d = json.loads(r.decode())
        df = pd.DataFrame(d)

        original_columns = [u'date', u'high', u'low', u'open', u'close', u'volume', u'quoteVolume', u'weightedAverage']
        new_columns = ['Timestamp', 'High', 'Low', 'Open', 'Close', 'Volume', 'QuoteVolume', 'WeighteAverage']
        df = df.loc[:, original_columns]
        df.columns = new_columns
        fileName = './data/bitcoin%sto%s.csv' % (key, str(int(key) + 1))
        df.to_csv(fileName, index=None)
    except BaseException as e:
        print(e)

print(time.time() - t1)
