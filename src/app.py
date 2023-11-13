import os
import glob
import sys
module_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__))))
if module_path not in sys.path:
    sys.path.append(module_path)
import dash
import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash.dependencies import Input, Output
from components.NavBar import sidebar
from pages.homePage import home_page_content
from pages.teams_22_23 import team_analysis_content
from pages.PredictionPage import prediction_page_content
ROOT_FOLDER = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
SRC_FOLDER = os.path.join(ROOT_FOLDER, "src/")
DATA_FOLDER = os.path.join(SRC_FOLDER, "data/")
ASSETS_FOLDER = os.path.join(SRC_FOLDER, "assets")

player_stats_22_23 = pd.read_csv(os.path.join(DATA_FOLDER,"PremierLeague22-23.csv"))
team_stats_22_23 = pd.read_csv(os.path.join(DATA_FOLDER,"2022-2023 Football Team Stats.csv"))
results_22_23  = pd.read_csv(os.path.join(DATA_FOLDER,"epl_results_2022-23.csv"))
club_assets = pd.read_csv(os.path.join(DATA_FOLDER,"epl_clubs_info_2022-23.csv"))
standings_22_23 = pd.read_csv(os.path.join(DATA_FOLDER,"PL_standings_22-23.csv"))
times_champs = pd.read_csv(os.path.join(DATA_FOLDER,"PL_champs.csv"))
std_stats = pd.read_csv(os.path.join(DATA_FOLDER,"premier_league_stats.csv"))
matches_df = pd.read_csv(os.path.join(DATA_FOLDER,"epl_results_2022-23.csv"))
goalkeeping_df = pd.read_csv(os.path.join(DATA_FOLDER,"pl_goalkeeping.csv"))
shots_df = pd.read_csv(os.path.join(DATA_FOLDER,"shotcreation.csv"))
extra_df = pd.read_csv(os.path.join(DATA_FOLDER,"third_table_stats.csv"))
passing_df = pd.read_csv(os.path.join(DATA_FOLDER,"passing.csv"))
possession_df =pd.read_csv(os.path.join(DATA_FOLDER,"Possession.csv"))
data_store = html.Div([dcc.Store(id="player-stats-df", data=player_stats_22_23.to_json()),
                       dcc.Store(id="results-22-23-df", data=results_22_23.to_json()),
                       dcc.Store(id="club-df", data=club_assets.to_json()),
                       dcc.Store(id = "standings-df",data=standings_22_23.to_json()),
                       dcc.Store(id = "champs-df",data=times_champs.to_json()),
                       dcc.Store(id = "std-stats-df",data=std_stats.to_json()),
                       dcc.Store(id = "matches-df",data=matches_df.to_json()),
                       dcc.Store(id = "goalkeeping-df",data = goalkeeping_df.to_json()),
                       dcc.Store(id = "shots-df",data=shots_df.to_json()),
                       dcc.Store(id = "extra-df",data=extra_df.to_json()),
                       dcc.Store(id = "passing-df",data = passing_df.to_json()),
                       dcc.Store(id = "possession-df",data = possession_df.to_json() )
                    #    dcc.Store(id="tours-df", data=tours.to_json()),
                    #    dcc.Store(id="teams-df", data=teams.to_json()),
                    #    dcc.Store(id="bookings-df", data=bookings.to_json()),
                    #    dcc.Store(id="team-stats-df", data=team_stats.to_json())
                     ])
external_style_sheet = glob.glob(os.path.join(
    ASSETS_FOLDER, "CSS","bootstrap") + "/*.css")

external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,
                                  "CSS") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER,
                                  "CSS","boxicons") + "/*.css")
app = dash.Dash(__name__,title="Premier League DashBoard",external_stylesheets=[dbc.themes.BOOTSTRAP]+external_style_sheet,suppress_callback_exceptions=True)
server = app.server
app.layout = html.Div([
    html.Div(className="layout-container",children=[
        dcc.Location(id="url"),
        data_store,
        html.Aside(className="",children=[
            sidebar
        ]),
        html.Div(className="layout-page",
            children=[
            html.Div(className="content-wrapper",
            children=[
        html.Div(className="container-xxl flex-grow-1 container-p-y p-0",
    id="page-content",
    children=[
    ]),
html.Footer(className="content-footer footer bg-footer-theme",
 children=[
],style={"margin-left": "6rem"}) ])])])
],style={'font-family': "RadikalMedium","margin-left": "6rem"})
@callback(
    Output(component_id ='page-content',component_property='children'),
    Input(component_id = 'url',component_property='pathname')  
)
def routing(path):
    if path == "/":
        return home_page_content
    elif path == "/team-analysis":
        return team_analysis_content
    elif path == "/predictions":
        return prediction_page_content
if __name__ =="__main__":
    app.run_server(port=3000,debug = True)
