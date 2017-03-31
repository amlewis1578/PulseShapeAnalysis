from datascience import *
import os, sys
import numpy as np
from PulseAnalysisFunctions import *



if __name__=='__main__':
	print('\n\nStarting program!\n\n')

## Initialize the tables and thresholds

	int_thshld=200
	fall_thshld=25
	cent_thshld=0.1

	pulses=Table(make_array('TOF','Integral','Integral Bin','Peak','Peak Location','Fall Time','Centroid'))
	pulses_abv_thshld=Table(make_array('TOF','Saturated','Integral','Fall Time','Centroid'))
	


## Read in the pulse info from PulseInfo.txt	
	pulsefile='PulseInfo.txt'
	with open(pulsefile,'r') as f:
		for line in f:
			(pulses,pulses_abv_thshld)=ProcessLine(line,pulses,pulses_abv_thshld,int_thshld,fall_thshld,cent_thshld)
			

## Look at pulses just above centroid threshold
	pulses_abv_cent=pulses_abv_thshld.where('Centroid',True).select('TOF')
	pulses_abv_cent=pulses_abv_cent.join('TOF',pulses,'TOF')


## Group to find averages
	average_cent_by_integral=pulses.select('Integral Bin','Centroid').group('Integral Bin',np.average)
	print(average_cent_by_integral.take(np.arange(0,15)))
#	average_cent_by_integral.hist()
#	savefig('CentroidsByIntegral.png')

## Find distributions

## Bring in a possible neutron and test

## Prediction?
