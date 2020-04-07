import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('Summary', href='/apps/summary')),
            dbc.NavItem(dbc.NavLink('Data', href='/apps/data')),
            dbc.NavItem(dbc.NavLink(
                'Regional Trends', href='/apps/regional_trends')),
            dbc.NavItem(dbc.NavLink('About', href='/apps/about')),
        ],
        brand='The African Covid-19 Dashboard',
        color='primary',
        dark=True,
        brand_href="/home",
        sticky="top",
    )
    return navbar
