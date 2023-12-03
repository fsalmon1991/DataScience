import numpy as np
import scipy as scp
from scipy import fft
import pprint
import pandas as pd
import geopandas
# Reading the dataset
df = pd.read_csv('/Users/franciscosalmonmoret/Documents/Study/DataScience/NDMaI_1990_1994.csv')

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


#Making a new dataframe for the data isolated from the geodata in the original dataframe by deleting the geometry column
df_data = df.drop(columns=["geometry"],axis=1)
rowlist = df_data.values.tolist()
row_full_size = len(rowlist)
fft_result_dir = {}
for data in rowlist:
    print("This is the amount of  data at the beginning in the rows = " + str(len(data)))
    clean_data = dltinvalid(-10,data)
    row_clean_size = len(clean_data)
    print("This is the amount of  data after being cleaned in the rows = " + str(row_clean_size))
    fftout = fft.fft(clean_data)
    data_with_sizes = len(data),row_clean_size,np.abs(fftout),fft.fftfreq(len(data))
    fft_result_dir[tuple(geom_list[rowlist.index(data)])] = data_with_sizes

pprint.pprint(fft_result_dir)
