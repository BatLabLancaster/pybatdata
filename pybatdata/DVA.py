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
