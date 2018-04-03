#! /usr/bin/python3

def findGrad(x1, y1, x2, y2):
	top=y2-y1
	bot=x2-x1

	if bot==0:
		return 0, 1
	else:
		return top/bot, 0

def findRes(x1, y1, x2, y2):
	grad=findGrad(x1,y1,x2,y2)
	if grad[1]==1:
		return x1
	else:
		return y1-grad[0]*x1


totalCount=0

testFile=open("p102_triangles.txt")

for iLine in testFile:

	coordS=[]
	coordS=iLine.split(",")
	coord=[int(coordS[0]),int(coordS[1]),int(coordS[2]),int(coordS[3]),int(coordS[4]),int(coordS[5])]
	
	countSuc=[0,0,0]
	for i in range(3):
		for o in range(3):
			if o!=i:
				last=3-i-o
				grad, check=findGrad(coord[i*2], coord[i*2+1], coord[o*2], coord[o*2+1])
				intercept=findRes(coord[i*2], coord[i*2+1], coord[o*2], coord[o*2+1])

				if check==1:
					if 0-intercept>0 and coord[last*2]-intercept>0:
						countSuc[i]+=1
					elif 0-intercept<0 and coord[last*2]-intercept<0:
						countSuc[i]+=1
				else:
					pseu=coord[last*2+1]-grad*coord[last*2]
					if 0-intercept>0 and pseu-intercept>0:
						countSuc[i]+=1
					elif 0-intercept<0 and pseu-intercept<0:
						countSuc[i]+=1
	print(coord)
	print(countSuc)
	if countSuc[0]==2 and countSuc[1]==2 and countSuc[2]==2:
		totalCount+=1

print(totalCount)
