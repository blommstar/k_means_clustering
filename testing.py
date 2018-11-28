import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('blogdata.csv', sep=';')
# df = pd.read_csv('blogdata.csv', sep="\t", quoting=csv.QUOTE_NONE)#, index_col=False)

# Make a copy of DF
df_tr = df

# Transsform the timeOfDay to dummies
df_tr = pd.get_dummies(df_tr, columns=['Blog'])

# Standardize
# clmns = ['Wattage', 'Duration', 'timeOfDay_Afternoon', 'timeOfDay_Evening',
#  'timeOfDay_Morning']
clmns = df.columns.values
df_tr_std = stats.zscore(df_tr[clmns])

# Cluster the data
kmeans = KMeans(n_clusters=2, random_state=0).fit(df_tr_std)
labels = kmeans.labels_

# Glue back to originaal data
df_tr['clusters'] = labels

# Add the column into our list
clmns.extend(['clusters'])

# Lets analyze the clusters
print(df_tr[clmns].groupby(['clusters']).mean())
