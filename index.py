import pandas as pd
import numpy as np

from dash import html, dcc, _dash_renderer
import dash_mantine_components as dmc
_dash_renderer._set_react_version('18.2.0')

# import plotly.express as px
# import plotly.graph_objs as go

from load_data import rent

comp0_graph = dmc.Card(
    [
        dcc.Store(id="comp0_graph_STORE", storage_type="memory"),
        dcc.Graph(figure={}, id="comp0_graph_GOPIE0", className="g")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp0_graph"
)


comp1_dropdown = dmc.Card(
    [
        dmc.CheckboxGroup(
            label="Zoning",
            value=[],
            size="xs",
            children = dmc.Stack([
                dmc.Checkbox(label="FS-RL", value="FS-RL", color="#16C410"),
                dmc.Checkbox(label="F-VR", value="F-VR", color="#16C410")
            ]),
            id="multi_zoning_SELECT0", 
            className="small-sq"
        ),
        dmc.CheckboxGroup(
            label="Style",
            value=[],
            size="xs",
            children = dmc.Stack([
                dmc.Checkbox(label="1-story, 1946 & newer", value="1-STORY 1946 & NEWER ALL STYLES", color="#16C410"),
                dmc.Checkbox(label="2-story, 1946 & newer", value="2-STORY 1946 & NEWER", color="#16C410"),
                dmc.Checkbox(label="1-story townhome, 1946 & newer", value="1-STORY TWNHM - 1946 & NEWER", color="#16C410"),
                dmc.Checkbox(label="2-story townhome, 1946 & newer", value="2-STORY TWNHM - 1946 & NEWER", color="#16C410")

            ]),
            id="multi_classtype_SELECT1", 
            className="small-sq"
        ),
        dmc.CheckboxGroup(
            label="Garage",
            value=[],
            size="xs",
            children = dmc.Stack([
                dmc.Checkbox(label="Unknown/NA", value="Unknown/NA", color="#16C410"),
                dmc.Checkbox(label="Attched", value="Attchd", color="#16C410"),
                dmc.Checkbox(label="Built-in", value="BuiltIn", color="#16C410"),
                dmc.Checkbox(label="Basment", value="Basment", color="#16C410"),
                dmc.Checkbox(label="Two types", value="2Types", color="#16C410")
            ]),
            id="multi_garage_SELECT2", 
            className="small-sq"
        ),
        dmc.CheckboxGroup(
            label="Masonry",
            value=[],
            size="xs",
            children = dmc.Stack([
                dmc.Checkbox(label="Unknown/NA", value="Unknown/NA", color="#16C410"),
                dmc.Checkbox(label="BrkFace", value="BrkFace", color="#16C410"),
                dmc.Checkbox(label="Stone", value="Stone", color="#16C410"),
                dmc.Checkbox(label="BrkCmn", value="BrkCmn", color="#16C410")
            ]),
            id="multi_masonry_SELECT3", 
            className="small-sq"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp1_dropdown big-sq"
)

comp2_title = dmc.Card(
    [
        dmc.Text(
            "Segmentation drilldown: houses worth more than 200k",
            size="xs",
            # c="white",
            fw=800,
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp2_title"
)

comp_01_inline = html.Div(
    [
        comp2_title,
        comp0_graph,
        comp1_dropdown
    ],
    className="in special-inline"
)

block0 = html.Div(
    [
        comp_01_inline
    ],
    className="d"
)

############################### composition ##################################

lyt = dmc.MantineProvider(
    [
        block0
    ]
)