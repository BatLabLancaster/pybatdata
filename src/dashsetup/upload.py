import datetime

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from ..iobat.test_file import test_file

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def parse_contents(contents, filename, date):
    df = test_file(contents, filename, date)
        
    print (date, date is not None)
    return html.Div([
        html.H5(
            children=['File name: ',filename],
            style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                }
            ),
        html.H6(
            children= ['Last modified: {}'.format((datetime.datetime.fromtimestamp(date)).strftime('%x %X')) if date is not None else None],
            style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '16',
                    'fontWeight': 'normal',
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
