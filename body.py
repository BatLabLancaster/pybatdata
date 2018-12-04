# -*- coding: utf-8 -*-
# System and Standard Libraries
import base64
import datetime
import io

# Dash Python - HTML Interface Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

# Dash Python - My HTML Interface
from mylayouts import *
from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

texts = {
    'introduction': ['Welcome to the Gluettery platform.',
                    'This platform was created in order to facilitate and stimulate the production of interactive graphics of battery-related data. ',
                    'As an open source platform, all collaboration and tips are more than welcome. ',
                    '\"Obrigado e de nada\"! '],
    'section1': '1. Select your file',
    'section2': '2. Select your analysis',
    'subsec2a': 'a) Data analysis',
    'subsec2b': 'b) Cycles',
    'subsec2c': 'c) Data and Cycle Type',
    'section3': '3. Enter your plot information',
    'subsec3a': 'a) Plot Title',
    'subsec3b': 'b) X Label',
    'subsec3c': 'c) Y Label',
}
colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

def BodyIntro():
    return html.Div(
        children = [Introduction()],
        style = {'width': '100%', 'height': '100%'}
    )

def Body():
    return html.Div(
        children = [
            # Section 1
            #- File Selection and Load
            Select_File(),

            # Section 2
            #- Analysis Parameters Selection
            Select_Analysis(),
            Select_Analysis_Cycle(),
            Select_Analysis_Radio(True,'A'),

            # Section 3
            #- Plot Information Selection
            Select_Plot_Information(),

            # Plot Button
            ButtonHTML('PLOT','plot_button'),
            html.Div(id='plot_click'),
        ], style={ 
                'width': '60%',
                'height': '90%',
                'marginLeft': '20%',
                'marginRight': '20%',
                'marginTop': '5%',
                'marginBotton': '5%',
                'borderWidth': '1px',
                'borderStyle': 'outset',
                'borderRadius': '5px',
                'backgroundColor': colors['background'],
            }, 
    )



def Introduction():
    return html.Div(
                children=[
                    SubTitleBoldHTML(texts['introduction'][0]),
                    SubTitleHTML(texts['introduction'][1]),
                    SubTitleHTML(texts['introduction'][2]),
                    SubTitleBoldHTML(texts['introduction'][3]),
                ], style={ 'width': '60%', 'height': '95%',
                    'marginLeft': '20%',
                    'marginRight': '20%',
                    'marginTop': '5%',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                    'backgroundColor': colors['background'],
                }, 
        )

def Select_File():
    return html.Div(
                [html.Div(
                    [SectionHTML(texts['section1'])],
                    style={ 'width': '100%', 
                            'height': '100%',
                            'backgroundColor': colors['background'],
                            }
                    ),
                html.Div(
                    [UploadHTML('upload-data')],
                    style={ 'width': '50%', 
                            'height': '100%',
                            'backgroundColor': colors['background'],
                            'marginLeft': '25%', 'marginRight': '25%'
                            }
                    )]
                )

def Select_Analysis():
    return html.Div([
        SectionHTML(texts['section2']),
        SubsectionHTML(texts['subsec2a']),
        DroplistHTML('analysis-dropdown',
                    [{'label': 'Differential Voltage Analysis (DVA)', 'value': 'DVA'},
                    {'label': 'Coulombic Efficiency (CE)', 'value': 'CE'}],
                    'DVA'),
    ])

def Select_Analysis_Cycle():
    return html.Div(
        id = 'analysis-cycle',
        children = [
            SubsectionHTML(texts['subsec2b']),
            InputTextHTML('cycles-input','Select Cycles to evaluate... single: "1", multi: "1, 3, 5", range: "1-5"'),
            SystemAnswerHTML('Selected Cycles = Empty','cycles-select'),
            SystemAnswerHTML('* Unnecessary for: Coulombic Efficiency plot.','cycles-select-un')
        ])

def Select_Analysis_Radio(radio_flag,radio):
    if radio_flag:
        return html.Div(
            id = 'analysis-radio',
            children = [
                SubsectionHTML(texts['subsec2c']),
                RadioItemsHTML(radio_flag,radio)
            ])
    else:
        return html.Div(
            id = 'analysis-radio',
            children = [
                RadioItemsHTML(radio_flag,radio)
            ])

def Select_Plot_Information():
    column1 = [SubsectionCenterHTML(texts['subsec3a']),InputTextHTML('title-input','Title here...')]
    column2 = [SubsectionCenterHTML(texts['subsec3b']),InputTextHTML('xlabel-input','X label here...')]
    column3 = [SubsectionCenterHTML(texts['subsec3c']),InputTextHTML('ylabel-input','Y label here...')]
    return html.Div([
        SectionHTML(texts['section3']),
        ThreeColumnsHTML([column1,column2,column3]),
    ])