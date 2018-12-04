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

def ImageHTML(fig):
    return html.Img(src='data:image/png;base64,{}'.format(fig))