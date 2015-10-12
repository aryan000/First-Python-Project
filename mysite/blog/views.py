from django.shortcuts import render

# Create your views here.
from matplotlib import pylab
from pylab import *

def graph() :
	x = [1,2,3,4,5,6]
	y = [5,2,6,8,2,7]
	plot(x,y,linewidth=2)

	xlabel('x axis')
	ylabel(' y asis')
	title('sample graph')
	grid(True)
	pylab.show()

 
