import plotly
import plotly.graph_objs as go
import pandas as pd 
import numpy as np 
import json

def generate_plot(group='sepal.length'):
    data = pd.read_csv('./data/iris.csv')
    p = go.Figure(data=go.Bar(x=data[group]), 
                layout=go.Layout(title=go.layout.Title(text=group)))
    graphJson = json.dumps(p, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJson