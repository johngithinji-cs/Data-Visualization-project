# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def create_dash_app(flask_app):
    dash_app = Dash(__name__, server=flask_app, url_base_pathname="/dash/")
    dash_app.title = "Data Analytics: Understand Your Data!"

    #sample data
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    dash_app.layout = html.Div(children=[
        html.H1(children='Data Analytics'),

        html.Div(children='''
            Understand your data
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    return dash_app
