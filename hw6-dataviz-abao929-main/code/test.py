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
import plotly.graph_objs as go
from plotly.offline import iplot

#What is the total number of traffic stops through from 2005 - 2015 per each county?
df = pd.read_csv('../data/ri_traffic_stops.csv', delimiter=',')
county_count = get_value_counts_table(df, 'county_fips')
fips = county_count['county_fips']
fips_dict = {'44007': 'ABC', '44003': 'DEF', '44009': 'GHI', '44005': 'JKL', '44001': 'MNO'}
colors = ['greenyellow', 'lime', 'limegreen', 'forestgreen', 'darkgreen']
plotly_data_dict = {
    # letting Plotly know that we're plotting a choropleth graph,
    "type": "choropleth",
    # saying that we're plotting the graph of the US only
    "locationmode": "USA-states",
    # getting the list of locations that we're plotting to Plotly
    "locations": county_count["county_fips"],
    # getting the value associated with each location
    "z": county_count["count"],
    # and choosing a color scheme for our map! We'll use "algae" for now to match
    # up with Starbucks theme!
    "colorscale": "algae",
    # and then we'll get a color bar to the side to explain the gradient
    # of the red colors in our graph (see the example photo above)
    "colorbar": {
        "title": "Stops Count"
    }
}
plotly_layout_dict = {
    # Communicating the title of the graph
    "title": "Stops by County in RI",
    "geo": {
        # Communicating that the scope is in the US
        "scope": "usa",
        # and that we want to show the latitude and longtitude grid
        "lataxis_showgrid": True,
        "lonaxis_showgrid": True,
    }
}
choropleth_map = go.Figure(layout=plotly_layout_dict,
                           data=[plotly_data_dict])
plot(choropleth_map)