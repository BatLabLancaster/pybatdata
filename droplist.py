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

def DroplistHTML(id_,options,value):
    return html.Div([
            dcc.Dropdown(
                id= id_,
                style = {
                    'width': '80%',
                    'textAlign': 'left',
                    'color': '#000000',
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                    'marginLeft': '10%',
                    'marginRight': '10%',
                },
                options= options,
                value= value,
                clearable=False,
            )],
            style = {
                'textAlign': 'left',
                'width': '100%',
            },
        )