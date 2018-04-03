triSet=set()

for i in range(1,601):
	triSet.add(i*(i+1)*0.5)

fobj=open("p042_words.txt")
for line in fobj:
	names=line

fobj.close()

print(names)

answer=0

workingcount=0

for i in range(0,len(names)):
	if names[i]=="\"" or names[i]==",":
		if workingcount!=0:
			if workingcount in triSet:
				answer=answer+1
		workingcount=0
	else:
		workingcount=workingcount+ord(names[i])-64

print(answer)
