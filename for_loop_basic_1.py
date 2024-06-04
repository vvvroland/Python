
for x in range (151):
    print (x)

for y in range (5,1001,5):
    print(y)

    
for z in range (1,101):
    if z%10==0:
        print("CodingDojo")
    elif z%5==0:
        print("Coding")
    else:
        print(z)


sum=0
for a in range (1, 500000, 2):
    if a%2!=0:
        sum+=a
print(sum)



for b in range (2018, -1, -4):
    print (b)

lowNumb=2
highNumb=9
mult=3
for c in range(lowNumb, highNumb+1,):
    if c%mult==0:
        print(c)
