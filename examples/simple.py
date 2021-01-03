'''
Simple pyCIR usage example.
'''

import pycir

x = [8, 12, 16, 18]
y = [0.4, 0.7, 0.6, 0.8]
wt = [50, 40, 20, 45]

output = pycir.cirPAVA(y=y, x=x, wt=wt, full=True)