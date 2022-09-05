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



#################### Main ####################



fig = plt.figure()



plt.subplot(2, 2, 1)


arq = open('A_L-4.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$L$ = 4', color='tab:blue', marker='o', linewidth=1)


arq = open('A_L-8.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$L$ = 8', color='tab:green', marker='o', linewidth=1)


arq = open('A_L-12.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$L$ = 12', color='orangered', marker='o', linewidth=1)


plt.xlabel('$\\tau$', size=BIG)
plt.ylabel('mean walk length', size=BIG, labelpad=BIG)
plt.xticks(size=SMA)
plt.yticks(size=SMA)
plt.xlim([1, 1024])
plt.ylim(3.5, 14)
plt.xscale('log')
#plt.yscale('log')
plt.legend(shadow=False, frameon=False, prop={'size': MED})



plt.subplot(2, 2, 2)


arq = open('B_n-4.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$n$ = 4', color='tab:blue', marker='o', linewidth=1)


arq = open('B_n-8.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$n$ = 8', color='tab:green', marker='o', linewidth=1)


arq = open('B_n-12.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$n$ = 12', color='orangered', marker='o', linewidth=1)


plt.xlabel('$\\tau$', size=BIG)
plt.ylabel('mean walk length', size=BIG, labelpad=BIG)
plt.xticks(size=SMA)
plt.yticks(size=SMA)
plt.xlim([1, 1024])
plt.ylim(3.5, 14)
plt.xscale('log')
#plt.yscale('log')
plt.legend(shadow=False, frameon=False, prop={'size': MED})



plt.subplot(2, 1, 2)


arq = open('C_n-4.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$n$ = 4', color='tab:blue', marker='o', linewidth=1)


arq = open('C_n-8.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$n$ = 8', color='tab:green', marker='o', linewidth=1)


arq = open('C_n-12.dat', 'r')
dat = arq.readlines()
dat.pop(0)
dat = [dat[i].split() for i in range(len(dat))]
arq.close()


X = [float(dat[i][0]) for i in range(len(dat))]
Y = [float(dat[i][1]) for i in range(len(dat))]
SY = [float(dat[i][2]) for i in range(len(dat))]


plt.errorbar(X, Y, yerr=SY, xerr=None, capthick=2, capsize=5, label='$n$ = 12', color='orangered', marker='o', linewidth=1)


plt.xlabel('$\\tau$', size=BIG)
plt.ylabel('mean walk length (antipode)', size=BIG, labelpad=BIG)
plt.xticks(size=SMA)
plt.yticks(size=SMA)
plt.xlim([1, 1024])
#plt.ylim()
plt.xscale('log')
#plt.yscale('log')
plt.legend(shadow=False, frameon=False, prop={'size': MED})



fig.set_size_inches(18, 16, forward=True)
fig.savefig('figure-1.pdf')



#################### Bottom ####################
