Readme for pulse shape analysis.

Running codes on the virtual machine for now.

The project description:


The final independent data investigation can be completed in pairs and is expected to required 10-20 hours of work. The purpose of the investigation is to apply what you've learned to some data set of your choosing. Investigations will require the following elements. Correct execution of every element is sufficient for full credit. You will present your investigation during RRR week to the course staff.


Choose and describe a data set that includes at least two tables, some quantitative variable, and some categorical variable.

Visualize some quantitative variable(s) of the data in a way that summarizes the data effectively and write a short observational description.

Visualize some categorical variable(s) of the data in a way that summarizes the data effectively and write a short observational description.

Summarize some aspect of the data in a table that involves grouping or pivoting and write a short observational description.

Summarize some aspect of the data in a table that involves joining the two tables and write a short observational description.

State a hypothesis related to the data and the corresponding null hypothesis.

Perform a statistical test for the hypothesis and write a short conclusion.

Describe a prediction problem related to the data.

Apply a prediction technique to the problem and briefly justify your choice of approach.

Evaluate the prediction technique quantitatively and write a short conclusion.




Using just the Cs-137 data

Run through with C++ and calculate:
	peak (implement threshold)
	integral
	fall time
	peak location
	centroid
	which integral bin it falls into (by 100)

	
Identify each pulse by the time stamp

Tables:
Every table has timestamp identifier


Table of identifier and values
Table of identifier, if integral above threshold1
Table of identifier, if centroid above threshold2
Table of identifier, if fall time below threshold 3

This way, can easy test with different groups of data easily

Grouping- find average centroid/fall location/ fall time per integral bin





Test- how high does the centroid have to be in order to say with 1% accuracy that is a neutron?

