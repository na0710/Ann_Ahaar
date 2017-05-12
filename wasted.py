import pandas as pd
import os 
import numpy as np

columns = ['item_id','wasted','day'];
rates = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wasted2.csv'), sep=',', names=columns, encoding='latin-1');
l = len(rates)

a = np.split(rates,[9,19,25,31,42,52,61])



m1 = np.argmax(np.bincount(a[0].wasted))
m2 = np.argmax(np.bincount(a[1].wasted))
m3 = np.argmax(np.bincount(a[2].wasted))
m4 = np.argmax(np.bincount(a[3].wasted))
m5 = np.argmax(np.bincount(a[4].wasted))
m6 = np.argmax(np.bincount(a[5].wasted))
m7 = np.argmax(np.bincount(a[6].wasted))

n1 = np.amax(a[0])
n2 = np.amax(a[1])
n3 = np.amax(a[2])
n4 = np.amax(a[3])
n5 = np.amax(a[4])
n6 = np.amax(a[5])
n7 = np.amax(a[6])

