#################### Header ####################


#	05/07/2022

#	Diego Cavalcante Cirne
#	0000-0003-0315-8690

#	Federal University of Pernambuco
#	Physics Department
#	Evolutionary Dynamics Lab


#################### Library ####################



import math
import os



#################### Form ####################



print()



ide =	[	'phe.N'
	,	'gen.N'
	]



num =	[	[int(input('n:\t'))]
	,	[int(input('L:\t'))]
	]



phe_N =		0
gen_N =		1



print()



sam_l = int(input('number of landscapes:\t'))


sur =	'maximum-abundance'



fol =	os.getcwd()
rea =	'/data.dat'
wri =	'/mean-error_?.dat'
sep =	''



print()



#################### Functions ####################



def linearization(num):


	siz = []


	for i in range(len(num)):


		siz.append(len(num[i]))


	pro = 1


	for i in range(len(siz)):
	
	
		pro *= siz[i]


	tab = []
	

	for i in range(pro):


		par = []
		quo = i
		
		
		for j in range(len(num)):


			par.append(num[len(num)-j-1][quo%siz[len(num)-j-1]])
			quo //= siz[len(num)-j-1]

		
		par.reverse()
		tab.append(par)


	return tab



def binarycoefficients(gen_N, par):


	coe = []
			
			
	for i in range(pow(2, par[gen_N])):
			
			
		aux = []
		quo = i
				
				
		for j in range(par[gen_N]):
				
				
			aux.append(quo % 2)
			quo //= 2
				
		
		aux.reverse()
		coe.append(aux)


	return coe



def hammingdistance(gen_N, par, coe):


	ham = [[0 for j in range(pow(2, par[gen_N]))] for i in range(pow(2, par[gen_N]))]


	for i in range(pow(2, par[gen_N])):
			
			
		for j in range(i):
			
			
			for k in range(par[gen_N]):
					
					
				if coe[j][k] != coe[i][k]:
						
						
					ham[i][j] += 1
						
						
				ham[j][i] = ham[i][j]


	return ham



#################### Main ####################



tab = linearization(num)



for par in tab:


	fil = sep.join((fol, rea))
	

	if os.path.exists(fil):


		arq = open(fil, 'r')
		dat = arq.readlines()
		arq.seek(0, 0)


		if len(dat) == sam_l:
		
		
			del dat


			ave = 0
			err = 0


			for lan in range(sam_l):


				mea = int(arq.readline().split()[0])
				
				
				ave += mea
				err += mea**2


			ave /= sam_l
			err /= sam_l
			err = math.sqrt(err - ave**2)


			arq2 = open(sep.join((fol, '/', sur, '.dat')), 'w')
			arq2.writelines(sep.join(('mean', '\t', 'error', '\n')))
			arq2.writelines(sep.join((str(ave), '\t', str(err))))
			arq2.close()


		arq.close()



#################### Bottom ####################
