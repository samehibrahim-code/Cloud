number = [5,3,0,2,0,4,0,1]
n=0
for i,j in enumerate( number) :
    if j == 0:
        n+=1
        number.pop (i)
zeros = [0 for i in range (n)]
new = zeros + number
print (new)
    
