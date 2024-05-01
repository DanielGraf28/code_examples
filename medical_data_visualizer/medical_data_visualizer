import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data
pd = pd.read_csv('medical_examination.csv')

# create 'overweight' column
pd['overweight'] = (pd['weight'] / (pd['height'] / 100)**2).apply(lambda x: 1 if x > 25 else 0)

# normalize 'cholesterol' and 'gluc' columns
pd['cholesterol'] = pd['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
pd['gluc'] = pd['gluc'].apply(lambda x: 0 if x == 1 else 1)

# draw categorical plot
def draw_cat_plot():
    df_cat = pd.melt(pd, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name= 'total')
    fig = sns.catplot(x= 'variable', y= 'total', hue= 'value', col= 'cardio', data= df_cat, kind= 'bar')
    fig = fig.fig
    fig.savefig('catplot.png')
    return fig

# draw heat map
def draw_heat_map():
    df_heat = pd[(pd['ap_lo'] <= pd['ap_hi']) & (pd['height'] >= pd['height'].quantile(0.025)) & (pd['height'] <= pd['height'].quantile(0.975)) & (pd['weight'] >= pd['weight'].quantile(0.025)) & (pd['weight'] <= pd['weight'].quantile(0.975))]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(11, 9))
    sns.heatmap(corr = corr, mask = mask, annot = True, fmt = '.1f', linewidths = 0.5, center = 0, square = True, cbar_kws = {'shrink': 0.5}, ax = ax)
    fig.savefig('heatmap.png')
    return fig
