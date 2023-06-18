import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
from hurst import compute_Hc

def momentum(df, window=1000):
    df['mean'] = df['profit'].rolling(window).mean()
    df['momentum'] = df['mean'].apply(lambda x: 'long' if x > 0 else 'short' if x < 0 else 'nothing')
    df = df.drop(['mean'], axis=1)
    return df

def mean_reversion(df, window=1000):
    df['mean'] = df['profit'].rolling(window).mean()
    df['mean_reversion'] = df['mean'].apply(lambda x: 'short' if x > 0 else 'long' if x < 0 else 'nothing')
    df = df.drop(['mean'], axis=1)
    return df

def HurstEXP(ts, window=1000):
    H, _, _ = compute_Hc(ts, min_window=window, max_window=window)
    return H

def hurst_rule(df, window=1000):
    df['H'] = df['profit'].rolling(window).apply(lambda x: HurstEXP(x))
    df['hurst_rule'] = df.apply(lambda x: x.momentum if x.H > 0.5 else x.mean_reversion if x.H < 0.5 else 'nothing', axis=1)
    df = df.drop(['H'], axis=1)
    return df

def count_cumsum(df):
    fun = lambda x: 0 if x == 'nothing' else 1 if x == 'long' else -1    
    df['str_momentum'] = df['momentum'].apply(fun)
    df['str_reversion'] = df['mean_reversion'].apply(fun)
    df['str_hurst'] = df['hurst_rule'].apply(fun)
    
    df['delta_momentum'] = df.apply(lambda x: x.profit * x.str_momentum, axis=1)
    df['delta_reversion'] = df.apply(lambda x: x.profit * x.str_reversion, axis=1)
    df['delta_hurst'] = df.apply(lambda x: x.profit * x.str_hurst, axis=1)
    
    df['cumsum_momentum'] = df['delta_momentum'].cumsum()
    df['cumsum_reversion'] = df['delta_reversion'].cumsum()
    df['cumsum_hurst'] = df['delta_hurst'].cumsum()
    
    df['cumsum_hold'] = df['profit'].cumsum()
    
    return df

def plot_all(df, *lst):
    lst[0]
    ax = df.plot(x='period', y='cumsum_'+lst[0], label=lst[0])
    for el in lst[1:]:
        df.plot(x='period', y='cumsum_'+el, ax=ax, label=el)
    plt.legend()
    plt.xticks(rotation=30)
    plt.show()