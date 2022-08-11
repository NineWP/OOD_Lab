# sum 3 number in array that result = 5
def getSubset(num_list) :
    if num_list == []:
        return [[]]
    x = getSubset(num_list[1:])
    return x + [[num_list[0]] + y for y in x]

def getSize3Subset(num_list) :
    return [x for x in getSubset(num_list) if len(x) == 3] 
    

num_list = [int(x) for x in input("Enter Your List : ").split()]
result = []
add_result = True

if len(num_list) <= 2 :
    print("Array Input Length Must More Than 2")
    exit()

for i in getSize3Subset(num_list) :
    if sum(i) == 5:
        if len(result) > 0 :
            for j in result :
                if set(j) == set(i):
                    add_result = False
        if add_result :
            i.sort()
            result.append(i)
    add_result = True

print(list(reversed(result)))



