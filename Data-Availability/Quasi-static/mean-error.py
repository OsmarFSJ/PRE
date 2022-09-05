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



ide =	[	'phe.rou_div'
	,	'phe.mut_sig'
	,	'phe.N'
	,	'gen.N'
	]



num =	[	[int(input('tau:\t'))]
	,	[float(input('sigma:\t'))]
	,	[int(input('n:\t'))]
	,	[int(input('L:\t'))]
	]



phe_rou_div =	0
phe_mut_sig =	1
phe_N =		2
gen_N =		3



print()



sam_l = int(input('number of landscapes:\t'))
sam_d = int(input('number of dynamics:\t'))



sur = 	[	'endpoint-predictability'
	,	'endpoint-entropy'
	,	'length'
	,	'path-predictability'
	,	'divergence'
	,	'length_antipode'
	,	'path-predictability_antipode'
	,	'divergence_antipode'
	]



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



def contraction(lin):


	pat = []
	pat.append(lin[0])


	for i in range(len(lin)):


		if lin[i] != pat[-1]:


			pat.append(lin[i])


	return pat



def sorting(pats, arr):


	fres = []


	dis = 0
		
						
	while len(pats)!=dis:
								
								
		pos = []
							
							
		for i in range(dis+1, len(pats)):
						
						
			if pats[i] == pats[dis]:
						
						
				pos.append(i)
								
								
		for i in range(len(pos)):
						

			pats.pop(pos[i]-i)
			arr.pop(pos[i]-i)
						
						
		fres.append(len(pos)+1)
			
							
		dis += 1


	return pats, fres, arr



def endpointfilter(pats, fres, pos, end):


	loc_pats = []
	loc_fres = []


	for i in range(len(pats)):
				
				
		if pos[i] == end:
				
				
			loc_pats.append(pats[i])
			loc_fres.append(fres[i])


	return loc_pats, loc_fres



def length(pats, fres):


	sur = 0
	
	
	for i in range(len(pats)):
	
	
		sur += fres[i]*len(pats[i])


	sur /= sum(fres)


	return sur



def predictability(att):


	sur = 0


	for i in range(len(att)):
				
				
		sur += att[i]**2


	sur /= sum(att)**2


	return sur



def pathpredictability(gen_N, par, att):


	sur = 0


	for end in range(pow(2, par[gen_N])):
				
				
		if att[end]:
					
			
			loc_pats, loc_fres = endpointfilter(pats, fres, arr, end)


			sur += att[end]*predictability(loc_fres)
	
	
	sur /= sum(att)


	return sur



def entropy(att):


	sur = 0


	for i in range(len(att)):
			
				
		if att[i]:
		
		
			sur += att[i]*math.log(att[i])


	sur /= sum(att)
	sur *= (-1)
	sur += math.log(sum(att))


	return sur
	
	

def pairwisedivergence(ham, loc_pats):


	loc_pats2 = []


	for i in range(len(loc_pats)):
	
	
		pat = [int(loc_pats[i][j]) for j in range(len(loc_pats[i]))]
		pat.pop(0)
		pat.pop(-1)
		
		
		loc_pats2.append(pat)


	pai = [[0 for j in range(len(loc_pats))] for i in range(len(loc_pats))]


	for i in range(len(loc_pats2)):
						
							
		for j in range(len(loc_pats2)):
							
								
			if i!=j and len(loc_pats2[i]) and len(loc_pats2[j]):
							
							
				for k in range(len(loc_pats2[i])):
								
								
					dis = []
										
										
					for l in range(len(loc_pats2[j])):
										
										
						dis.append(ham[loc_pats2[i][k]][loc_pats2[j][l]])


					pai[i][j] += min(dis)


	return pai



def divergence(loc_pats, loc_fres, pai):


	div = 0
						
						
	for i in range(len(loc_pats)):
						
						
		for j in range(i):
						
						
			div += (pai[i][j]+pai[j][i])*loc_fres[i]*loc_fres[j]/(len(loc_pats[i])-1+len(loc_pats[j])-1)
								
							
	div /= sum(loc_fres)**2
	div *= 2


	return div



