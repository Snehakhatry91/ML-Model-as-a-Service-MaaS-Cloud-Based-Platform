import numpy as np
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
def preprocess(data:list):
    arr=np.array(data).reshape(1,-1)
    return scaler.fit_transform(arr)[0]
