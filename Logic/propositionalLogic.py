sent={}

def postfix(s):
	stack=[]
	post=[]
	prior={'!':3,'^':2,'v':1,'(':0}
	
	l=len(s)
	for i in range(l):
		if ord(s[i])>=97 and ord(s[i])<=122 and s[i]!='v':
			post.append(s[i])
		elif s[i]=='(':
			stack.append('(')
		elif s[i]=='v' or s[i]=='!' or s[i]=='^':
			while(len(stack) and prior[stack[-1]]>prior[s[i]]):
				post.append(stack.pop())
			stack.append(s[i])
		elif s[i]==')':
			while(len(stack) and stack[-1]!='('):
				post.append(stack.pop())
			stack.pop()
	while len(stack):
		post.append(stack.pop())

	return post

def evaluate(post):
	stack=[]
	for i in post:
		if i==0 or i==1:
			stack.append(i)
		elif i=='!':
			e=stack.pop()
			e=1-e
			stack.append(e)
		elif i=='^':
			a=stack.pop()
			b=stack.pop()
			stack.append(a*b)
		else:
			a=stack.pop()
			b=stack.pop()
			x=a+b
			if x==2:
				x=1
			stack.append(x)

	return stack.pop()

class Logic:
	
	def __init__(self,x):
		self.var=set()
		self.num=0
		self.y=x
		all_comb=self.generate_combinations(x)
		truth_values=[]
	
		for i in all_comb:
			y=self.truth_assignment(i,x)
			truth_values.append(str(y==True))
		ans=[[] for i in range(self.num)]

		for i in range(self.num):
			for j in all_comb[i]:
				ans[i].append(j)
			ans[i].append(truth_values[i])
		sent[self.y]=ans

	

	def calc_var(self,x):
		for i in x:
			j=ord(i)
			if j>=97 and j<=122 and i!='v':
				self.var.add(i)
		
	def generate_combinations(self,x):
		self.calc_var(x)
		l=len(self.var)
		self.num=2**l
	
		all_comb=[]
		for i in range(self.num):
			y=[0 for j in range(l)]
			a=i;k=0
			while a!=0:
				y[k]=a%2
				a=a/2
				k=k+1
			all_comb.append(y)

		return all_comb
	
	def truth_assignment(self,value,x):
		l=list(self.var)
		post=postfix(x)
		for i in range(len(l)):
			for j in range(len(post)):
				if post[j]==l[i]:
					post[j]=value[i]
				
		#print post
		return evaluate(post)
			
				
		

a=Logic("p^q")
b=Logic("(pvq)v(!p^!q)")
c=Logic("p^!q")
#d=Logic("pv!q")
print "Evaluation: "
for i in sent:
	print i
	for j in sent[i]:
		print j
	print

class Parameter:
	def __init__(self):
		self.tautology=[]
		self.contradiction=[]
		self.contingency=[]
		self.equivalence=[]
		self.entailment=[]
	def check_tautology(self):
		for i in sent:
			ans=True
			for j in sent[i]:
				if j[-1]!='True':
					ans=False
					break
			if ans:
				self.tautology.append(i)
		
	def check_contradiction(self):
		for i in sent:
			ans=True
			for j in sent[i]:
				if j[-1]!='False':
					ans=False
					break
			if ans:
				self.contradiction.append(i)
	def check_contingency(self):
		for i in sent:
			if i not in self.tautology and i not in self.contradiction:
				self.contingency.append(i)

	def check_equivalence(self):
		key=sent.keys()
		for x in range(len(sent)):
			for y in range(x+1,len(sent)):
				i=key[x];j=key[y]
				if len(sent[i])==len(sent[j]):
					ans=True
					
					for k in range(len(sent[i])):
						if sent[i][k][-1]!=sent[j][k][-1]:
							ans=False
							break
					if ans:
						self.equivalence.append((i,j))
	def check_entailment(self):
		for i in sent:
			for j in sent:	
				if i!=j and len(sent[i])==len(sent[j]):
					ans=True
					for k in range(len(sent[i])):
						if sent[i][k][-1]=='True' and sent[j][k][-1]=='False':
							ans=False
							break
					if ans:
						self.entailment.append((i,j))
	def check_consistency(self):
		key=sent.keys()
		k=0
		x=[[] for i in range(len(key))]
		num=len(sent[key[0]])
		for i in sent:
			for j in sent[i]:
				x[k].append(j[-1])
			k=k+1
		#print x
		ans=['True' for i in range(num)]
		
		for j in range(num):
			y=[]
			for i in range(len(x)):
				y.append(x[i][j])

			if y==ans:
				return True
		return False

b=Parameter()
b.check_tautology()
print "Tautology: ", b.tautology
b.check_contradiction()
print "Self-Contradiction: " ,b.contradiction
b.check_contingency()
print "Contingency: " ,b.contingency
b.check_equivalence()
print "Equivalence: " ,b.equivalence
b.check_entailment()
print "Entailment: ", b.entailment
print b.check_consistency()
