import math

answer=0
seto=set()
for i in range(2,10):
	work=1
	while work<=199:
		if math.log(math.pow(i,work),10)//1==work-1:
			seto.add(math.pow(i,work))
			print(math.pow(i,work))
		work+=1

print("Answer:",len(seto))
