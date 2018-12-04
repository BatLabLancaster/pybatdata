# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy
import scipy
import scipy.signal

from utils import *

from analysisselect import *
from plotinfoselect import *
from ackandcreators import *
from mylayouts import *
from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

import os, re, Defs
from Defs import *
from utils import *

Novonix_Table = ["Time","Current (A)","Potential (V)","Capacity (Ah)","Temperature (C)","Circuit Temperature (C)","Coulombic Efficiency (Fg-1)/(Cycle number)","Differential Voltage Analysis (A/V)"]

CURRENT      = 5
POTENTIAL    = 6
CAPACITY     = 7
TEMPERATURE  = 8
CIRCUIT_TEMP = 9
COULUMBIC 	 = 10
DVA 		 = 11

def CoulombicEfficiency(file,title,xlabel,ylabel):
	if xlabel != '':
		plotx = xlabel
	else:
		plotx = 'Cycle Number'
	if ylabel != '':
		ploty = ylabel
	else:
		ploty = 'Coulombic Efficiency (%)'
	
	X = []
	Y = []

	x = []
	y = []

	charge, discharge = [], []
	cycle = 1

	i = 0
	nrows = len(file)
	while i < nrows:
		while( i < nrows and cycle == -int(file[i]['Cycle Number'])):
			value = float(file[i]['Capacity (Ah)'])

			if( int(file[i]['Cycle Number']) < 0 and value != 0):
				discharge.append(value)

			i += 1

		cycle += 1

		while( i < nrows and cycle == int(file[i]['Cycle Number'])):
			value = float(file[i]['Capacity (Ah)'])

			if( int(file[i]['Cycle Number']) > 0):
				charge.append(value)

			i += 1

		# d. incrementing the cycle
		x.append(cycle-1)
		if(len(discharge) > 1 and len(charge) > 1 and (max(discharge)-min(discharge)) != 0):	
			print(len(discharge),len(charge),((max(charge)-min(charge))/(max(discharge)-min(discharge)))*100)
			y.append(((max(charge)-min(charge))/(max(discharge)-min(discharge)))*100)

		charge, discharge = [], []

	print('finish')
	return  html.Div([
	    dcc.Graph(
	        id='graph',
	        figure={
	            'data': [
	                {
	                	'x': x,
	                    'y': y,
	                    'name': 'Trace 1',
	                    'mode': 'lines+markers',
	                    'marker': {'size': 12}
	                }
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

def differentiate(V, Q):
	dVdQ = []
	plotx = []
	V = pd.Series(V)
	Q = pd.Series(Q)
	# Applies a moving average filter
	V_smooth = pd.Series.rolling(V, 1).mean() 
	Q_smooth = pd.Series.rolling(Q, 1).mean()

	#differentiting
	dV = numpy.diff(V)
	dQ = numpy.diff(Q)
	dVdQ = dV/dQ

	#applies a gaussian filter and a convolution 
	g = scipy.signal.gaussian(min(40, len(Q)-1), 2.5)
	g = g/sum(g)
	dVdQ_gaus = numpy.convolve(dVdQ, g, mode='same')

	return dVdQ_gaus

def DVA(file,title,xlabel,ylabel,cycles):
	cycle_test = 1

	if xlabel != '':
		plotx = xlabel
	else:
		plotx = 'Capacity (Ah)'
	if ylabel != '':
		ploty = ylabel
	else:
		ploty = 'dV/dQ'
	
	X, Y = [], []
	Q, V = [], []
	dQdV = []
	cycle, cur_file = 1, 1

	i = 0
	nrows = len(file)
	while i < nrows:
		while( i < nrows and cycle ==  abs(int(file[i]['Cycle Number']))):
			valueQ = float(file[i]['Capacity (Ah)'])
			valueV = float(file[i]['Potential (V)'])

			if(int(file[i]['Cycle Number']) > 0 and valueQ != 0 and valueV != 0):
				Q.append(valueQ)
				V.append(valueV)

			i += 1

		cycle = cycle + 1
		if(len(Q) > 3 and len(V) > 3 and any([t != Q[0] for t in Q]) ):
			window_size= max([3, round(len(V)/50) if round(len(V)/50) % 2 != 0 else round(len(V)/50)+1])
			dVdQ = differentiate(V, Q)

			if((int(cycle)-2) in cycles):
				X.append(Q[1:len(Q)])
				Y.append(dVdQ)
				
		V, Q, dVdQ = [], [], []

	if len(X) > 0:
		return html.Div([
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
					                for i in range(len(X))
					            ],
					            'layout':{
					        		'title':title,
				            		'xaxis': {
				            			'title':plotx,
				            			'size':18,
				            			'family':'Roboto Condensed Bold',
				            		},
				            		'yaxis': {
				            			'title':ploty,
				            			'size':18,
				            			'family':'Roboto Condensed Bold',
				            		}
				            	}
					        }
					    )
				    ])
	else:
		return None