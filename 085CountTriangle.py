def gridToTriangle(x,y):
	sumOfTriangle=0
	for i in range(x):
		for o in range(y):
			sumOfTriangle+=(x-i)*(y-o)
	
	return(sumOfTriangle)

solved=False
sizeOfTriangle=1
closestGuy=[0,0]
difference=99999999
answer=0

while not(solved):
	sizeOfTriangle+=1
	for i in range(sizeOfTriangle):
		tempAns=gridToTriangle(i+1,sizeOfTriangle)
		tempDiff=abs(2000000-tempAns)
		if tempDiff<difference:
			closestGuy=[i+1,sizeOfTriangle]
			difference=tempDiff
			answer=tempAns
		if tempDiff>200000000:
			solved=True
	
	if sizeOfTriangle%100==0:
		print(sizeOfTriangle)

print(closestGuy)
print(answer)
