import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from navbar import Navbar

nav = Navbar()

about_layout = html.Div([
    nav,
    dbc.Container(
        dbc.Row(
            dcc.Markdown('''
# The African Covid-19 Dashboard
### Foreword
Hello and welcome, you might be wondering "oh great" another dashboard and yes you are right it is however, the prime focus of this dashboard is as stated in the title to mainly visualize an overview of the 2019 Novel Coronavirus COVID-19 (2019-nCoV) epidemic as it relates to the African continent.

This dashboard was built with Python using [Dash](https://dash.plot.ly/), with charts made in [Plotly](https://plot.ly/) and the Flatly theme of the app provided by [Bootswatch](https://bootswatch.com/flatly/).
 The code behind the dashboard  is available [here](github.com).
 
Take in kind that this is my first dashboard as well as using Dash so it is not an expert level dashboard but hey we all gotta start somewhere. 😁

### Data
The data used in this dashboard is provided by the [Johns Hopkins Center for Systems Science and Engineering](https://github.com/CSSEGISandData/COVID-19) Coronavirus repository.

The African regions in this dashboard were apportioned according to the  [United Nations geoscheme](https://en.wikipedia.org/wiki/United_Nations_geoscheme)

### Inspiration
I would not have been able to create my first dashboard without some inspiration from the following sources, and I am highly grateful to them.

 - [The Coronavirus Dashboard by RamiKrispin](https://github.com/RamiKrispin/coronavirus_dashboard) built in R
 - [Covid-19 Dashboard by raffg](https://github.com/raffg/covid-19) built in python


            
            '''),
            justify="center",
        )
    )

])
