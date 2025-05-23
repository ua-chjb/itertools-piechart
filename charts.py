import pandas as pd
import numpy as np
from itertools import *

from dash import html
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import dash_mantine_components as dmc

def onebigpiechart(df):

    vcs_df = df["Price >= 200k"].value_counts()

    color_map = {
        "Under 200k": "#F3F3F3",
        "Over 200k": "#EA00FF",
    }

    # pull_map = {
    #     "Under 200k": 0,
    #     "Over 200k": 0.1,
    # }

    colors = [color_map[row] for row in vcs_df.index]
    # pulls = [pull_map[row] for row in vcs_df.index]

    fig = go.Figure(
        go.Pie(
            labels=vcs_df.index,
            values=vcs_df.values,
            marker={
                "colors": colors, 
                "line": {
                    "width": 1, 
                    "color": "black"
                }
            },
            hole=0.3,
            # pull=pulls
        )
    )

    fig.add_annotation(
        text=len(df),
        xref="paper",
        yref="paper",
        x=0.5, y=0.5,
        showarrow=False
    )

    fig.update_layout({
        "legend": {
            "orientation": "h",
            "yanchor": "top",
            "y":0,
            "xanchor":"center",
            "x": 0.5
        }
    })

    return fig.update_layout({
        "margin": {"t": 0, "b": 0, "r": 0, "l": 0},
    })
