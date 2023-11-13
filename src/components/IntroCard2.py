from dash import html
import dash_bootstrap_components as dbc
IntroCard2 = html.Div(className="col-md-12 container-fluid col-lg-12 mb-md-0 mb-4 card-chart-container", style={"margin-left": "10px"}, children=[

    html.Div(className="card", children=[
        dbc.Row([
            dbc.Col(className="col-lg-6", children=[
                html.Div(className="card-header card-m-0 me-2 pb-3", children=[
                    html.H2(["Premier League Predictions"],
                        className="card-title m-0 me-2 mb-2", style={"font-size": "2vw"}),
                    html.Span(
                        "From Data Science Point-of-View", style={"color": "#0084d6", "font-size": "1.5vw","textAlign":"center"})
                ]),
                html.P(["The correspondence between model and reality is very good. Remember all the complexity at play here.All the shouting by the manager from the touchline.The fans trying to rally their team .The thoughts in the heads of the players as they tell  themselves that now is their chane to score.None of these factors seem to affect the distribution of goals scored. On the contrary ,it is all these factors acting together that generate the type of randomness assumed in the model"
                ],style={"teteam xtAlign":"center"}),
                 html.P(["Football’s beauty is its unpredictability, says Arsene Wenger .Arsene Wenger says his undiminished, ever-lasting love of football is based on the game’s glorious unpredictability."],style={"teteam xtAlign":"center"}),
                 html.P(["At a football club, there's a holy trinity—the players, the manager and the supporters. Directors don't come into it. They are only there to sign the cheques."

],style={"teteam xtAlign":"center"}),
html.P(["NOTE ** The predictions are based on the last season(22/23) and results till matchweek 9 of the current season , this is purely an analysis based on historical data **"

],style={"teteam xtAlign":"center"})
            ]),

            dbc.Col(className="col-lg-6", children=[
                html.Img(
                    src="./assets/images/prediction_page_pic.png", className="img-fluid"
                )
            ])
        ]),
    ])
])