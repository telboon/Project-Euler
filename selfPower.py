import math

ans=0
for i in range(1,1001):
	ans=ans+pow(i,i)

magic=str(ans)
print(magic[-10:len(magic)])
