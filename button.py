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

def ButtonHTML(text_,id_):
    return html.Div(
            children=[html.Button(text_, 
                id=id_,
                style={
                    'height': '95%',
                    'width': '80%',
                    'marginLeft':'10%', 'marginRight': '10%',
                    'marginBottom': '5%',
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                    'marginTop': '35px',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                },
            ),],
            style={'textAlign': 'center','backgroundColor': '#FFFFFF'},
        )