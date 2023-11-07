from dash.dependencies import Input, Output, State
import pandas as pd
from dash import html, callback,dcc
import dash_loading_spinners as dls
from utils.theme import LOADING_DEBOUNCE
import plotly.express as px
import utils.theme as theme
yellow_cards = html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
                        children=[html.Div(className="card", children=[
                            html.Div(className="card-body", children=[
                                html.Div(className="d-flex justify-content-between", children=[

                                    html.Div(className="card-info w-100",
                                         children=[html.Small(className="card-text", children=["Yellow Cards"]),
                                                   dls.Triangle(
                                                   html.H2(className="mb-2 mt-2 card-title mb-2",
                                                           id="yellow-card-body",
                                                           style={"font-size": "4vw"})),
                                                   ], style={"text-align": "center"}),

                                    html.Div(className="card-icon d-flex align-items-center w-50", children=[
                                        html.Img(className="img-fluid bx-lg",
                                             src="./assets/images/yellow-card.png", style={"width": "6rem",
                                                                                           })
                                    ]
                                    )
                                ])

                            ])
                        ])
                        ]
                        )


red_cards = html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
                     children=[html.Div(className="card", children=[
                         html.Div(className="card-body", children=[
                             html.Div(className="d-flex justify-content-between", children=[

                                 html.Div(className="card-info w-100",
                                          children=[html.Small(className="card-text", children=["Red Cards"]),
                                                    dls.Triangle(
                                              html.H2(className="mb-2 mt-2 card-title mb-2",
                                                      id="red-card-body",
                                                      style={"font-size": "4vw"}), debounce=LOADING_DEBOUNCE),
    
                                                    ], style={"text-align": "center"}),

                                 html.Div(className="card-icon d-flex align-items-center w-50", children=[
                                        html.Img(className="img-fluid bx-lg",
                                                 src="./assets/images/red-card.png", style={"width": "6rem",
                                                                                            })
                                        ]
                                 )
                             ])

                         ])
                     ])
                     ],style={"min-height": "11rem"}
                     )

# TeamBookings = html.Div(
#     className="col-md-12 col-lg-2 mb-md-0 mb-4 card-chart-container d-flex flex-column justify-content-between", id="team-bookings",
#     children=[
#         yellow_cards,
#         red_cards
#     ]
# )
Progressive_Passes = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="progressive-pass-text")
                         ),
                         html.H6(
                             className="card-text m-0", children=["Progressive Passes"], style={"font-size": "2vw"}
                         ),
                         html.Small(
                             className="card-text", id="progressive-pass-text",
                             style={"font-size": "4vw"}

                         )
                     ], style={"text-align": "center"}),

        ])

    ])
], style={"min-height": "11rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)
xg_xag_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H5(className="mb-2 mt-2 card-title mb-2",
                                       id="xGxAG-90-text")
                         ),
                         html.H6(
                             className="card-text m-0", children=["Exprected Goals + Actual Goals per 90 minutes"], style={"font-size": "2vw"}
                         ),
                         html.Small(
                             className="card-text", id="xGxAG-90-text",
                             style={"font-size": "x-small"}

                         )
                     ], style={"text-align": "center"}),

        ])

    ])
], style={"min-height": "11rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)
 
 

@callback(
    Output("yellow-card-body", "children"),
    Output("red-card-body", "children"),
    # Output("progressive-pass-text","children"),
    # Output("xGxAG-90-text","children"),
    Input("query-team-select", "value"),
    State("std-stats-df", "data")
)
def update_team_bookings(query_team, team_stats_df):
    team_stats_df = pd.read_json(team_stats_df)
    yellow_card = team_stats_df.loc[team_stats_df.Squad ==
                                           query_team]["CrdY"].values[0]

    red_card = team_stats_df.loc[team_stats_df.Squad ==
                                        query_team]["CrdR"].values[0]
    prog_p = team_stats_df.loc[team_stats_df.Squad == query_team]["PrgP"].values[0]
    xG_XAG = team_stats_df.loc[team_stats_df.Squad == query_team]["xG+xAG"].values[0]
    return yellow_card,red_card
TeamMatchesResults = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                              children=[

                                  html.Div(
                                      className="card-chart",
                                      children=[
                                          html.H4("Overall Team Results",
                                                  className="card-header card-m-0 me-2 pb-3"),
                                          dls.Triangle(
                                              id="team-matches-results",
                                              children=[

                                              ], debounce=theme.LOADING_DEBOUNCE
                                          )
                                      ]
                                  )

                              ],
                              )
