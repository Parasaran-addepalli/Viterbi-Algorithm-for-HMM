pi = [1,0]
a = [[0.7,0.3],[0.5,0.5]]
b = [[0.6,0.1,0.3],[0.1,0.7,0.2]]
seq =[2,1,0]

prob = pi
states=[]

for i in range(len(seq)):
    x = max(a[0][0]*prob[0]*b[0][seq[i]], a[1][0]*prob[1]*b[1][seq[i]])
    y = max(a[0][1]*prob[0]*b[0][seq[i]], a[1][1]*prob[1]*b[1][seq[i]])
    l=[]
    if a[0][0]*prob[0]*b[0][seq[i]] >= a[1][0]*prob[1]*b[1][seq[i]]:
        l.append(0)
    else:
        l.append(1)
    
    if a[0][1]*prob[0]*b[0][seq[i]] >= a[1][1]*prob[1]*b[1][seq[i]] :
        l.append(0)
    else:
        l.append(1)
    prob[0] = x
    prob[1] = y
    states.append(l)
print(states)

seq=[]
n=1
l=[]
if prob[0]>=prob[1]:
    print('The probability of given sequence is :',prob[0])
    n=0
else:
    print('The probability of given sequence is :',prob[1])
    n=1
seq.insert(0,n)
while states:
    l = states.pop(-1)
    seq.insert(0,l[n])
    n=l[n]
print('The best sequence is'+str(seq))
    
    

    
