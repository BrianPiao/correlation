import plotly.express as p
import csv as c
import numpy as np

def getDataSource(data_path):
     Percent = []
     Present = []
     with open(data_path) as c_file:
        c_reader = c.DictReader(c_file)
        for row in c_reader:
            Percent.append(float(row["Marks In Percentage"]))
            Present.append(float(row["Days Present"]))
     return {"x" : Percent, "y": Present}

def findCorr(ds):
    c = np.corrcoef(ds["x"], ds["y"])
    print ("Student Marks vs Days Present : ", c[0,1])
     
def setup():
    data_path  = "Student Marks vs Days Present.csv"
    ds = getDataSource(data_path)
    findCorr(ds)

setup()

#correlation = 1 correctly collerated (more than 1)