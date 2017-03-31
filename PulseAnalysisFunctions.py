from datascience import *
import os, sys
import numpy as np


def ProcessLine(line,pulses,pulses_abv_thshld,int_thshld,fall_thshld,cent_thshld):
	'''Function to process each line in the pulseinfo file and fill in the tables'''

	#split up line into information
	line=line.split()
	TOF=line[0]
	integral=float(line[1])
	peak_location=int(line[2])
	peak=float(line[3])
	centroid=float(line[4])
	fall_time=int(line[5])

	#determine if saturated and calculated integral bin
	saturated = (peak>=250)
	integral_bin=(np.round(integral/100))*100

	#determine if above thresholds
	above_integral = integral>=int_thshld
	above_falltime = fall_time>=fall_thshld
	above_centroid = centroid>=cent_thshld

	#populate tables
	pulses=pulses.with_row([TOF,integral,integral_bin,peak,peak_location,fall_time,centroid])
	pulses_abv_thshld=pulses_abv_thshld.with_row([TOF,saturated,above_integral,above_falltime,above_centroid])


	return (pulses,pulses_abv_thshld)
