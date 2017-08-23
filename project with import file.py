import math
import os


		
def dic(x):
	y=[]
	for i in x:
		i= i.lower().replace("."," ").replace("/n"," ").replace(","," ")
	y.append(x)
	print(y)
	d={}
	for i in range(len(y)):
		d[y[i]]=y.count(y[i])
	return d

def dot(s1,s2):
	sum=0
	for i in s1:
		if i in s2:
			sum=sum+(s1.get(i)*s2.get(i))
	return sum
def vec(x):
	vec=0
	for i in x:
		vec=vec+(x.get(i)**2)
	vect=math.sqrt(vec)
	return vect
path=os.getcwd()
files=os.listdir(path)
files_text=[i for i in files if i.endswith('.txt')]
print(files_text)
for x in range(len(files_text)):
	for y in range(len(files_text)):
		if(x<y):
			filename1=files_text[x]
			filename2=files_text[y]
			l1=open(filename1,'r').read().split()
			s1=dic(l1)
			l2=open(filename2,"r").read().split()
			#print(list2)
			s2=dic(l2)
			d=dot(s1,s2)
			vec1=vec(s1)
			#print(vec1)
			vec2=vec(s2)
			#print(vec2)
			ans=(d/(vec1*vec2))*100
			print("plagarism for 2 files id",ans,"%")



