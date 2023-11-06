from dash.dependencies import Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
import dash_loading_spinners as dls
import utils.theme as theme
from dash import callback
from components.TeamCards import yellow_cards,red_cards
team_info = pd.read_csv("C:/Users/arnav/Desktop/foot-board/PL-dashboard/data/premier_league_teams_standings.csv")
epl_info = pd.read_csv("C:/Users/arnav/Desktop/foot-board/PL-dashboard/data/epl_clubs_info_2022-23.csv")

pl_winning_times_card = html.Div(html.Div(className="card", children=[
    html.Div(className="card-body", children=[
        html.Div(className="d-flex justify-content-between", children=[
            html.Div(className="card-info w-100",
                     children=[
                         dls.Triangle(
                               html.H2(className="mb-2 mt-2 card-title mb-2",
                                       id="winning-times-text",
                                       style={"font-size": "4.2vw"})
                         ),
                         html.H6(
                             className="card-text m-0", children=["Times Winner"], style={"font-size": "1vw"}
                         ),
                         html.Small(
                             className="card-text", id="winning-years-text",
                             style={"font-size": "0.6rem"}

                         )
                     ], style={"text-align": "center"}),

            html.Div(className="card-icon d-flex align-items-center", children=[
                html.Img(className="img-fluid bx-lg",
                         src="./assets/images/trophy2.jpg", style={"width": "8rem"})
            ]
            )
        ])

    ])
], style={"min-height": "11rem"}),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container"
)

TeamStatsOverall = dbc.Row(children=[
    html.Div(className="col-lg-3 col-md-6 col-sm-12 card-chart-container", children=[html.Div(className="card", children=[
        html.Div(className="card-body", children=[
            html.Div(className="d-flex justify-content-between", children=[
                html.Div(className="card-info",
                         children=[
                             dbc.Select(
                                 id="query-team-select",
                                 value="Manchester City",
                                 options=[
                                     {"label": l, "value": l} for l in epl_info['club_name']
                                 ],
                                 style={"width": "10rem"}
                             ),
                             html.P(className="card-text mb-1 mt-1 fs-sm",
                                    id="team-abv-text",
                                    children=[f"Team Abv: "]),
                         ]),
                html.Div(className="card-icon d-flex align-items-center w-40 justify-content-center p-1", children=[
                    dls.Triangle(
                        html.Img(className="img-fluid bx-lg",
                                 id="team-flag-main",
                                 style={
                                     "width": "2em", "box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"}
                                 ),
                        debounce=theme.LOADING_DEBOUNCE
                    )
                ]
                )

            ])

        ])
    ], style={"min-height": "11rem"})]
    ),
    pl_winning_times_card,
    red_cards,
    yellow_cards


])
@callback(
    Output("team-abv-text",'children'),
    Output("team-flag-main", "src"),
    Output("winning-times-text", "children"), 
    Input("query-team-select", "value"),
    State("club-df", "data"),
    State("champs-df","data")
)
def update_team_select(query_team,epl_info,champ_info):
    
    epl_info = pd.read_json(epl_info)
    champ_info = pd.read_json(champ_info)
    team_abv = epl_info.loc[epl_info.club_name == query_team,'abv'].values[0]
    team_flag  = epl_info.loc[epl_info.club_name == query_team,'logo_link'].values[0]
    temp_times = champ_info.loc[champ_info.Champions==
                                   query_team,'Champions']
    winning_times = len(temp_times)
    
    return team_abv,team_flag,winning_times
