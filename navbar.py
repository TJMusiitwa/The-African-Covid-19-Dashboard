import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('Summary', href='/apps/app1')),
            dbc.NavItem(dbc.NavLink('Map', href='/apps/app2')),
            dbc.NavItem(dbc.NavLink('Trends', href='#')),
            dbc.NavItem(dbc.NavLink('About', href='/apps/about')),
        ],
        brand='The African Covid-19 Dashboard',
        color='primary',
        dark=True,
        brand_href="/home",
        sticky="top",
    )
    return navbar
