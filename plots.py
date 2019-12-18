import plotly
import plotly.graph_objs as graph_objs
import pandas as pd 
import numpy as np 
import json

def generate_plot(group='sepal.length'):
    data = pd.read_csv('./data/iris.csv')
    p = [graph_objs.Bar(x=data[group])]
    graphJson = json.dumps(p, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJson