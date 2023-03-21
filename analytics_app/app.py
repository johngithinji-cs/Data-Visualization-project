import pandas as pd
from dash import Dash, dcc, html


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Alkatro:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Data Analytics: Understand Your Data!"

data = (
        # Read in the csv file
        pd.read_csv("avocado.csv")
        .query("type == 'conventional' and region == 'Albany'")
        .assign(Date=lambda data: pd.to_datetime(data["Date"],
                format="%Y-%m-%d"))
        .sort_values(by="Date")
        )

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children='favicon', className='header-emoji'),
                html.H1(
                    children='Data Analytics', className='header-title'),
                html.P(
                    children=("Analyze your data to discover"
                              " life changing information"),
                    className="header-description"
                    ),
            ],
            className="header"
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        #config={"displayModeBar": False}
                        figure={
                            "data": [
                                {
                                    # Specify columns to visualize
                            "x": data["Date"],
                            "y": data["AveragePrice"],
                            #type is type of visualization bar, line etc
                            "type": "lines",
                            "hovertemplate": (
                                "$%{y:.2f}<extra></extra>"
                                ),
                        },
                ],
                "layout": {
                    "title": {
                        "text": "Average price",
                        "x": 0.05,
                        "xanchor": "left",
                        },
                    "xaxis": {"fixedrange": True},
                    "yaxis": {
                        "tickprefix": "$",
                        "fixedrange": True,
                    },
                    "colorway": ["#17b897"],
                    },
                },
            ),
            className="card",
        ),
        html.Div(
            children=dcc.Graph(
                id="volume-chart",
                #config={"displayModeBar": False},
                figure={
                    "data": [
                        {
                            # Specify columns to visualize
                            "x": data["Date"],
                            "y": data["Total Volume"],
                            #type is type of visualization bar, line etc
                            "type": "lines",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Sales",
                            "x": 0.05,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True},
                        "yaxis": {"fixedrange": True},
                        "colorway": ["#E12D39"],
                        },
                    },
                ),
                className="card",
            ),
        ],
        className="wrapper",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=5000, debug=True)
