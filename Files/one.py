f=open('one.txt','r')
data=f.read()
cp=open('two.txt','w')
cp.write(data)
f.close()
cp.close()