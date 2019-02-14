# Structure and content of the Footage
import dash
import dash_html_components as html
from .mylayouts import SubTitleHTML

texts = {
    'bye': 'Thanks for using Gluttery',
    'creators': 'https://github.com/BatLabLancaster/batlab_dash',
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
        SubTitleHTML(texts['bye'],'#FFFFFF','28'),
        SubTitleHTML(texts['creators'],'#FFFFFF','28'),
    ])
