import pandas as pd
import csv

stats = pd.read_csv("stats.csv")

stats.drop(['Name', 'Pos'], axis=1, inplace=True)

stats = stats.corr()
stats.to_csv("statsCM.csv")
