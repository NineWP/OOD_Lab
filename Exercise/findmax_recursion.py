def Max(list):
    if len(list) == 1 :
        return list[0]
    else :
        m = Max(list[1:])
        return m if m > list[0] else list[0]

inp = list(map(int, input("Enter Input : ").split()))
print(Max(inp))