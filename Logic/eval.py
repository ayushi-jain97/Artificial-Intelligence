stack=[]
post=[]
prior={'!':3,'^':2,'v':1,'(':0}
s="!(p^q)^((pvq)vp)"
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

print post

for i in range(len(post)):
	if post[i]=='p':
		post[i]=1
	elif post[i]=='q':
		post[i]=0

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

print stack.pop()
