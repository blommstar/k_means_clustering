
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("blogdata2.txt", sep="\t")
df.fillna(df.mean(), inplace=True)


X = np.array(df.drop(['Blog'], 1).astype(float))
y = np.array(df['Blog'])

kmeans = KMeans(n_clusters=5, max_iter=600, algorithm = 'auto')

kmeans.fit(X)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))

