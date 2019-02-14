# Structure for a drop-down menu
import dash
import dash_core_components as dcc
import dash_html_components as html

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
