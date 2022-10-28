import os
import sys
import threading
import webbrowser
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
filename = os.path.abspath(os.path.join(bundle_dir, 'LukaDoncic.csv'))
df = pd.read_csv(filename)

app.layout = html.Div(children=[
    html.H1(children='Sample Dash App'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.Br(), 

    dcc.RadioItems(
        id='loc-radio-items',
        options=['All', 'Home', 'Away'],
        value='All', 
        inline=True
    ),

    dcc.Graph(
        id='example-graph',
        figure={}
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='loc-radio-items', component_property='value')
)
def filter_location(location):
    if location == 'All':
        return px.scatter(df, x="GAME_DATE", y="PTS", color="WL")
    elif location == 'Home':
        df_filtered = df[(df['LOC'] == 'Home')]
        return px.scatter(df_filtered, x="GAME_DATE", y="PTS", color="WL")
    elif location == 'Away':
        df_filtered = df[(df['LOC'] == 'Away')]
        return px.scatter(df_filtered, x="GAME_DATE", y="PTS", color="WL")

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    # app.run_server(debug=True) # does not work with pyinstaller
    app.run_server(debug=False)