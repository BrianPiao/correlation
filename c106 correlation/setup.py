import plotly.express as p
import csv as c
import numpy as np

def getDataSource(data_path):
     temp = []
     ice_cream_sales = []
     with open(data_path) as c_file:
        c_reader = c.DictReader(c_file)
        for row in c_reader:
            temp.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales( ₹ )"]))
     return {"x" : temp, "y": ice_cream_sales}

def findCorrelation(datasource):
     correlation = np.corrcoef(datasource["x"], datasource["y"])
     print("\n Correlation between Temperature vs Ice Cream Sales :  \t",correlation[0,1])


def setup():
    data_path  = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

#correlation = 1 closely collerated (greater than 0)