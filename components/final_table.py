import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
df = pd.read_csv("C:/Users/arnav/Desktop/foot-board/PL-dashboard/data/Predicted_Standings.csv")
df1 = pd.read_csv('C:/Users/arnav/Desktop/foot-board/PL-dashboard/data/final_prediction.csv')

table = dbc.Table.from_dataframe(df,columns=["Teams","Predicted Points"]
    ,header=["Club","Predicted Points"],className=" no-footer", striped=False, bordered=False, hover=True)
table1  = dbc.Table.from_dataframe(df1,columns=['Date_x','HomeTeam','AwayTeam' ,'Predicted Winner']
    ,header=['Date','HomeTeam','AwayTeam','Predicted Winner'],className=" no-footer", striped=False, bordered=False, hover=True)

TeamStandingsTable = html.Div(className="col-md-12 col-lg-4 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H4(" Predicted Results in Premier League 23/24",
                    className="card-title m-0 me-2", style={"font-size": "1.5vw"}),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            table

        ], style={"height": theme.MAX_CHART_HEIGHT, "align-text": "center"})
    ])
])
TeamFixtureTable = html.Div(className="col-md-12 col-lg-4 mb-md-0 mb-4 card-chart-container", children=[
    html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3", children=[
            html.H4(" Predicted Standings in Premier League 23/24",
                    className="card-title m-0 me-2", style={"font-size": "1.5vw"}),
        ]),
        html.Div(className="table-responsive text-nowrap overflow-auto", children=[
            table1

        ], style={"height": theme.MAX_CHART_HEIGHT, "align-text": "center"})
    ])
])
