from dash import html
import dash_bootstrap_components as dbc
from components.PLchampsCard import PLChamps
from components.IntroCard import IntroCard
from components.HomePageComponents import GoalsandAssists
from components.HomePageComponents import TeamGoals
from components.HomePageComponents import MostFouls
from components.HomePageComponents import PassCompletion,ToSuc,Err,Gca,G_Sot


home_page_content = html.Div([
        dbc.Row([
            IntroCard
        ]),
        dbc.Row([
            PLChamps
        ]),
        dbc.Row([
            GoalsandAssists,
            TeamGoals
        ]),
        dbc.Row([
            MostFouls,PassCompletion
        ]),
        dbc.Row([
            ToSuc,Err
        ]),
        dbc.Row([
            Gca,G_Sot
        ])
    ])