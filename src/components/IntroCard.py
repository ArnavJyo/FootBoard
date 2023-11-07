from dash import html
import dash_bootstrap_components as dbc

IntroCard = html.Div(className="col-md-12 container-fluid col-lg-12 mb-md-0 mb-4 card-chart-container", style={"margin-left": "10px"}, children=[

    html.Div(className="card", children=[
        dbc.Row([
            dbc.Col(className="col-lg-6", children=[
                html.Div(className="card-header card-m-0 me-2 pb-3", children=[
                    html.H2(["Premier League Dashboard"],
                        className="card-title m-0 me-2 mb-2", style={"font-size": "2vw"}),
                    html.Span(
                        "From Data Science Point-of-View", style={"color": "#38003c", "font-size": "1.5vw","textAlign":"center"})
                ]),
                html.P(["This dashboard presents all you need to know about English Premier League through history: winners, current season analytics, matches, and more. You can also check each team's statistics and compare teams with each other in the",
                        html.A(" Teams tab.", href="/team-analysis",
                               style={"color": "#38003c"}),
                ],style={"textAlign":"center"})
            ]),
            
            dbc.Col(className="col-lg-6", children=[
                html.Img(
                    src="./assets/images/playersIntro.png", className="img-fluid"
                )
            ])
        ]),
    ])
])
