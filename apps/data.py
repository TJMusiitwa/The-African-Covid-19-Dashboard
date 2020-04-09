import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd

from navbar import Navbar

df_africa = pd.read_csv('africa_data.csv')

nav = Navbar()

data_layout = html.Div(
    children=[
        nav,
        dbc.Container([
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df_africa.columns],
                data=df_africa.to_dict('records'),
                virtualization=True,
                sort_action='native',
                filter_action="native",
            ),
            html.Div(html.Br(),),
            dbc.Row(
                [
                    dbc.Col(html.A(
                        'Download This Data',
                        id='download-link',
                        download="africa_data.csv",
                        href="",
                        target="_blank",
                        className='btn btn-secondary'
                    )),

                ],
                justify="end",
                align="end",
            ),
        ],
            fluid=True,
        ),

    ])
