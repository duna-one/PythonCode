from shet import func

a = int(input("Enter a:"))
b = int(input("Enter b:"))

x_Range=list(range(int(a-3*b**(1/2)), int(a+3*b**(1/2)), int(0.2*b**(1/2))))

spis=[]
for x in x_Range:
    spis.append(func(a,b,x))

fp=open('lambda.txt','wt')
for i in range(2,len(spis)):
	print(str(str(spis[i-1])+' ,'+str(spis[i])))
	spis_up=str(str(spis[i-1])+' ,'+str(spis[i]))	
	fp.write(spis_up)
	fp.write('\n')

fp.close()