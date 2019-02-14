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
