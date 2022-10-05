def Power(a, b) :
    if b == 0 : return 1
    if b == 1 : 
        return a
    return a * Power(a, b-1)

a, b = map(int, input().split())
print(Power(a, b))

