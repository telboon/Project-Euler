def FibonacciChecker(num2): 
	num=int(num2)
	working=1

	if num==1:
		return "yes"
	
	full=[1,1]
	
	while full[working]<num:
		full+=[full[working]+full[working-1]]
		if full[working+1]>num:
			return "no"	
		working+=1

		if full[working]==num:
			return "yes"
	return "no"

	
# keep this function call here	
# to see how to enter arguments in Python scroll down
print FibonacciChecker(raw_input())	

