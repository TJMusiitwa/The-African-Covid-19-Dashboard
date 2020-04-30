import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

#from app import app
from navbar import Navbar

nav = Navbar()

df_africa = pd.read_csv('africa_data.csv')
df_africa['date'] = pd.to_datetime(df_africa['date'])

update = df_africa['date'].dt.strftime('%B %d, %Y').iloc[-1]

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

recovered_map_data = df_africa[df_africa['date'] == df_africa['date'].iloc[-1]].groupby('Country/Region').agg(
    {'Recovered': 'sum', 'Longitude': 'mean', 'Latitude': 'mean', 'Country/Region': 'first'})

death_map_data = df_africa[df_africa['date'] == df_africa['date'].iloc[-1]].groupby('Country/Region').agg(
    {'Deaths': 'sum', 'Longitude': 'mean', 'Latitude': 'mean', 'Country/Region': 'first'})

# Initialize figure with subplots
fig = make_subplots(
    rows=1, cols=3,
    subplot_titles=['Active cases in Africa',
                    'Recovered cases in Africa', 'Death cases in Africa'],
    column_widths=[0.4, 0.4, 0.4],
    specs=[[{"type": "scattergeo"}, {"type": "scattergeo"}, {"type": "scattergeo"}]])


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
                    showscale=False,
                    symbol='circle',
                    line=dict(width=1, color='rgba(102, 102, 102)'),
                    colorscale='Blues',
                    cmin=0,
                    color=map_data['Active'],
                    cmax=map_data['Active'].max(),
                    colorbar_title="Active Cases")),
    row=1, col=1
)


fig.add_trace(
    go.Scattergeo(
        lon=recovered_map_data['Longitude'],
        lat=recovered_map_data['Latitude'],
        text=recovered_map_data['Country/Region'] + ': ' +
        recovered_map_data['Recovered'].astype(str),
        mode='markers',
        showlegend=False,
        marker_size=(
            100 * recovered_map_data['Recovered'] / recovered_map_data['Recovered'].max()),
        marker=dict(reversescale=False,
                    autocolorscale=False,
                    showscale=False,
                    symbol='circle',
                    line=dict(width=1, color='rgba(102, 102, 102)'),
                    colorscale='Greens',
                    cmin=0,
                    color=recovered_map_data['Recovered'],
                    cmax=recovered_map_data['Recovered'].max(),
                    colorbar_title="Recovered Cases")),
    row=1, col=2
)


fig.add_trace(
    go.Scattergeo(
        lon=death_map_data['Longitude'],
        lat=death_map_data['Latitude'],
        text=death_map_data['Country/Region'] + ': ' +
        death_map_data['Deaths'].astype(str),
        mode='markers',
        showlegend=False,
        marker_size=(
            100 * death_map_data['Deaths'] / death_map_data['Deaths'].max()),
        marker=dict(reversescale=False,
                    autocolorscale=False,
                    showscale=False,
                    symbol='cross',
                    line=dict(width=1, color='rgba(102, 102, 102)'),
                    colorscale='Reds',
                    cmin=0,
                    color=death_map_data['Deaths'],
                    cmax=death_map_data['Deaths'].max(),
                    colorbar_title="Death Cases")),
    row=1, col=3
)

# Update geo subplot properties
fig.update_geos(
    scope='africa',
    resolution=50,
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
    margin=dict(r=10, t=25, b=25, l=10),
)

traces = [go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Confirmed'].sum(),
    hovertemplate='%{y:,g}',
    name="Confirmed",
    stackgroup='one',
    mode='lines'),
    go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Active'].sum(),
    hovertemplate='%{y:,g}',
    name="Active",
    stackgroup='one',
    mode='lines'),
    go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Recovered'].sum(),
    hovertemplate='%{y:,g}',
    name="Recovered",
    stackgroup='one',
    mode='lines'),
    go.Scatter(
    x=df_africa.groupby('date')['date'].first(),
    y=df_africa.groupby('date')['Deaths'].sum(),
    hovertemplate='%{y:,g}',
    name="Deaths",
    stackgroup='one',
    mode='lines')]

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
    html.Div(children='Data last updated {}'.format(update), style={
        'textAlign': 'center',
    }),
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
                                                        'font': {'size': 25, 'color': 'yellow'}},
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
                                                    'font': {'size': 25, 'color': 'yellow'}},
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
        dbc.Container(dcc.Graph(figure=fig, responsive='auto',))
    ]),
    dbc.Container(
        dcc.Graph(
            figure={
                'data': traces,
                'layout': {
                    'title': 'Cases timeline in Africa',
                    'xaxis_title': 'Date',
                    'yaxis_title': 'Number of Cases',
                }
            })
    ),
    html.Div([
        html.P(children='As per {}, Africa has not reached the point where the number of active cases surpasses the revovered cases; this means that we still have a long way to go before seeing a defeat of the virus.'.format(update), className='lead')
    ], className='blockquote text-center')

])
# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)
