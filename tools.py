import numpy as np
import scipy as scp
from scipy import fft
import pprint
import pandas as pd
import geopandas
# Reading the dataset
df = pd.read_csv('/Users/franciscosalmonmoret/Documents/Study/DataScience/NDMaI_1990_1994.csv')
rows = int(df.shape[0]/2)
print(rows)
df = df.iloc[:rows,:]

# Making a new dataframe for the geodata
df_geom = df[["geometry"]].copy()
geom_list = df_geom.values.tolist()
print(geom_list[0])
clean_data = []

def dltinvalid(value,data):
    clean_data = []
    for elements in data:
        if elements != -10:
            clean_data.append(elements)
    return clean_data  

def orderArraybyOIndex(arrayA,arrayB):
    
    listaA = arrayA.tolist()
    listaB = arrayB.tolist()
    lista_index = []
    for elements in listaA:
        lista_index.append((elements, listaA.index(elements)))
    sortedA = np.sort(arrayA)[::-1]
    result = []
    for data in sortedA:
        for value in lista_index:
            if data == value[0]:
                result.append((data, listaB[value[1]]))   
    return result
#Making a new dataframe for the data isolated from the geodata in the original dataframe by deleting the geometry column
df_data = df.drop(columns=["geometry"],axis=1)
# Splitting in two half the data frame and working the first half because the tow half are equals
rowlist = df_data.values.tolist()


row_full_size = len(rowlist)
fft_result_dir = {}
for data in rowlist:
    print("This is the amount of  data at the beginning in the rows = " + str(len(data)))
    clean_data = dltinvalid(-10,data)
    row_clean_size = len(clean_data)
    print("This is the amount of  data after being cleaned in the rows = " + str(row_clean_size))
    fftout = fft.fft(clean_data)
    data_with_sizes = len(data),row_clean_size,orderArraybyOIndex(fft.fftfreq(len(clean_data)),np.abs(fftout))
    fft_result_dir[tuple(geom_list[rowlist.index(data)])] = data_with_sizes
    
#sortedDict = sorted(fft_result_dir.items(), key=lambda x:x[1])
pprint.pprint(fft_result_dir)
