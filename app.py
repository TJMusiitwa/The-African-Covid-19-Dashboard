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

from apps import about, app1, app2

init_notebook_mode(connected=True)

flatly_theme = ['assets/bootstrap.min.css', 'assets/bootstrap-grid.min.css']

app = dash.Dash(__name__, external_stylesheets=flatly_theme)

# server = app.server

app.config.suppress_callback_exceptions = True
app.title = 'African COVID-19 Dashboard'
app._favicon = 'assets/favicon.ico'

df_africa = pd.read_csv('africa_data.csv')
df_africa['date'] = pd.to_datetime(df_africa['date'])
update = df_africa['date'].dt.strftime('%B %d, %Y').max()


available_countries = sorted(df_africa['Country/Region'].unique())
# Outline the specific regions of the African continent
ea = ['Burundi',
      'Comoros',
      'Djibouti',
      'Eritrea',
      'Ethiopia',
      'Kenya',
      'Madagascar',
      'Malawi',
      'Mauritius',
      'Mozambique',
      'Rwanda',
      'Seychelles',
      'Somalia',
      'South Sudan',
      'Tanzania',
      'Uganda',
      'Zambia',
      'Zimbabwe']
na = ['Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia', 'Sudan']
wa = [
    'Benin',
    'Burkina Faso',
    'Cabo Verde',
    '''Côte d'Ivoire''',
    'Gambia',
    'Ghana',
    'Guinea',
    'Guinea-Bissau',
    'Liberia',
    'Mali',
    'Mauritania',
    'Niger',
    'Nigeria',
    'Senegal',
    'Sierra Leone',
    'Togo'
]
ca = ['Cameroon',
      'Central African Republic',
      'Chad',
      'Congo (Brazzaville)',
      'Angola',
      'Equatorial Guinea',
      'Gabon',
      'Sao Tome and Príncipe',
      'Congo (Kinshasa)',
      'Republic of the Congo', ]
sa = ['Botswana',
      'Eswatini',
      'Lesotho',
      'Namibia',
      'South Africa']

region_options = {'East Africa': ea, 'West Afica': wa,
                  'Southern Africa': sa, 'North Africa': na, 'Central Africa': ca}


# df_ea = pd.read_csv('df_ea.csv')
# df_wa = pd.read_csv('df_wa.csv')
# df_na = pd.read_csv('df_na.csv')
# df_sa = pd.read_csv('df_sa.csv')
# df_ca = pd.read_csv('df_ca.csv')


app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)
# App1 Callback


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
    if pathname == '/apps/app1':
        return app1.app1_layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/about':
        return about.about_layout
    else:
        return app1.app1_layout


# server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
