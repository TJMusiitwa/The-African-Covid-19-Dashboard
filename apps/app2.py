from navbar import Navbar
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table

df_africa = pd.read_csv('africa_data.csv')

#from app import app
nav = Navbar()

layout = html.Div(
    children=[
        nav,
        html.Div([
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df_africa.columns],
                data=df_africa.to_dict('records'),

            )

        ])
    ])

# @app.callback(
#     Output('app-2-display-value', 'children'),
#     [Input('app-2-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)
