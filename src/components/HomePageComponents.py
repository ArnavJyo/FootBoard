
import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import numpy as np

import os
ROOT_FOLDER = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
SRC_FOLDER = os.path.join(ROOT_FOLDER, "src/")
DATA_FOLDER = os.path.join(SRC_FOLDER, "data/")
prem22_23 = pd.read_csv(os.path.join(ROOT_FOLDER,"data/PremierLeague22-23.csv"))
team_goals = prem22_23.groupby('Squad')['Goals'].sum().reset_index()
total_goals_scored = prem22_23['Goals'].sum()
sorted_data_fouls = prem22_23.sort_values(by='Fls', ascending=False)
total_fouls = prem22_23['Fls'].sum()
sorted_data = prem22_23.sort_values(by='ToSuc', ascending=False)
Error_data = prem22_23.sort_values(by='Err', ascending=False)
top_10_players_error = Error_data.head(10)
sorted_GCA = prem22_23.sort_values(by='GCA', ascending=False)
def create_card(fig, class_name, title="Title"):
    return html.Div(
        html.Div(
            className="card-chart",
            children=[
                html.H4(title,
                        className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                dcc.Graph(
                    figure=fig.update_layout(
                        paper_bgcolor="rgb(0,0,0,0)",
                        plot_bgcolor="rgb(0,0,0,0)",
                        legend=dict(bgcolor=theme.LEGEN_BG),
                        font_family=theme.FONT_FAMILY,
                    ),
                    config={"displayModeBar": False},
                )
            ],
        ), className=class_name,style={"margin-left": "5%"}
    )
GoalsandAssists = create_card(class_name= "card-chart-container col-lg-5 col-md-12 col-sm-12",title="Goals and Assists Plot",fig = px.scatter(prem22_23, x='Goals', y='Assists', text='Player',title='Goals vs. Assists')
)
TeamGoals = create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Goals per Team",fig=px.bar(team_goals, x='Squad', y='Goals', title='Total Goals Scored in 22/23: '+ str(total_goals_scored)))

MostFouls = create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Most Fouls Commited ",fig=px.bar(sorted_data_fouls, x='Player', y='Fls', title='Total Fouls Commited in 22/23: '+ str(total_fouls),labels={'Fls': 'Fouls', 'Player': 'Player Name'}))

PassCompletion = create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Pass Completion",fig = px.scatter_ternary(
    prem22_23,
    a='PasLonCmp%',
    b='PasMedCmp%',
    c='PasShoCmp%',
    hover_name='Player',  # Display player name on hover
    title='Ternary Scatter Plot of Players',
    labels={'PasLonCmp%': 'Long Pass Completion %', 'PasMedCmp%': 'Medium Pass Completion %', 'PasShoCmp%': 'Short Pass Completion %'},width=400,
)
)
ToSuc = create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Fouls Commited",fig = px.bar(
    sorted_data,
    x='Player',
    y='ToSuc',
    title='Players with the Most Fouls Commited',
    labels={'ToSuc': 'Number of Defenders Taken On Successfully'},
))
Err = create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Most Errors Commited which led to a shot",fig = px.bar(
    top_10_players_error,
    x='Player',
    y='Err',
    title='Players with the Most Errors Commited',
    labels={'Err': 'Errors Commited'},
))
Gca =create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Most Goal Creating Actions",fig = px.bar(
    sorted_GCA,
    x='Player',
    y='GCA',
    title='Players with the Most GCA',
    labels={'GCA': 'Goal Creating Actions'},
))
G_Sot = create_card(class_name='card-chart-container col-lg-5 col-md-12 col-sm-12',title="Goals per Shot on Target (G/SoT) for Players",fig = px.scatter(
    prem22_23,
    x='Player',
    y='G/SoT',
    title='Goals per Shot on Target (G/SoT) for Players',
    labels={'G/SoT': 'Goals per Shot on Target'},
))