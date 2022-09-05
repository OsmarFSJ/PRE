#################### Header ####################


#	05/07/2022

#	Diego Cavalcante Cirne
#	0000-0003-0315-8690

#	Federal University of Pernambuco
#	Physics Department
#	Evolutionary Dynamics Lab


#################### Library ####################



import math
import matplotlib.pyplot as plt
import os



#################### Form ####################



SMA = 14
MED = 18
BIG = 20



sep = ''



#################### Main ####################



fig = plt.figure()



plt.subplot(2, 3, 1)


arq = open('S-1_tau-2.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [int(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
Z = [float(dat[i][2]) for i in range(len(dat))]


Y2 = [cel for cel in Y]
Y2.sort()
Z2 = []


for i in range(len(Y2)):


	pos = Y.index(Y2[i])
	Z2.append(Z[pos])


Xtic = [sep.join(('$L$', str(X[i]+1))) for i in range(len(X))]
Xtic[-1] = '$GO$'


col = ['orange' for j in range(len(X))]
col[-1] = 'blue'


plt.bar(X, Z2, color=col)
plt.title(sep.join(('$\\tau$ = 2')), size=BIG)
plt.ylabel('Accessibility (sample 1)', rotation='vertical', size=BIG)
plt.xticks(X, Xtic, fontsize=10)
plt.ylim([pow(10, -5), pow(10, 0)])
plt.yscale('log')



plt.subplot(2, 3, 2)


arq = open('S-1_tau-10.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


Y = [float(dat[i][1]) for i in range(len(dat))]
Z = [float(dat[i][2]) for i in range(len(dat))]


Y2 = [cel for cel in Y]
Y2.sort()
Z2 = []


for i in range(len(Y2)):


	pos = Y.index(Y2[i])
	Z2.append(Z[pos])


plt.bar(X, Z2, color=col)
plt.title(sep.join(('$\\tau$ = 10')), size=BIG)
plt.xticks(X, Xtic, fontsize=10)
plt.ylim([pow(10, -5), pow(10, 0)])
plt.yscale('log')



plt.subplot(2, 3, 3)


arq = open('S-1_tau-200.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


Y = [float(dat[i][1]) for i in range(len(dat))]
Z = [float(dat[i][2]) for i in range(len(dat))]


Y2 = [cel for cel in Y]
Y2.sort()
Z2 = []


for i in range(len(Y2)):


	pos = Y.index(Y2[i])
	Z2.append(Z[pos])


plt.bar(X, Z2, color=col)
plt.title(sep.join(('$\\tau$ = 200')), size=BIG)
plt.xticks(X, Xtic, fontsize=10)
plt.ylim([pow(10, -5), pow(10, 0)])
plt.yscale('log')


plt.subplot(2, 3, 4)


arq = open('S-2_tau-2.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [int(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
Z = [float(dat[i][2]) for i in range(len(dat))]


Y2 = [cel for cel in Y]
Y2.sort()
Z2 = []


for i in range(len(Y2)):


	pos = Y.index(Y2[i])
	Z2.append(Z[pos])


Xtic = [sep.join(('$L$', str(X[i]+1))) for i in range(len(X))]
Xtic[-1] = '$GO$'


col = ['orange' for j in range(len(X))]
col[-1] = 'blue'


plt.bar(X, Z2, color=col)
plt.title(sep.join(('$\\tau$ = 2')), size=BIG)
plt.ylabel('Accessibility (sample 2)', rotation='vertical', size=BIG)
plt.xticks(X, Xtic, fontsize=10)
plt.ylim([pow(10, -5), pow(10, 0)])
plt.yscale('log')



plt.subplot(2, 3, 5)


arq = open('S-2_tau-10.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


Y = [float(dat[i][1]) for i in range(len(dat))]
Z = [float(dat[i][2]) for i in range(len(dat))]


Y2 = [cel for cel in Y]
Y2.sort()
Z2 = []


for i in range(len(Y2)):


	pos = Y.index(Y2[i])
	Z2.append(Z[pos])


plt.bar(X, Z2, color=col)
plt.title(sep.join(('$\\tau$ = 10')), size=BIG)
plt.xticks(X, Xtic, fontsize=10)
plt.ylim([pow(10, -5), pow(10, 0)])
plt.yscale('log')



plt.subplot(2, 3, 6)


arq = open('S-2_tau-200.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


Y = [float(dat[i][1]) for i in range(len(dat))]
Z = [float(dat[i][2]) for i in range(len(dat))]


Y2 = [cel for cel in Y]
Y2.sort()
Z2 = []


for i in range(len(Y2)):


	pos = Y.index(Y2[i])
	Z2.append(Z[pos])


plt.bar(X, Z2, color=col)
plt.title(sep.join(('$\\tau$ = 200')), size=BIG)
plt.xticks(X, Xtic, fontsize=10)
plt.ylim([pow(10, -5), pow(10, 0)])
plt.yscale('log')



fig.set_size_inches(18, 12, forward=True)
plt.savefig('figure-3.pdf')



#################### Bottom ####################
