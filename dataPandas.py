import pandas as pd
import numpy
import csv

df = pd.read_csv('blogdata.txt', sep="\t", quoting=csv.QUOTE_NONE)
print(df)



#print("Total rows: {0}".format(len(data)))

# See which headers are available
#print(list(data))