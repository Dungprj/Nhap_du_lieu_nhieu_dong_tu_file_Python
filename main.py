f = open("Input.txt","r")

def sum(a):
	s = 0
	for i in a:
		s+=i
	return s

k = list(map(int,f.readline().split()))
m = k[0]
n = k[1]
a = []
for i in range(m):
	k = list(map(int,f.readline().split()))
	a.append(k)
b = [0]*m
for i in range(len(a)):
	b[i] = sum(a[i])

for i in range(len(b)-1):
	for j in range(i+1,len(b)):
		if (b[i] > b[j]):
			b[i],b[j] = b[j],b[i]
			a[i],a[j] = a[j],a[i]


fw = open("Output.txt","w")
for i in range(m):
	kq = ' '.join(map(str,a[i]))
	fw.write(kq+'\n')


