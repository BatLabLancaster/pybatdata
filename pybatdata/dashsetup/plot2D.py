import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy
import scipy
import scipy.signal

from .mylayouts import *
from .myinput import InputTextHTML
from .radioitems import RadioItemsHTML
from .droplist import DroplistHTML
from .button import ButtonHTML

def plot2D(dropdown_select,file,title,xlabel,ylabel,cycles,mode):
	if xlabel != '':
		plotx = xlabel
	else:
		plotx = 'Cycle Number'
	if ylabel != '':
		ploty = ylabel
	else:
		ploty = dropdown_select
	
	X, y, Y = [],[], []
	i, cycle, cur_file = 0, 1, 1
	nrows = len(file)
	while i < nrows:
		while( i < nrows and cycle ==  abs(int(file[i]['Cycle Number']))):
			value = float(file[i][dropdown_select])

			if(mode*int(file[i]['Cycle Number']) > 0):
				y.append(value)

			elif(mode*int(file[i]['Cycle Number']) == 0):
				y.append(value)

			i += 1

		# d. incrementing the cycle
		cycle = cycle + 1
		print(cycle)
		if(cycle-2 in cycles):
			X.append(numpy.r_[0:len(y)])
			Y.append(y)

		y = []

	print('finish')
	return  html.Div([
	    dcc.Graph(
	        id='graph',
	        figure={
	            'data': [
	                {
	                	'x': X[i],
	                    'y': Y[i],
	                    'mode': 'lines+markers',
	                    'marker': {'size': 12},
	                    'name': 'Cycle {}'.format(cycles[i]),
	                }
					for i in range(len(Y))
	            ],
	            'layout':{
	        		'title':title,
            		'xaxis': {
            			'title':plotx,
            			'size':18,
            			'family':'Roboto Condensed Bold'
            		},
            		'yaxis': {
            			'title':ploty,
            			'size':18,
            			'family':'Roboto Condensed Bold'
            		}
            	}
	        }
	    )
    ]
    )
