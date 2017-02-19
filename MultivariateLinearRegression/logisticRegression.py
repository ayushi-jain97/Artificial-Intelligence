from math import sqrt,exp
from random import shuffle
f=open("diabetes.txt","r")
l=f.readlines()
shuffle(l)
x=[]
y=[]

x_test=[]
y_test=[]

for i in l:
	c=i.strip().split(',')
	for j in range(len(c)-1):
		c[j]=float(c[j])
	c=[1]+c
	x.append(c[:len(c)-1])
	if c[-1]=='tested_positive':
		y.append(1)
	else:
		y.append(0)


s=int(0.8*(len(x)))
x_test=x[s:]
x=x[:s]

y_test=y[s:]
y=y[:s]


theta=[]
temp=[]
n=len(x[0]) #number of features
m=len(x) #number of training examples
for i in range(n):
	theta.append(0)
	temp.append(0)



alpha=0.00001
iterations=10000


for i in range(iterations):
	for j in range(n):
		f=0
		for k in range(m):
			hthetaX=0
			for c in range(n):
				hthetaX=hthetaX+x[k][c]*theta[c]
			gthetaX=1.0/(1+exp(-1*hthetaX))
			f=f+(gthetaX-y[k])*x[k][j]
		temp[j]=theta[j]-(alpha*f)/m
	
	error=0
	for k in range(m):
		pred=0
		for j in range(n):
			pred=pred+theta[j]*x[k][j]
		pred=1.0/(1+exp(-1*pred))
		error=error+(pred-y[k])**2
	
	print sqrt(error/(2*m))
	for j in range(n):
		theta[j]=temp[j]



print theta

rme=0
		
for i in range(len(x_test)):
	pred=0
	for j in range(n):
		pred=pred+theta[j]*x_test[i][j]
	pred=1.0/(1+exp(-1*pred))
	if(pred>=0.5):
		pred=1;
	else:
		pred=0
	print pred,y_test[i]
	rme=rme+(pred-y_test[i])**2


print "Error: " ,(rme*100.0)/len(x_test)



