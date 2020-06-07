import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import transforms

df = transforms.df

layout = html.Div(
    id='table-paging-with-graph-container',
    className="five columns"
)


@app.callback(Output('table-paging-with-graph-container', "children"),
              [Input('Last_Decade', 'value')
                  , Input('year-slider', 'value')
                  , Input('Artist-drop', 'value')
               ])
def update_graph(yearcheck, prices, artists):
    dff = df

    low = prices[0]
    high = prices[1]

    dff = dff.loc[(dff['Year'] >= low) & (dff['Year'] <= high)]

    if yearcheck == ['Y']:
        dff = dff.loc[dff['Year'] >= 2010]
    else:
        dff

    if len(artists)>0:
        dff = dff[dff['Artist_Name'].isin(artists)]
    else:
        dff

    trace1 = go.Histogram(x=dff['Year'],
                          name="Histotest"
                          , opacity=0.7)
    return html.Div([
        dcc.Graph(
            id='rating-price'
            , figure={
                'data': [trace1],
                'layout': dict(
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    hovermode='closest'
                )
            }
        )
    ])