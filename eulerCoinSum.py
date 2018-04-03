maxjump=[1,9,9,90,90,80,200,200]
value=[200,100,50,20,10,5,2,1]

working=[0,0,0,0,0,0,0,0]

ans=0

while working[0]<maxjump[0]:
	working[7]=working[7]+1

	#check if exceed maxjump
	for i in range(7,0,-1):
		if working[i] > maxjump[i]:
			working[i-1]=working[i-1]+1
			working[i]=0

	#start check if adds to two
	check=0
	for i in range(0,8):
		check=check+working[i]*value[i]
	
	if check==200:
		print(working)
		ans=ans+1
	elif check>200:
		for i in range(7,0,-1):
			if working[i]!=0:
				working[i]=0
				working[i-1]=working[i-1]+1
				working[7]=-1
				break
	
print("Total Count:",ans+1)
