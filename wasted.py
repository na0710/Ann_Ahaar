import pandas as pd
import os 
import numpy as np
from operator import itemgetter
columns = ['item_id','wasted','day'];
rates = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wasted2.csv'), sep=',', names=columns, encoding='latin-1');

a = np.split(rates,[9,19,25,31,42,52,61])

m1 = np.argmax(np.bincount(a[0].item_id))
m2 = np.argmax(np.bincount(a[1].item_id))
m3 = np.argmax(np.bincount(a[2].item_id))
m4 = np.argmax(np.bincount(a[3].item_id))
m5 = np.argmax(np.bincount(a[4].item_id))
m6 = np.argmax(np.bincount(a[5].item_id))
m7 = np.argmax(np.bincount(a[6].item_id))

m = [m1,m2,m3,m4,m5,m6,m7]
m_max = np.argmax(np.bincount(m))

a[0] = np.array(a[0])
a[1] = np.array(a[1])
a[2] = np.array(a[2])
a[3] = np.array(a[3])
a[4] = np.array(a[4])
a[5] = np.array(a[5])
n1 = sorted(a[0],key=itemgetter(1),reverse = True)[0][0]
n2 = sorted(a[1],key=itemgetter(1),reverse = True)[0][0]
n3 = sorted(a[2],key=itemgetter(1),reverse = True)[0][0]
n4 = sorted(a[3],key=itemgetter(1),reverse = True)[0][0]
n5 = sorted(a[4],key=itemgetter(1),reverse = True)[0][0]
n6 = sorted(a[5],key=itemgetter(1),reverse = True)[0][0]

k1 = sorted(a[0],key=itemgetter(1),reverse = True)[0][1]
k2 = sorted(a[1],key=itemgetter(1),reverse = True)[0][1]
k3 = sorted(a[2],key=itemgetter(1),reverse = True)[0][1]
k4 = sorted(a[3],key=itemgetter(1),reverse = True)[0][1]
k5 = sorted(a[4],key=itemgetter(1),reverse = True)[0][1]
k6 = sorted(a[5],key=itemgetter(1),reverse = True)[0][1]

n = [n1,n2,n3,n4,n5,n6]
k = [k1,k2,k3,k4,k5,k6]

wasted_array = np.column_stack((n,k))

n_max = sorted(wasted_array,key=itemgetter(1),reverse = True)[0][0]
print(n_max)
print(m_max)