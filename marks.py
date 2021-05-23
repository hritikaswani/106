import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    marks = []
    days_present = []
    with open(data_path)as f:
        csv_reader =  csv.DictReader(f)
        for row in csv_reader :
            marks.append(float(row["Marks"]))
            days_present.append(float(row["Days Present"]))
    return{"x":marks,"y":days_present}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Co-Relation Between Marks And Days Present :\n--->",correlation[0,1])

def plotFigure(data_path):
    with open(data_path)as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Marks", y = "Days Present")
        fig.show()

def setup():
    data_path = "marks.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()