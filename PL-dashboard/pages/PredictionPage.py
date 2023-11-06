from dash import html
import dash_bootstrap_components as dbc
from components.IntroCard2 import IntroCard2
from components.final_table import TeamStandingsTable,TeamFixtureTable

prediction_page_content = html.Div(children = [
    dbc.Row(children=[
        IntroCard2
    ]),
    dbc.Row(children=[
        TeamStandingsTable,TeamFixtureTable
    ])

])