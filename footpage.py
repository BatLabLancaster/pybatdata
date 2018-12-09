# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html

from mylayouts import *
from image import *

images = {
}

texts = {
    'bye': 'Thanks to use Gluttery',
    'creators': 'CREATORS',
    'alana': ['Technical expertise in Interfacial electrochemistry, Electrocatalysis, Development and Characterization of materials for energy conversion/storage. Project Design and Management.'],
    'caio': ['<TO DO>'],
    'micanga': ['Computer Science researcher currently working with Cooperative Game Theory. Diverse background and interest in the hottest areas (e.g., Data Forecasting and General Problem Design).'],
}

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

def FootPage():
    return html.Div(style={ 'width': '100%', 'height': '100%',
            'backgroundColor': colors['background'],
            'backgroundImage': 'url(https://www.everynation.org/wp-content/uploads/2018/02/Monthly-Website-Header-background.jpg)'},
        children = [
        TitleHTML(texts['bye'],'#FFFFFF','32'),
        TitleHTML(texts['creators'],'#FFFFFF','32'),
    ])