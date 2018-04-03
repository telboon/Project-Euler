def checkPass(longPass, combi):
	passStr=str(longPass)
	countPass=0
	for i in range(len(passStr)):
		if countPass!=3 and passStr[i]==combi[countPass]:
			countPass+=1
	
	if countPass==3:
		return True
	else:
		return False


def checkAll(longPass, combiList):
	failure=False
	for i in range(len(combiList)):
		tempAns=checkPass(longPass, combiList[i])
		if not(tempAns):
			failure=True
			break
	
	return not(failure)

currentIn=" "
combiList=[]
while currentIn!="":
	currentIn=input()
	if currentIn!="":
		combiList.append(currentIn)

longPass=100
while (1):

	if longPass%1000==0:
		print(longPass)
	
	if checkAll(longPass, combiList):
		print("Answer: "+str(longPass))
		break
	else:
		longPass+=1
	
