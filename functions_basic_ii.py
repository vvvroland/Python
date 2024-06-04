
#1
def countdown(num):
    list=[]
    for x in range(num,-1, -1):
        list.append(x)
    return list

print(countdown(5))

#2
mist=[1,2]
x=mist[1]

def pandr(a,b):
    print(mist[0])
    return x

print(pandr(mist[0],mist[1]))

#3

hand=[1,2,3,4,5]

def one_plus(a):
    sum= a[0] + len(a)
    return sum

print(one_plus(hand))

#4
mouth=[5,2,3,2,1,4]
lip=mouth[1]
oris=[]

def greater_value(a,b):
    for x in range(0, len(a)):
        if a[x]>b:
            oris.append(a[x])
    #print(oris) 
    #print(len(oris))   
    if len(oris)<2:
        return False
    else:
        return oris                
        
print(greater_value(mouth,lip))

#5

peat=[]

def lenval(a, b):
    alt=a+1
    for x in range(0,alt):
        peat.append(b)
    return peat

#print(lenval(4,7))
print(lenval(6,2))