import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

#from app import app
from navbar import Navbar

nav = Navbar()


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
                                dcc.Graph(id='confirmed_total'),
                                className='card text-white bg-primary'
                            ))),
                    dbc.Col(dbc.Card(
                        dbc.CardBody(
                            [html.H3("1400", className="card-title"),
                             html.P("Active Cases",
                                    className="card-text"),
                             ],
                            className='card text-white bg-info'
                        ))),
                    dbc.Col(dbc.Card(
                        dbc.CardBody(
                            [html.H3("1400", className="card-title"),
                             html.P("Recovered Cases",
                                    className="card-text"),
                             ],
                            className='card text-white bg-success'
                        ))),
                    dbc.Col(dbc.Card(
                        dbc.CardBody(
                            [html.H3("100", className="card-title"),
                             html.P("Deaths",
                                    className="card-text"),
                             ],
                            className='card text-white bg-danger'
                        ))),
                ]
            ),
            fluid=True,
        ),
        dbc.Row(
            [
                # dbc.Col(html.Div(""), width=3),
                dbc.Col(
                    children=dbc.FormGroup(
                        [

                            dbc.Label("Region"),
                            dbc.RadioItems(
                                options=[
                                    {'label': 'North Africa', 'value': 'NA'},
                                    {'label': 'East Africa', 'value': 'EA'},
                                    {'label': 'West Africa', 'value': 'WA'},
                                    {'label': 'Central Africa', 'value': 'CA'},
                                    {'label': 'South Africa', 'value': 'SA'},
                                ],
                                value='EA',
                                id="radioitems-inline-input",
                                inline=True,
                                # className='custom-control custom-radio',
                                # inputClassName='custom-control-input',
                                # labelClassName='custom-control-label',
                            ),
                        ],
                        className='form-group'
                    ),
                    align='center',
                    style={'align': 'center'},
                    width={"size": 8, "offset": 3}
                ),
                # dbc.Col(html.Div(""), width=3),
            ]
        ),
    ])
])
# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)
