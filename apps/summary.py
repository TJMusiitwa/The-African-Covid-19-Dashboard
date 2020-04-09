import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
from plotly.subplots import make_subplots

#from app import app
from navbar import Navbar

nav = Navbar()

df_africa = pd.read_csv('africa_data.csv')
df_africa['date'] = pd.to_datetime(df_africa['date'])

value = df_africa[df_africa['date'] ==
                  df_africa['date'].iloc[-1]]['Confirmed'].sum()
delta = df_africa[df_africa['date'] ==
                  df_africa['date'].unique()[-2]]['Confirmed'].sum()

active_value = df_africa[df_africa['date'] ==
                         df_africa['date'].iloc[-1]]['Active'].sum()
active_delta = df_africa[df_africa['date'] ==
                         df_africa['date'].unique()[-2]]['Active'].sum()


recovered_value = df_africa[df_africa['date'] ==
                            df_africa['date'].iloc[-1]]['Recovered'].sum()
recovered_delta = df_africa[df_africa['date'] ==
                            df_africa['date'].unique()[-2]]['Recovered'].sum()


deaths_value = df_africa[df_africa['date'] ==
                         df_africa['date'].iloc[-1]]['Deaths'].sum()
deaths_delta = df_africa[df_africa['date'] ==
                         df_africa['date'].unique()[-2]]['Deaths'].sum()

map_data = df_africa[df_africa['date'] == df_africa['date'].iloc[-1]].groupby('Country/Region').agg(
    {'Active': 'sum', 'Longitude': 'mean', 'Latitude': 'mean', 'Country/Region': 'first'})

# Initialize figure with subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=['Number of active cases by African countries', '', ''],
    column_widths=[0.6, 0.4],
    row_heights=[0.4, 0.6],
    specs=[[{"type": "scattergeo", "rowspan": 2}, {"type": "bar"}],
           [None, {"type": "scatter"}]])

# Add scattergeo globe map of active corona locations
fig.add_trace(
    go.Scattergeo(
        lon=map_data['Longitude'],
        lat=map_data['Latitude'],
        text=map_data['Country/Region'] + ': ' +
        map_data['Active'].astype(str),
        mode='markers',
        showlegend=False,
        marker_size=(100 * map_data['Active'] / map_data['Active'].max()),
        marker=dict(reversescale=False,
                    autocolorscale=False,
                    symbol='circle',
                    line=dict(width=1, color='rgba(102, 102, 102)'),
                    colorscale='Reds',
                    cmin=0,
                    color=map_data['Active'],
                    cmax=map_data['Active'].max(),
                    colorbar_title="Active Cases")),
    row=1, col=1
)

# Add locations bar chart
fig.add_trace(
    go.Bar(x=df_africa['date'], y=df_africa['Confirmed'],
           marker=dict(color="crimson"), showlegend=False),
    row=1, col=2
)

# Add 3d surface of volcano
fig.add_trace(
    go.Scatter(),
    row=2, col=2
)

# Update geo subplot properties
fig.update_geos(
    scope='africa',
    showcountries=True,
    showsubunits=True,
    showland=True,
    projection_type="natural earth",
    landcolor="rgb(100, 125, 100)",
    oceancolor="MidnightBlue",
    showocean=True,
    lakecolor="LightBlue",
)

# Set theme, margin, and annotation in layout
fig.update_layout(
    margin=dict(r=10, t=25, b=40, l=60),
)

# fig.show()

