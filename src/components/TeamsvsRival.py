import pandas as pd
from dash import html,dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
import numpy as np
from dash import callback
import plotly.graph_objects as go
import plotly.express as px
club_colors = {
    "Manchester City": "skyblue",
    "Arsenal": "red",
    "Manchester United": "red",
    "Newcastle United": "black",
    "Liverpool": "red",
    "Brighton": "blue",
    "Aston Villa": "claret",
    "Tottenham Hotspur": "white",
    "Brentford": "red",
    "Fulham": "black",
    "Crystal Palace": "blue",
    "Chelsea": "blue",
    "Wolves": "gold",
    "West Ham": "claret",
    "Bournemouth": "red",
    "Nottingham Forest ": "red",
    "Everton": "blue",
    "Leicester City City": "blue",
    "Leeds United": "white",
    "Southampton": "red"
}


RivalSectionTitle = html.Div([
    html.H2([html.Span("See How "), html.Span(id="rival-section-title",
            style={"color": theme.COLOR_PALLETE[0], }), html.Span(" Performed against other teams in Premier League ")])
], style={"margin-top": "3rem"})

TeamVsRivalMainCard = html.Div(className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
                               children=[html.Div(className="card", children=[
                                   html.Div(className="card-body", children=[
                                       html.Small("Choose Rival Team to see history with",
                                                  className="card-text mt-1 mb-2",
                                                  ),
                                       dbc.Select(id="rival-team-select"),
                                       html.Div(className="d-flex justify-content-between mt-3", children=[
                                           html.Div(className="card-info w-100",
                                                    children=[html.P(className="card-text mb-1 mt-1", id="rival-main-card-header"),
                                                              html.P(className="card-title mb-1 mt-1",
                                                                     id="rival-main-card-body",
                                                                     style={"font-size": "1rem"}),
                                                              ],
                                                    ),

                                           html.Div(className="card-icon d-flex align-items-center", children=[
                                               html.Img(className="img-fluid", id="rival-main-card-icon", alt="flag",
                                                        src="icon", style={"width": "5em", "box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"})
                                           ]
                                           )
                                       ]),
                                       html.P(
                                           className="card-text  mt-2", id="rival-main-card-subtitle", style={"font-size": "0.8em"})

                                   ])
                               ], style={"min-height": "17.2rem"})

                               ]
                               )
@callback(
    Output("rival-team-select", "options"),
    Output("rival-team-select", "value"),
    Output("rival-main-card-subtitle", "children"),
    Output("rival-section-title", "children"),
    Input("query-team-select", "value"),
    State("matches-df", "data"),
)
def update_rival_select_options(query_team, matches_df):
    matches_df = pd.read_json(matches_df)

    away_teams = matches_df.loc[(
        matches_df.AwayTeam == query_team)].HomeTeam.unique()
    home_teams = matches_df.loc[(
        matches_df.HomeTeam == query_team)].AwayTeam.unique()
    rival_teams = set(away_teams)
    rival_teams = list(rival_teams.union(home_teams))
    rival_teams.sort()
    

    options = [{"label": l, "value": l} for l in rival_teams]
    card_subtitle = f"*Note: only teams that have played against {query_team} are shown in the list"

    return options, rival_teams[np.random.randint(0, len(rival_teams))], card_subtitle, query_team
@callback(
    Output("rival-main-card-icon", "src"),
    Output("rival-main-card-body", "children"),
    Input("rival-team-select", "value"),
    State("club-df", "data")
)
def update_team_vs_rival_main_card(rival_team, teams_df):
    teams_df = pd.read_json(teams_df)
    team_code = f"Team Abv: {teams_df.loc[teams_df.club_name==rival_team , 'abv']}"

    rival_logo = teams_df.loc[teams_df.club_name ==rival_team,"logo_link"].values[0]
    return rival_logo, team_code

SpiderChart = html.Div(className="col-md-12 col-lg-4 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H4("Team Comparison",
                    className="card-title m-0 me-2", style={"font-size": "1.5vw"}),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            dls.Triangle(id="team-comparison-chart",
                         children=[
                         ], debounce=theme.LOADING_DEBOUNCE)

        ], style={"height": theme.MAX_CHART_HEIGHT, "align-text": "center"})
    ])
])

