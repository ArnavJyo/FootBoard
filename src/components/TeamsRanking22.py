import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback
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


TeamRankingTable = html.Div(className="col-md-12 col-lg-4 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H4("Standings in Premier League 22/23",
                    className="card-title m-0 me-2", style={"font-size": "1.5vw"}),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            dls.Triangle(id="team-ranking-table",
                         children=[
                         ], debounce=theme.LOADING_DEBOUNCE)

        ], style={"height": theme.MAX_CHART_HEIGHT, "align-text": "center"})
    ])
])


@callback(
    Output("team-ranking-table", "children"),
    Input("query-team-select", "value"),
    State("standings-df", "data")
)
def update_standings_table(selected_team, data):
    df = pd.read_json(data)
    table = dbc.Table.from_dataframe(df,columns=["Pos","Team","Points","Goals_Scored","Goal_Difference"]
    ,header=["Position", "Club","Points","Goals Scored","Goal Difference"],className=" no-footer", striped=False, bordered=False, hover=True)
    # if selected_team:
    #     # Apply the custom style to the selected team's row
    #     for i, row in enumerate(df.iterrows()):
    #         club = row[1]['Team']
    #         if club == selected_team:
    #             selected_team_color = club_colors.get(club, 'white')
    #             table.children[i + 1].style = {
    #                 'background-color': selected_team_color,
    #                 'font-weight': 'bold',  # Optional: Add other styles as needed
    #             }

    return table