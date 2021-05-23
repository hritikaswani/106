import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path)as f:
        csv_reader =  csv.DictReader(f)
        for row in csv_reader :
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["Sleep"]))
    return{"x":coffee,"y":sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Co-Relation Between Drinking Coffee And Sleep :\n--->",correlation[0,1])

def plotFigure(data_path):
    with open(data_path)as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Coffee", y = "Sleep")
        fig.show()

def setup():
    data_path = "coffee.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()