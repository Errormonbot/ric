import numpy as np
from scipy import stats
from numpy.random import randn
N=20
a=5*randn(100)+50
print(a)
b=5*randn(100)+51
print(b)
var_a=a.var(ddof=1)
var_b=b.var(ddof=1)
s=np.sqrt((var_a+var_b)/2)
t=(a.mean() - b.mean())/(s*np.sqrt(2/N))
df=2*N - 2
p=1 - stats.t.cdf(t,df=df)
print("t = " + str(t))
print("p = " + str(2*p))
if t>p :
    print("mean of two distribution are different and significant")
else:
    print("mean of two distribution are same and not significant")
