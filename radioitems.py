# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

from utils import *

def RadioItemsHTML(radio_flag,radio):
    if radio_flag:
        return html.Div([
                dcc.RadioItems(
                    id='type-radioitems',
                    style = {
                        'textAlign': 'left',
                        'color': colors['text'],
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '18',
                        'fontWeight': 'normal',
                        'marginLeft': '35px',
                    },
                    options=[
                        {'label': 'Charge', 'value': 'C'},
                        {'label': 'Discharge', 'value': 'D'},
                        {'label': 'Full Cycle', 'value': 'F'},
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