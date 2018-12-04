# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

def TitleHTML(children,color='#000000',fontSize='64'):
	return html.H1(
            children=children,
            style={
                'textAlign': 'center',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginTop': '35px',
                'marginBot': '35px'
            }
		)

def TitleLeftHTML(children,color='#000000',fontSize='64'):
    return html.H1(
            children=children,
            style={
                'width': '80%', 'height': '100%',
                'textAlign': 'left',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginLeft': '20%',
            }
        )

def SubTitleHTML(children,color='#000000',fontSize='18'):
	return html.P(
            children= children, 
            style={
                'width': '90%', 'height': '100%',
                'textAlign': 'center',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'normal',
                'marginLeft': '5%',
                'marginRight': '5%',
            }
        )

def SubTitleBoldHTML(children,color='#000000',fontSize='18'):
    return html.P(
            children= children, 
            style={
                'width': '90%', 'height': '100%',
                'textAlign': 'center',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginLeft': '5%',
                'marginRight': '5%',
            },
        )

def SectionHTML(children,color='#000000',fontSize='24'):
	return html.H1(
            children= children,
            style={
                'textAlign': 'left',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '35px',
            }
        )

def SectionCenterHTML(children,color='#000000',fontSize='24'):
    return html.H1(
            children= children,
            style={
                'textAlign': 'center',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginTop': '35px',
            }
        )

def SubsectionHTML(children,color='#000000',fontSize='20'):
	return html.H1(
            children= children,
            style={
                'textAlign': 'left',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '15px',
            }
        )

def SubsectionCenterHTML(children,color='#000000',fontSize='20'):
    return html.H1(
            children= children,
            style={
                'textAlign': 'center',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'bold',
                'marginTop': '15px',
            }
        )

def ParagraphHTML(children,color='#000000',fontSize='18'):
	return html.P(
            children= children, 
            style={
                'textAlign': 'justify',
                'color': color,
                'fontFamily': 'Roboto Condensed',
                'fontSize': fontSize,
                'fontWeight': 'normal',
                'margin': '35px',
            }
        )

def SystemAnswerHTML(children,id_):
    return html.H1(
            id = id_,
            children=children,
            style={
                'width': '95%', 'height': '100%',
                'textAlign': 'left',
                'color': '#000000',
                'fontFamily': 'Roboto Condensed',
                'fontSize': '16',
                'marginLeft': '5%',
            }
        )

def ThreeColumnsHTML(children):
    return html.Div([
            html.Div(children=children[0],
                style={'textAlign': 'center','width': '33%', 'display': 'inline-block'}),
            html.Div(children=children[1],
                style={'textAlign': 'center','width': '33%', 'display': 'inline-block'}),
            html.Div(children=children[2],
                style={'textAlign': 'center','width': '33%', 'display': 'inline-block'}),
        ])