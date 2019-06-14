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
