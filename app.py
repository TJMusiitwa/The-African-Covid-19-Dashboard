import glob
import io
import re
from datetime import date, timedelta

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import requests
from dash.dependencies import Input, Output
from plotly.offline import init_notebook_mode, iplot

from apps import about, summary, data, regional_trends

init_notebook_mode(connected=True)

flatly_theme = ['assets/bootstrap.min.css', 'assets/bootstrap-grid.min.css']

app = dash.Dash(__name__, external_stylesheets=flatly_theme)

server = app.server

app.config.suppress_callback_exceptions = True
app.title = 'African COVID-19 Dashboard'
app._favicon = 'assets/favicon.ico'

df_africa = pd.read_csv('africa_data.csv')
df_africa['date'] = pd.to_datetime(df_africa['date'])
update = df_africa['date'].dt.strftime('%B %d, %Y').max()


available_countries = sorted(df_africa['Country/Region'].unique())

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)
# Summary Callback


@app.callback(
    Output('confirmed_total', 'figure'),
    [Input('africa_confirmed', 'value')])
def confirmed():
    value = df_africa[df_africa['date'] ==
                      df_africa['date'].iloc[-1]]['Confirmed'].sum()
    delta = df_africa[df_africa['date'] ==
                      df_africa['date'].unique()[-2]]['Confirmed'].sum()
    return{
        'data': [{'type': 'indicator',
                  'mode': 'number+delta',
                  'value': value,
                  'delta': {'reference': delta,
                            'valueformat': '.2%',
                            'relative': True,
                            'font': {'size': 25}},
                  'number': {'valueformat': ',',
                             'font': {'size': 50}},
                  'domain': {'y': [0, 1], 'x': [0, 1]}}],
        'layout': go.Layout(
            title={'text': "CUMULATIVE CONFIRMED"},
        )
    }

# Navigation Callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/summary':
        return summary.summary_layout
    elif pathname == '/apps/data':
        return data.data_layout
    elif pathname == '/apps/regional_trends':
        return regional_trends.trends_layout
    elif pathname == '/apps/about':
        return about.about_layout
    else:
        return summary.summary_layout


# server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
