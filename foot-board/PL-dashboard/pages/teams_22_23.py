from dash import html
import dash_bootstrap_components as dbc
from components.TeamSelector import TeamStatsOverall
from components.TeamsRanking22 import TeamRankingTable
from components.TeamCards import Progressive_Passes,TeamMatchesResults,xg_xag_card,TeamPossession
from components.TeamsvsRival import RivalSectionTitle,TeamVsRivalMainCard,SpiderChart,ScoredvsConceded

team_analysis_content = html.Div(
    children=[
        TeamStatsOverall,
        dbc.Row(children=[
            TeamRankingTable,
            TeamMatchesResults,
            TeamPossession
        ]),
        dbc.Row(children =[
            RivalSectionTitle

        ]),
        dbc.Row(children=[
            TeamVsRivalMainCard,
            SpiderChart,
            ScoredvsConceded
        ])


    ]
)
