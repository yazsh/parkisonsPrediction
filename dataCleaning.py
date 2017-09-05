import pandas as pd
import csv

data = pd.read_csv("/Users/yazen/Desktop/datasets/ParkinsonsData/Drinking_all_export.txt", chunksize=1000, iterator=True, nrows=5)

for chunk in data:
    print(chunk)