def meandivergence(gen_N, par, att):


	sur = 0


	for end in range(pow(2, par[gen_N])):
				
				
		if att[end]:
					
			
			loc_pats, loc_fres = endpointfilter(pats, fres, arr, end)
			pai = pairwisedivergence(ham, loc_pats)
			div = divergence(loc_pats, loc_fres, pai)


			sur += att[end]*div
	
	
	sur /= sum(att)


	return sur



#################### Main ####################



tab = linearization(num)



for par in tab:


	fil = sep.join((fol, rea))
	
	
	if os.path.exists(fil):
	

		arq = open(fil, 'r')
		dat = arq.readlines()


		if len(dat) == sam_l*sam_d:


			del dat


			coe = binarycoefficients(gen_N, par)
			ham = hammingdistance(gen_N, par, coe)


			ave = [0 for i in range(len(sur))]
			err = [0 for i in range(len(sur))]


			arq.seek(0, 0)


			for lan in range(sam_l):


				att = [0 for i in range(pow(2, par[gen_N]))]


				for dyn in range(sam_d):
				
				
					end = int(arq.readline().split()[-1])
					att[end] += 1


				mea = [0 for i in range(len(sur))]
				

				mea[0] += predictability(att)
				mea[1] += entropy(att)

					
				for i in range(0, 2):
	
	
					ave[i] += mea[i]
					err[i] += mea[i]**2


			for i in range(0, 2):


				ave[i] /= sam_l
				err[i] /= sam_l
				err[i] = math.sqrt((err[i] - ave[i]**2)/sam_l)


			arq.seek(0, 0)


			sam_el = 0


			for lan in range(sam_l):


				pats = []
				arr = []
				att = [0 for i in range(pow(2, par[gen_N]))]


				for dyn in range(sam_d):
				
				
					lin = arq.readline().split()
					end = int(lin[-1])
					pat = contraction(lin)

					
					if len(pat)>1:


						pats.append(pat)
						arr.append(end)
						att[end] += 1


				pats, fres, arr = sorting(pats, arr)


				if sum(fres) == sam_d:
				
				
					sam_el += 1
					mea = [0 for i in range(len(sur))]


					mea[2] += length(pats, fres)
					mea[3] += pathpredictability(gen_N, par, att)
					mea[4] += meandivergence(gen_N, par, att)

					
					for i in range(2, 5):
	
	
						ave[i] += mea[i]
						err[i] += mea[i]**2

			
			if sam_el:


				for i in range(2, 5):


					ave[i] /= sam_el
					err[i] /= sam_el
					err[i] = math.sqrt((err[i] - ave[i]**2)/sam_el)


			arq.seek(0, 0)


			sam_el = 0


			for lan in range(sam_l):


				pats = []
				arr = []
				att = [0 for i in range(pow(2, par[gen_N]))]


				for dyn in range(sam_d):
				
				
					lin = arq.readline().split()
					end = int(lin[-1])
					pat = contraction(lin)

					
					if len(pat)>1:


						pats.append(pat)
						arr.append(end)
						att[end] += 1


				if att[-1]:
				
				
					pats, fres, arr = sorting(pats, arr)


					if sum(fres) == sam_d:


						sam_el += 1
						mea = [0 for i in range(len(sur))]
							

						loc_pats, loc_fres = endpointfilter(pats, fres, arr, pow(2, par[gen_N])-1)
						pai = pairwisedivergence(ham, loc_pats)


						mea[5] += length(loc_pats, loc_fres)
						mea[6] += predictability(loc_fres)
						mea[7] += divergence(loc_pats, loc_fres, pai)

					
						for i in range(5, 8):
	
	
							ave[i] += mea[i]
							err[i] += mea[i]**2


			if sam_el:


				for i in range(5, 8):


					ave[i] /= sam_el
					err[i] /= sam_el
					err[i] = math.sqrt((err[i] - ave[i]**2)/sam_el)


			for i in range(len(sur)):
				
				
				arq2 = open(sep.join((fol, '/', sur[i], '.dat')), 'w')
				arq2.writelines(sep.join(('mean', '\t', 'error', '\n')))
				arq2.writelines(sep.join((str(ave[i]), '\t', str(err[i]))))
				arq2.close()


		arq.close()



#################### Bottom ####################
