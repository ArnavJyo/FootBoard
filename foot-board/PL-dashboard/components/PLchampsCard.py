import dash
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html, callback

data = pd.read_csv("C:/Users/arnav/Desktop/foot-board/PL-dashboard/data/champions.csv")
# STYLE_SHEET_ROWS= {
#   "--bs-gutter-x": "1.625rem",
#   "--bs-gutter-y": "0",
#   "display": "flex",
#   "flex-wrap": "wrap",
#   "margin-top": "calc(-1 * var(--bs-gutter-y))",
#   "margin-right": "calc(-0.5 * var(--bs-gutter-x))",
#   "margin-left": "calc(-0.5 * var(--bs-gutter-x))"
# }
# Split the data into two rows
row1_data = data.iloc[:11]
row2_data = data.iloc[11:]

# Function to create a card for a winner
def create_winner_card(year, club_name, club_logo):
    return dbc.Col([
        html.Img(className="img-fluid m-2 rounded",src=club_logo, alt=club_name, style={"box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)"}),
        html.Center(html.H6(f"({year})",className="m-0"))
        
    ],className="col-lg-1 col-md-2 col-sm-4")
PLChamps= html.Div(className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container", children=
    [ html.Div(className="card", children=[
        html.Div(className="card-header card-m-0 me-2 pb-3",children=[
    html.H4("Premier League Winners Last 20 Years",className="card-title text-center m-0 me-2")]),
    html.Div([
        dbc.Row([create_winner_card(year, club_name, club_logo) for year, club_name, club_logo in row1_data.values], className="mt-2 mb-2 p-3 justify-content-center"),
        dbc.Row([create_winner_card(year, club_name, club_logo) for year, club_name, club_logo in row2_data.values], className="mt-2 mb-2 p-3 justify-content-center")
    ],style={"align-text": "center"})
    ],
)
    ])