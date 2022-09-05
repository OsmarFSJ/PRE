###### FIGURES ######


	Each folder named "Figure" contain:


		(i) One ".pdf" file: 

			Plot.

		(ii) One ".dat" files for each curve:

			Values arranged in 3 columns.

			Each line represents a single point and displays:

				x-value (parameter), y-value (mean) and y-bar (error).
		
		(iii) One ".py" file:
	
			Python3 script to reproduce the plot.
		
			Requires Matplotlib:

				Ubuntu systems installation trough terminal:
			
					~ sudo apt-get install python3-matplotlib
			
			



###### SIMULATIONS ######


	The remaining folders refer to the codes to perform simulations.


	We used 03 (three) distinct codes:
		(MA) Number of maxima: calculates the average value of the number of local optima of fitness landscapes.
		(MO) Moving-optimum: This is main code. It is used to generate the adaptive walks alongside the dynamics of environmental change
		(QS) Quasi-static: It presents an alternative mode of the main dynamics.


	Source dynamics and figures map as follows:

		FIGURE		DYNAMICS
		1		MO
		2		MO & MA
		3		MO
		4		MO
		5		MO
		6		MO
		7		MO & QS
	

	They contain:

		(1) One ".cpp" file:
	
			C++ source code
	
			Requires the GSL scientific library:
		
				Ubuntu systems installation trough terminal:
			
					(C++)	~ sudo apt-get install build-essential
					(GSL)	~ sudo apt-get install gsl-bin
					(GSL)	~ sudo apt-get install libgsl-dev
			
				Ubuntu systems compilation trough terminal:
		
					~ c++ -o3 [source_code_name].cpp -o [executable_name] -lm -lgsl -lgslcblas
	
			After compilation we will get an executable
	
		
			Execution asks terminal input of parameters in the following sequence:
			
				tau
				n
				L
				number of landscapes
				number of dynamics
			
			Produces "data.dat":
			
				Contains (number of landscapes)*(number of dynamics) lines
				
				The j-th evolutionary path realization of the i-th landscape realization is displayed on line ((number of landscapes)*i+j)
			
				
		
		(2) One ".py" file:
		
			Python3 script "mean-error.py"
			
			Execution asks exactly the same input used for "data.dat" production
			
			Produces "[measure_name].dat":
			
				Contains mean and error for the respective measure





###### BOTTOM ######
