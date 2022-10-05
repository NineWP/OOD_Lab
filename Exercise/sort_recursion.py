def quick_sort(l) :
    if len(l) <= 1 :
        return l
    else :
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] + quick_sort([e for e in l[1:] if e > l[0]])

inp = list(map(int, input("Enter Input : ").split(', ')))

print(quick_sort(inp))