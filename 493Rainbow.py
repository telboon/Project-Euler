#! /usr/bin/python3
from decimal import *
import random

total=[]

for i in range(1000):
	print(i)
	for o in range(10):
		balls=[]
		bag=[]
		for color in range(70):
			balls.append(int(random.uniform(0,7)))
		for choice in range(10):
			choose=int(random.uniform(0,70))
			while balls[choose]==-1:
				choose=int(random.uniform(0,70))

			bag.append(balls[choose])
			balls[choose]=-1

		allCount=len(set(balls))
		total.append(allCount)

a=Decimal(sum(total))
b=Decimal(len(total))
c=Decimal(a/b)
print(getcontext())
print(c)
print(total)
