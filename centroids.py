import dataPandas
import random

centroids = list()

print(dataPandas.df[dataPandas.df.columns[2]])

for word in dataPandas.df:
    centroids.append(word)
    dataPandas.df
    # print(random(min(dataPandas.df[word]),  max(dataPandas.df[word])))
    #for mentions in dataPandas.df[word]:
        #print(mentions)



#ran = random.randint(min(dataPandas.df[word]),  max(dataPandas.df[word]))


#get random number based om mentions (min-max)

print(centroids)