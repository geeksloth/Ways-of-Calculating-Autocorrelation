import numpy as np
from dataset import data

x = np.array(data) 

# Mean
mean = np.mean(data)

# Variance
var = np.var(data)

# Normalized data
ndata = data - mean

acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
acorr = acorr / var / len(ndata)

print(acorr)