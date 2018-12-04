# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html

from mylayouts import *

texts = {
    'title': 'Gluettery',
}
colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

def Header():
    return html.Div(
        children = [
            html.Div(
                children=[TitleLeftHTML(texts['title'],'#FFFFFF','100')],
                style={ 'width': '100%', 'height': '100%',
                'backgroundColor': colors['background'],
                'backgroundImage': 'url(https://www.everynation.org/wp-content/uploads/2018/02/Monthly-Website-Header-background.jpg)'},
            )
        ],
        style = {
                'width': '100%', 'height': '100%',
        }
    )