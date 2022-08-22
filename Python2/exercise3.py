def generateRange(a = 0.0, b = 0.0, c = 1.0):
    num_lst = []
    #print(a,b,c)
    if a > b:
        a,b = b,a

    while a < b:
        num_lst.append("{:g}".format(a))
        a += c
    float_lst = [float(i) for i in num_lst]
    return tuple(float_lst)
    
    
print("*** New Range ***")
num = [float(x) for x in input("Enter Input : ").split()]

#print(len(num), num)

if len(num) == 1:
    print(generateRange(num[0]))
elif len(num) == 2:
    print(generateRange(num[0], num[1]))
else :
    print(generateRange(num[0], num[1], num[2]))