summary_layout = html.Div([
    # Disclaimer Alert
    dbc.Alert(
        [
            html.H4("Disclaimer!", className="alert-heading"),
            html.P(
                "The information provided from this dashboard is in no way endorsed by the respective Government Agencies of the African countries displayed here. The predictions potrayed from this dashboard are only theoretical and should be taken as just a theory and more data and better predictions can be applied to come up with better data",
                className="mb-0"
            ),
        ],
        id="disclaimer-alert",
        dismissable=True,
        is_open=True,
        duration=10000,
        className='alert alert-dismissible alert-warning'
    ),
    nav,
    html.Br(),
    # html.Div(children='Data last updated {} at 5pm Pacific time'.format(update), style={
    #     'textAlign': 'center',
    # }),
    html.Div([
        # The statistic Cards
        dbc.Container(
            children=dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Graph(figure={
                                    'data': [{'type': 'indicator',
                                              'mode': 'number+delta',
                                              'value': value,
                                              'delta': {'reference': delta,
                                                        'valueformat': '.2%',
                                                        'relative': True,
                                                        'font': {'size': 25}},
                                              'number': {'valueformat': ',',
                                                         'font': {'size': 50, 'color': 'white'}},
                                              'domain': {'y': [0, 1], 'x': [0, 1]}}],
                                    'layout': {
                                        'title': 'Total Confirmed Cases',
                                        'height': 150,
                                        'paper_bgcolor': 'rgba(0,0,0,0)',
                                        'plot_bgcolor': 'rgba(0,0,0,0)',
                                        'autosize': True,
                                        'font': {'color': 'white'}

                                    }
                                }),
                                className='card text-white bg-primary'
                            ))),
                    dbc.Col(dbc.Card(
                        dcc.Graph(
                            figure={
                                'data': [{'type': 'indicator',
                                          'mode': 'number+delta',
                                          'value': active_value,
                                          'delta': {'reference': active_delta,
                                                    'valueformat': '.2%',
                                                    'relative': True,
                                                    'font': {'size': 25, 'color': 'red'}},
                                          'number': {'valueformat': ',',
                                                     'font': {'size': 50, 'color': 'white'}},
                                          'domain': {'y': [0, 1], 'x': [0, 1]}}],
                                'layout': {
                                    'title': 'Total Active Cases',
                                    'height': 150,
                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                    'plot_bgcolor': 'rgba(0,0,0,0)',
                                    'font': {'color': 'white'}
                                }
                            },
                        ),
                        className='card text-white bg-info',
                        body=True
                    )),
                    dbc.Col(dbc.Card(
                        dcc.Graph(
                            figure={
                                'data': [{'type': 'indicator',
                                          'mode': 'number+delta',
                                          'value': recovered_value,
                                          'delta': {'reference': recovered_delta,
                                                    'valueformat': '.2%',
                                                    'relative': True,
                                                    'font': {'size': 25}},
                                          'number': {'valueformat': ',',
                                                     'font': {'size': 50, 'color': 'white'}},
                                          'domain': {'y': [0, 1], 'x': [0, 1]}}],
                                'layout': {
                                    'title': 'Total Recovered Cases',
                                    'height': 150,
                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                    'plot_bgcolor': 'rgba(0,0,0,0)',
                                    'font': {'color': 'white'}
                                }

                            },

                        ),
                        body=True,
                        className='card text-white bg-success'
                    )),
                    dbc.Col(dbc.Card(
                        dcc.Graph(
                            figure={
                                'data': [{'type': 'indicator',
                                          'mode': 'number+delta',
                                          'value': deaths_value,
                                          'delta': {'reference': deaths_delta,
                                                    'valueformat': '.2%',
                                                    'relative': True,
                                                    'font': {'size': 25}},
                                          'number': {'valueformat': ',',
                                                     'font': {'size': 50, 'color': 'white'}},
                                          'domain': {'y': [0, 1], 'x': [0, 1]}}],
                                'layout': {
                                    'title': 'Total Deaths',
                                    'height': 150,
                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                    'plot_bgcolor': 'rgba(0,0,0,0)',
                                    'font': {'color': 'white'}
                                }
                            },

                        ),
                        className='card text-white bg-danger',
                        body=True
                    ),
                    ),
                ],

            ),

        ),
    ]),
    html.Br(),
    html.Div([
        dbc.Container(dcc.Graph(figure=fig, responsive=True,))
    ])
])
# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)
