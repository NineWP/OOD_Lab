def minIndex( a , i , j ):
    if i == j:
        return i
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)

def recurSelectionSort(a, n, index = 0):
    if index == n:
        return -1
    k = minIndex(a, index, n-1)
    if k != index:
        a[k], a[index] = a[index], a[k]
        print("swap {} <-> {} : ".format(a[index], a[k]))
    recurSelectionSort(a, n, index + 1)

inp = [int(e) for e in input("Enter Input : ").split()]
n = len(inp)

recurSelectionSort(inp, n)

for i in inp:
    print(i, end=' ')