@callback(
    Output("team-matches-results", "children"),
    Input("query-team-select", "value"),
    State("results-22-23-df", "data")
)
def update_team_matches_result(query_team, team_stats_df):
    team_stats_df = pd.read_json(team_stats_df)
    team_stats={}
    for index,row in team_stats_df.iterrows():
        home_team = row["HomeTeam"]
        away_team = row["AwayTeam"]
        ftr = row["FTR"]
        if home_team not in team_stats:
            team_stats[home_team] = {'W': 0, 'L': 0, 'D': 0}
        if away_team not in team_stats:
            team_stats[away_team] = {'W': 0, 'L': 0, 'D': 0}

        if ftr == "H":
            team_stats[home_team]["W"] +=1
            team_stats[away_team]["L"]+=1
        elif ftr == "A":
            team_stats[home_team]["L"]+=1
            team_stats[away_team]['W']+=1
        else:
            team_stats[home_team]["D"]+=1
            team_stats[away_team]["D"]+=1
    team_wins_df = pd.DataFrame(team_stats).T
    win_counts = team_wins_df.loc[query_team]["W"]
    lose_counts = team_wins_df.loc[query_team]["L"]
    draw_counts = team_wins_df.loc[query_team]["D"]

    return dcc.Graph(figure=px.pie(names=["Won", "Lost", "Draw"], values=[win_counts, lose_counts, draw_counts], hole=0.6,
                                   color_discrete_sequence=theme.COLOR_PALLETE,
                                   ).add_annotation(x=0.5, y=0.5,
                                                    text='In 38 Matches',
                                                    showarrow=False)
                     .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                    plot_bgcolor="rgb(0,0,0,0)",
                                    legend=dict(
                                        bgcolor=theme.LEGEN_BG),
                                    font_family=theme.FONT_FAMILY,
                                    margin={"t": 40, "b": 40, "l": 32}
                                    ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )
TeamPossession = html.Div(className="card-chart-container col-lg-4 md-6 sm-12",
                              children=[

                                  html.Div(
                                      className="card-chart",
                                      children=[
                                          html.H4("Overall Team Possession",
                                                  className="card-header card-m-0 me-2 pb-3"),
                                          dls.Triangle(
                                              id="team-matches-possession",
                                              children=[

                                              ], debounce=theme.LOADING_DEBOUNCE
                                          )
                                      ]
                                  )

                              ],
                              )
@callback(
    Output("team-matches-possession", "children"),
    Input("query-team-select", "value"),
    State("possession-df", "data")
)
def update_team_match_possession(query_team, team_stats_df):
    team_stats_df =pd.read_json(team_stats_df)
    defence = team_stats_df.loc[team_stats_df.Squad == query_team]["Def3rd"].values[0]
    middle =  team_stats_df.loc[team_stats_df.Squad == query_team]["Mid3rd"].values[0]
    attack = team_stats_df.loc[team_stats_df.Squad == query_team]["Att3rd"].values[0]
    return dcc.Graph(figure=px.pie(names=["Defensive 3rd", "Middle 3rd", "Attacking 3rd"], values=[defence, middle, attack], hole=0.6,
                                   color_discrete_sequence=theme.COLOR_PALLETE,
                                   ).add_annotation(x=0.5, y=0.5,
                                                    text='In 38 Matches',
                                                    showarrow=False)
                     .update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                    plot_bgcolor="rgb(0,0,0,0)",
                                    legend=dict(
                                        bgcolor=theme.LEGEN_BG),
                                    font_family=theme.FONT_FAMILY,
                                    margin={"t": 40, "b": 40, "l": 32}
                                    ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )



