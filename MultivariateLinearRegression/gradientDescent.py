from math import sqrt
from random import shuffle
f=open("dataset_2","r")
l=f.readlines()
shuffle(l)
x=[]
y=[]

x_test=[]
y_test=[]

for i in l:
	c=i.strip().replace('\n','').split(' ')
	if len(c)==2:
		c=map(float,c)
		c=[1]+c
		x.append(c[:len(c)-1])
		y.append(c[-1])


#s=int(0.8*(len(x)))
#x_test=x[s:]
#x=x[:s]

#y_test=y[s:]
#y=y[:s]


theta=[]
temp=[]
n=len(x[0]) #number of features
m=len(x) #number of training examples
for i in range(n):
	theta.append(0)
	temp.append(0)

#print theta

alpha=0.00003
iterations=100000


for i in range(iterations):
	for j in range(n):
		f=0
		for k in range(m):
			hthetaX=0
			for c in range(n):
				hthetaX=hthetaX+x[k][c]*theta[c]
			f=f+(hthetaX-y[k])*x[k][j]
		temp[j]=theta[j]-(alpha*f)/m
	
	error=0
	for k in range(m):
		pred=0
		for j in range(n):
			pred=pred+theta[j]*x[k][j]
		error=error+(pred-y[k])**2
	
	print sqrt(error/(2*m))
	for j in range(n):
		theta[j]=temp[j]



#theta=gradientDescent(theta,0.001,50)
print theta

rme=0
		
for i in range(len(x)):
	pred=0
	for j in range(n):
		pred=pred+theta[j]*x[i][j]
	print pred,y[i]
	rme=rme+(pred-y[i])**2


rme=sqrt(rme/(2*len(x)))
print rme



