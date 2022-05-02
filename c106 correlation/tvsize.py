import plotly.express as p
import csv as c
import numpy as np

def getDataSource(data_path):
     time = []
     tvsize = []
     with open(data_path) as c_file:
        c_reader = c.DictReader(c_file)
        for row in c_reader:
            time.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
            tvsize.append(float(row["Size of TV"]))
     return {"x" : tvsize, "y": time}

def findCorrelation(datasource):
     correlation = np.corrcoef(datasource["x"], datasource["y"])
     print("\n Correlation between TV size vs Hours spent :  \t",correlation[0,1])


def setup():
    data_path  = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

#correlation = 0 not collerated (equal to 0)