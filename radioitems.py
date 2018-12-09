# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

def RadioItemsHTML(radio_flag,radio):
    if radio_flag:
        return html.Div([
                dcc.RadioItems(
                    id='type-radioitems',
                    style = {
                        'textAlign': 'left',
                        'color': '#000000',
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '18',
                        'fontWeight': 'normal',
                        'marginLeft': '35px',
                    },
                    options=[
                        {'label': 'Charge', 'value': 'C'},
                        {'label': 'Discharge', 'value': 'D'},
                        {'label': 'All Data', 'value': 'A'},
                    ],
                    value=radio,
                    labelStyle={
                        'display': 'inline-block',
                        'paddingRight': '15px'
                        }
                )
            ])
    else:
        return html.Div([
                dcc.RadioItems(
                    id='type-radioitems',
                    value='A'
                )
            ])