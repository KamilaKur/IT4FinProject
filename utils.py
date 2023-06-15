import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

def plot_candles(df, part=0.001):
    
    length = int(df.shape[0] * part)
    
    df = df.iloc[:length, :]
    
    fig = go.Figure(data=[go.Candlestick(x=df['period'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])
    fig.show()