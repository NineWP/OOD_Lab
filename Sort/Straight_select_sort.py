def maxIndex(arr, l, r) :
    if l == r :
        return l
    most = maxIndex(arr, l + 1, r)
    if arr[l] > arr[most] :
        return l
    return most


def selectionSort(arr, l, r) :
    if r <= l :
        return print(arr)
    most = maxIndex(arr, l, r)
    if most != r :
        arr[r], arr[most] = arr[most], arr[r]
        print(f"swap {arr[most]} <-> {arr[r]} : {arr}")
    selectionSort(arr, l, r - 1)

inp = [int(e) for e in input("Enter Input : ").split()]
n = len(inp)

selectionSort(inp, 0, n-1)