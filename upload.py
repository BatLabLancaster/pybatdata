import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),
                error_bad_lines = False)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(
                io.BytesIO(decoded),
                error_bad_lines = False)
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(
            children=['Opened file: ',filename],
            style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                }
            ),
        html.H6(
            children= ['Opened at: ',datetime.datetime.fromtimestamp(date)],
            style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'bold',
                }
            ),
    ])

def UploadTextHTML():
    return html.Div([
                '\"Drag and Drop\" or ',
                html.A('Select Files')
            ])

def UploadHTML(id_):
    return html.Div([
        dcc.Upload(
            id=id_,
            children= UploadTextHTML(),
            style={
                'width': '100%',
                'height': '100%',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    ])