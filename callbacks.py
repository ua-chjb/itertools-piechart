from dash import Input, Output, State, exceptions
from functools import reduce

from load_data import rent
from charts import onebigpiechart



def apply_single_filter(df, key, val):
    return df[df[key].isin(val)]

def apply_multiple_features(filter_dct):
    df_filtered = reduce(
        lambda df, item: apply_single_filter(df, *item),
        list(filter_dct.items()),
        rent.copy()
    )
    return df_filtered



def callbacks_center(app):
    @app.callback(
        Output("comp0_graph_STORE", "data"),
        Input("multi_zoning_SELECT0", "value"),
        Input("multi_classtype_SELECT1", "value"),
        Input("multi_garage_SELECT2", "value"),
        Input("multi_masonry_SELECT3", "value"),
        prevent_initial_call=True
    )
    def xwing(zoning_lst, classtype_lst, garage_lst, masonry_lst):
        filters = {}

        if zoning_lst:
            filters["ZngCdPr"] = zoning_lst
        
        if classtype_lst:
            filters["ClassSc_S"] = classtype_lst

        if garage_lst:
            filters["GarageType"] = garage_lst

        if masonry_lst:
            filters["MasVnrType"] = masonry_lst

        return filters
    @app.callback(
        Output("comp0_graph_GOPIE0", "figure"),
        Input("comp0_graph_STORE", "data")
    )
    def r2d2(filter_dct):
        if not filter_dct:
            df_filtered = rent
        else:
            df_filtered = apply_multiple_features(filter_dct)
        
        return onebigpiechart(df_filtered)