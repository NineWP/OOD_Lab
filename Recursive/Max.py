def Max_value(numlist, n) :
    if n == 1 :
        return numlist[0]
    return max(numlist[n-1], Max_value(numlist, n-1))

inp = input("Enter Input : ").split()
inp = list(map(int, inp))
n = len(inp)
print("Max :",Max_value(inp, n))