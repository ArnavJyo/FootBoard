from dash import html
import dash_bootstrap_components as dbc
# SIDEBAR_STYLE = {
#     "position": "relative",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
#     "transition": "width 0.3s ease-in-out"
# }

sidebar = html.Div(
    [
        
        html.Div(
            [

                html.Img(src="./assets/images/premierleaguelogo.jpg", style={"width": "3rem"}),
                html.H6("PremierLeague", className="m-0"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="tf-icons bx bx-trophy fas fa-home"), html.Span("22/23 Season Stats" , className="me-2")],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-group"),
                        html.Span("22/23 Teams"),
                    ],
                    href="/team-analysis",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="menu-icon tf-icons bx bx-info-circle"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                    className="pe-3",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)

