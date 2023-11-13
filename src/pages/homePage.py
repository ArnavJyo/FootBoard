from dash import html
import dash_bootstrap_components as dbc
from components.PLchampsCard import PLChamps
from components.IntroCard import IntroCard
from components.HomePageComponents import GoalsandAssists,PassCompletion,ToSuc,Err,Gca,G_Sot,TeamGoals,MostFouls



home_page_content = html.Div([
        dbc.Row([
            IntroCard
        ]),
        dbc.Row([
            PLChamps
        ]),
        dbc.Row([
            Err,
            TeamGoals
        ]),
        dbc.Row([
            MostFouls,PassCompletion
        ]),
        dbc.Row([
            ToSuc,GoalsandAssists
        ]),
        dbc.Row([
            Gca,G_Sot
        ])
    ])
