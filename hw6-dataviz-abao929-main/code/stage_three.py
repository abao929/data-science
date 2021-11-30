from utils import *
import random
import numpy as np
import pandas as pd

# import matplotlib - very important
import matplotlib.pyplot as plt

# import the toolkit for plotting matplotlib 3D
from mpl_toolkits import mplot3d

# import the stuff for geographic plots
import plotly.figure_factory as ff

#What is the total number of traffic stops through from 2005 - 2015 per each county?
df = pd.read_csv('../data/ri_traffic_stops.csv', delimiter=',')
county_count = get_value_counts_table(df, 'county_fips')
fips = county_count['county_fips']
fips_dict = {'44007': 'ABC', '44003': 'DEF', '44009': 'GHI', '44005': 'JKL', '44001': 'MNO'}
colors = ['greenyellow', 'lime', 'limegreen', 'forestgreen', 'darkgreen']
fig = ff.create_choropleth(fips=fips,\
                            values=county_count['count'],\
                            scope=['RI'],\
                            title='RI Counties',\
                            colorscale=colors,\
                            show_hover=True,\
                            #centroid_marker=fips_dict,\
                            legend_title='Stops by County')
fig.layout.template = None

fig.show()
