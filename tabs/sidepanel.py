import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from tabs import tab1, tab2
from database import transforms

df = transforms.df
min_p = df.Year.min()
max_p = df.Year.max()

layout = html.Div([
    html.H1('Dashing Through')
    , dbc.Row([dbc.Col(
        html.Div([
            html.H2('Filters')
            , dcc.Checklist(id='Last_Decade'
                            , options=[
                    {'label': ' Released this decade ', 'value': 'Y'}
                ])
            ,html.Div([html.P() ,html.H5('Artist'), dcc.Dropdown(id = 'Artist-drop'
                        ,options=[
                             {'label': i, 'value': i} for i in df['Artist_Name'].unique()],
                        value=[],
                        multi=True
                    )])
            , html.Div([html.H5('Year Slider')
                           , dcc.RangeSlider(id='year-slider'
                                             , min=min_p
                                             , max=max_p
                                             , marks={1910: '1910',
                                                      1920: '1920',
                                                      1930: '1930',
                                                      1940: '1940',
                                                      1950: '1950',
                                                      1960: '1960',
                                                      1970: '1970',
                                                      1980: '1980',
                                                      1990: '1990',
                                                      2000: '2000',
                                                      2010: '2010',
                                                      2020: '2020',
                                                      }
                                             , value=[1910, 2200]
                                             )

                        ])

        ], style={'marginBottom': 30, 'marginTop': 25, 'marginLeft': 0, 'marginRight': 0})
        , width=3)

        , dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Data Table', value='tab-1'),
                dcc.Tab(label='Scatter Plot', value='tab-2'),
            ])
            , html.Div(id='tabs-content')
        ]), width=9)])

])
