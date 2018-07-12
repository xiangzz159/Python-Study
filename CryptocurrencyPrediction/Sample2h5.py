#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/26 13:37

@desc:

'''

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from CryptocurrencyPrediction.PastSampler import PastSampler
import numpy as np

dfp = './data/bitcoin2017to2018.csv'

columns = ['Close']
df = pd.read_csv(dfp)
time_stamps = df['Timestamp']
df = df.loc[:,columns]
original_df = pd.read_csv(dfp).loc[:,columns]

file_name = 'bitcoin2015to2016_close.h5'

scaler = MinMaxScaler()
for c in columns:
    df[c] = scaler.fit_transform(df[c].values.reshape(-1, 1))

A = np.array(df)[:, None, :]
original_A = np.array(original_df)[:, None, :]
time_stamps = np.array(time_stamps)[:, None, None]

NPS, NFS = 256, 16
ps = PastSampler(NPS, NFS, False)
B, Y = ps.transform(A)
input_times, output_times = ps.transform(time_stamps)
original_B, original_Y = ps.transform(original_A)

import h5py
with h5py.File(file_name, 'w') as f:
    f.create_dataset("inputs", data = B)
    f.create_dataset('outputs', data = Y)
    f.create_dataset("input_times", data = input_times)
    f.create_dataset('output_times', data = output_times)
    f.create_dataset("original_datas", data=np.array(original_df))
    f.create_dataset('original_inputs',data=original_B)
    f.create_dataset('original_outputs',data=original_Y)
