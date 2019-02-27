# Application structure

# Dash Python - HTML Interface Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

from ..iobat.test_file import test_file
from ..iobat.fileclass import fileclass

# Dash Python - My HTML Interface
from .mylayouts import *
from .myinput import InputTextHTML,InputPathHTML
from .radioitems import RadioItemsHTML
from .droplist import DroplistHTML
from .button import ButtonHTML

texts = {
    'introduction': ['Welcome to the Gluettery platform.',
                    'This platform was created in order to facilitate and stimulate the production of interactive graphics of battery-related data. ',
                    'As an open source platform, all collaboration and tips are more than welcome. ',
                    '\"Obrigado e de nada\"! '],
    'section1': '1. Path to your file',
    'subsec1a': 'Once you have introduced the path, press Enter',
    'section2': '2. Select your analysis',
    'subsec2a': 'a) Type of analysis:',
    'subsec2b': 'b) Cycles to be evaluated:',
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
            'height': '85%',
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
    text_path = "C:\\path\\2\\file   or   C:/path/2/file"
    return html.Div([
        SectionHTML(texts['section1']),
        SubTitleHTML(texts['subsec1a']),
        InputPathHTML('path2file-input',text_path),
        html.Div(id='path2file-submit',
                 style={
                     'textAlign': 'center',
                     'color': colors['text'],
                     'fontFamily': 'Roboto Condensed',
                            'fontSize': '16',
                     'fontWeight': 'normal',
                 }
        )
                ])

def File_Info():
    filename = fileclass.name

    if (filename is None or filename == ""):
        return u'''No path to file has been input yet.'''
    else:
        test_file(dash=True)
        print('fileclass.problem ={}'.format(fileclass.problem))
        if fileclass.problem:
            return u'''There was an error processing "{}"'''.format(filename)
        else:
            return u'''File: "{}", Tester: "{}"'''.format(filename,fileclass.tester)

def Select_Analysis():
    return html.Div([
        SectionHTML(texts['section2']),
        SubsectionHTML(texts['subsec2a']),
        DroplistHTML('analysis-dropdown',
                    [{'label': 'Current (A)', 'value': 'Current (A)'},
                     {'label': 'Potential (V)', 'value': 'Potential (V)'},
                     {'label': 'Capacity (Ah)', 'value': 'Capacity (Ah)'},
                     {'label': 'Temperature (°C)', 'value': "Temperature (°C)"},
                     {'label': 'Circuit Temperature (°C)', 'value': "Circuit Temperature (°C)"},
                     {'label': 'Energy (Wh)', 'value': 'Energy (Wh)'},
                     {'label': 'Differential Voltage Analysis (DVA)', 'value': 'Differential Voltage Analysis (DVA)'},
                     {'label': 'Coulombic Efficiency (CE)', 'value': 'Coulombic Efficiency (CE)'}],
                    ''),
    ])

def Select_Analysis_Cycle():
    return html.Div(
        id = 'analysis-cycle',
        children = [
            SubsectionHTML(texts['subsec2b']),
            InputTextHTML('cycles-input','Single: "1"; Multi: "1, 3, 5", Range: "1-5"'),
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
