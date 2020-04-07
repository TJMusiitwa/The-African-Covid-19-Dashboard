import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# from app import app
# from apps import app1, app2


index_layout = html.Div([
    dcc.Link('Go to app1', href='/apps/app1')
    html.Br()
    dcc.Link('Go tp app2', href='/apps/app2')
])


# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/apps/app1':
#         return app1.layout
#     elif pathname == '/apps/app2':
#         return app2.layout
#     else:
#         return app1.layout


# if __name__ == '__main__':
#     app.run_server(debug=True)
