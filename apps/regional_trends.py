import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from navbar import Navbar

nav = Navbar()

df_africa = pd.read_csv('africa_data.csv')
df_africa['date'] = pd.to_datetime(df_africa['date'])

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

# Central African Region
caActive_fig = go.Figure()
for country in ca:
    caActive_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

caActive_fig.update_layout(title="Active COVID-19 cases in Central Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")
#
caConfirmed_fig = go.Figure()
for country in ca:
    caConfirmed_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Confirmed'].sum(),
        name=country,
        opacity=0.8))

caConfirmed_fig.update_layout(title="Confirmed COVID-19 cases in Central Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")
#
caRecovered_fig = go.Figure()
for country in ca:
    caRecovered_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Recovered'].sum(),
        name=country,
        opacity=0.8))

caRecovered_fig.update_layout(title="Recovered COVID-19 cases in Central Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")

#
caDeaths_fig = go.Figure()
for country in ca:
    caDeaths_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Deaths'].sum(),
        name=country,
        opacity=0.8))

caDeaths_fig.update_layout(title="Death COVID-19 cases in Central Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")


# West African Region
waActive_fig = go.Figure()
for country in wa:
    waActive_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

waActive_fig.update_layout(title="Active COVID-19 cases in Western Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")
#
waConfirmed_fig = go.Figure()
for country in wa:
    waConfirmed_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Confirmed'].sum(),
        name=country,
        opacity=0.8))

waConfirmed_fig.update_layout(title="Confirmed COVID-19 cases in Western Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")
#
waRecovered_fig = go.Figure()
for country in wa:
    waRecovered_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Recovered'].sum(),
        name=country,
        opacity=0.8))

waRecovered_fig.update_layout(title="Recovered COVID-19 cases in Western Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")

#
waDeaths_fig = go.Figure()
for country in wa:
    waDeaths_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Deaths'].sum(),
        name=country,
        opacity=0.8))

waDeaths_fig.update_layout(title="Death COVID-19 cases in Western Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")


# East African Region
eaActive_fig = go.Figure()
for country in ea:
    eaActive_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

eaActive_fig.update_layout(title="Active COVID-19 cases in Eastern Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")
#
eaConfirmed_fig = go.Figure()
for country in ea:
    eaConfirmed_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Confirmed'].sum(),
        name=country,
        opacity=0.8))

eaConfirmed_fig.update_layout(title="Confirmed COVID-19 cases in Eastern Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")
#
eaRecovered_fig = go.Figure()
for country in ea:
    eaRecovered_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Recovered'].sum(),
        name=country,
        opacity=0.8))

eaRecovered_fig.update_layout(title="Recovered COVID-19 cases in Eastern Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")

#
eaDeaths_fig = go.Figure()
for country in ea:
    eaDeaths_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Deaths'].sum(),
        name=country,
        opacity=0.8))

eaDeaths_fig.update_layout(title="Death COVID-19 cases in Eastern Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")


# North African Region
naActive_fig = go.Figure()
for country in na:
    naActive_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

naActive_fig.update_layout(title="Active COVID-19 cases in Northern Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")
#
naConfirmed_fig = go.Figure()
for country in na:
    naConfirmed_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Confirmed'].sum(),
        name=country,
        opacity=0.8))

naConfirmed_fig.update_layout(title="Confirmed COVID-19 cases in Northern Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")
#
naRecovered_fig = go.Figure()
for country in na:
    naRecovered_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Recovered'].sum(),
        name=country,
        opacity=0.8))

naRecovered_fig.update_layout(title="Recovered COVID-19 cases in Northern Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")

#
naDeaths_fig = go.Figure()
for country in na:
    naDeaths_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Deaths'].sum(),
        name=country,
        opacity=0.8))

naDeaths_fig.update_layout(title="Death COVID-19 cases in Northern Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")

# South African Region
saActive_fig = go.Figure()
for country in sa:
    saActive_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Active'].sum(),
        name=country,
        opacity=0.8))

saActive_fig.update_layout(title="Active COVID-19 cases in Southern Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")
#
saConfirmed_fig = go.Figure()
for country in sa:
    saConfirmed_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Confirmed'].sum(),
        name=country,
        opacity=0.8))

saConfirmed_fig.update_layout(title="Confirmed COVID-19 cases in Southern Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")
#
saRecovered_fig = go.Figure()
for country in sa:
    saRecovered_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Recovered'].sum(),
        name=country,
        opacity=0.8))

saRecovered_fig.update_layout(title="Recovered COVID-19 cases in Southern Africa",
                              xaxis_title="Date",
                              yaxis_title="Number of Individuals")

#
saDeaths_fig = go.Figure()
for country in sa:
    saDeaths_fig.add_trace(go.Scatter(
        x=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['date'].first(),
        y=df_africa[df_africa['Country/Region'] ==
                    country].groupby('date')['Deaths'].sum(),
        name=country,
        opacity=0.8))

saDeaths_fig.update_layout(title="Death COVID-19 cases in Southern Africa",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")

trends_layout = html.Div([
    nav,
    dbc.Alert(
        [
            "The regions shown below have been apportioned according to the United Nations geoscheme. ",
            html.A("More information here.",
                   href="https://en.wikipedia.org/wiki/United_Nations_geoscheme", className="alert-link"),
        ],
        # color="info",
        dismissable=True,
        fade=True,
        is_open=True,
        className='alert alert-dismissible alert-info'
    ),
    dbc.Container(
        dcc.Tabs([
            dcc.Tab(label='East Africa', children=[
                dbc.Container(
                    fluid=True,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=eaConfirmed_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=eaActive_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=eaActive_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=eaDeaths_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                    ],
                ),
            ],

            ),
            # West Africa
            dcc.Tab(label='West Africa', children=[
                dbc.Container(
                    fluid=True,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=waConfirmed_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=waActive_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=waRecovered_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=waDeaths_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                    ],
                ),
            ],

            ),

            # Central Africa
            dcc.Tab(label='Central Africa', children=[
                dbc.Container(
                    fluid=True,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=caConfirmed_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=caActive_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=caRecovered_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=caDeaths_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                    ],
                ),
            ],
            ),

            # South Africa
            dcc.Tab(label='South Africa',
                    children=[
                        dbc.Container(
                            fluid=True,
                            children=[
                                dbc.Row(
                                    [
                                        dbc.Col(dcc.Graph(
                                            figure=saConfirmed_fig,
                                            responsive=True,
                                        )),
                                        dbc.Col(dcc.Graph(
                                            figure=saActive_fig,
                                            responsive=True,
                                        )),
                                    ]
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(dcc.Graph(
                                            figure=saRecovered_fig,
                                            responsive=True,
                                        )),
                                        dbc.Col(dcc.Graph(
                                            figure=saDeaths_fig,
                                            responsive=True,
                                        )),

                                    ]
                                ),
                            ],
                        ),
                    ],

                    ),
            # North Africa
            dcc.Tab(label='North Africa', children=[
                dbc.Container(
                    fluid=True,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=naConfirmed_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=naActive_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(
                                    figure=naRecovered_fig,
                                    responsive=True,
                                )),
                                dbc.Col(dcc.Graph(
                                    figure=naDeaths_fig,
                                    responsive=True,
                                )),

                            ]
                        ),
                    ],
                ),
            ],
            ),
        ],
        ),
    )
])