@callback(
    Output("team-comparison-chart","children"),
    Input("rival-team-select", "value"),
    Input("query-team-select", "value"), 
    [State("goalkeeping-df","data"),
    State("shots-df","data"),
    State("extra-df","data"),State("passing-df","data"),State("possession-df","data")]
)
def update_spider_chart(rival_team,curr_team,goalkeeping_df,shots_df,extra_df,passing_df,poss_df):
    g_df = pd.read_json(goalkeeping_df)
    shots_df = pd.read_json(shots_df)
    extra_df = pd.read_json(extra_df)
    passing_df = pd.read_json(passing_df)
    poss_df = pd.read_json(poss_df)
    clean_sheets_h = g_df.loc[g_df.Squad == curr_team,"CS"].values[0]
    clean_sheets_r = g_df.loc[g_df.Squad == rival_team,"CS"].values[0]
    sca_h = shots_df.loc[shots_df.Squad == curr_team,"SCA90"].values[0]
    sca_r = shots_df.loc[shots_df.Squad == rival_team,"SCA90"].values[0]
    gca_h = shots_df.loc[shots_df.Squad == curr_team,"GCA90"].values[0]
    gca_r = shots_df.loc[shots_df.Squad == rival_team,"GCA90"].values[0]
    aerial_h = extra_df.loc[extra_df.Squad == curr_team,"Won%"].values[0]
    aerial_r = extra_df.loc[extra_df.Squad == rival_team,"Won%"].values[0]
    passing_h = passing_df.loc[passing_df.Squad == curr_team,"Cmp%"].values[0]
    passing_r = passing_df.loc[passing_df.Squad == rival_team,"Cmp%"].values[0]
    possession_h = poss_df.loc[poss_df.Squad == curr_team,"Poss"].values[0]
    possession_r = poss_df.loc[poss_df.Squad == rival_team,"Poss"].values[0]
    attack_h = (sca_h+gca_h)/2
    attack_r =(sca_r+gca_r)/2
    categories = ["Clean Sheets","Attack" ,"Aerial duals Won","Pass Completion","Possession"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r =[clean_sheets_h,attack_h,aerial_h,passing_h,possession_h],
        theta= categories,
        fill="toself",
        name = curr_team,
        fillcolor='rgba(0,0,255,0.2)'
    ))
    fig.add_trace(go.Scatterpolar(
        r =[clean_sheets_r,attack_r,aerial_r,passing_r,possession_r],
        theta= categories,
        fill="toself",
        name = rival_team,
        fillcolor='rgba(255,0,0,0.2)'
    ))
    fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 100]
    )),
  showlegend=False
)
    return dcc.Graph(figure = fig)
ScoredvsConceded = html.Div(className="col-md-12 col-lg-4 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H4("Scored vs Conceded",
                    className="card-title m-0 me-2", style={"font-size": "1.5vw"}),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            dls.Triangle(id="team-comparison-goals",
                         children=[
                         ], debounce=theme.LOADING_DEBOUNCE)

        ], style={"height": theme.MAX_CHART_HEIGHT, "align-text": "center"})
    ])
])
@callback(
    Output("team-comparison-goals","children"),
    Input("rival-team-select", "value"),
    Input("query-team-select", "value"),
    State("results-22-23-df","data")   
)
def update_bargraph(rival_team ,query_team,results_df):
    results_df = pd.read_json(results_df)
    home_goals = results_df.loc[(results_df.HomeTeam == query_team) & (results_df.AwayTeam == rival_team),'FTHG'].values[0]
    rival_goals = results_df.loc[(results_df.HomeTeam == query_team) & (results_df.AwayTeam == rival_team),'FTAG'].values[0]
    home_goals1 = results_df.loc[(results_df.HomeTeam == rival_team) & (results_df.AwayTeam == query_team),'FTHG'].values[0]
    rival_goals1 = results_df.loc[(results_df.HomeTeam == rival_team) & (results_df.AwayTeam == query_team),'FTAG'].values[0]
    return dcc.Graph(figure=px.bar(x=["Goals Scored", "Goals Conceded"], y=[home_goals+home_goals1, rival_goals+rival_goals1], height=theme.MAX_CHART_HEIGHT,
                                   labels={"y": "Count", "x": ""}, color_discrete_sequence=theme.COLOR_PALLETE, text_auto=True,
                                   ).update_layout(paper_bgcolor="rgb(0,0,0,0)",
                                                   plot_bgcolor="rgb(0,0,0,0)",
                                                   legend=dict(
                                                       bgcolor=theme.LEGEN_BG),
                                                   font_family=theme.FONT_FAMILY,
                                                   ),
                     config={
        "displayModeBar": False},
        style=theme.CHART_STYLE

    )

