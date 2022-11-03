def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]     
        if not swapped:
            return


inp = [int(e) for e in input("Enter Input : ").split()]
lst = []
temp = []
med = 0.0

for i in inp :
    lst.append(i)
    temp.append(i)
    bubbleSort(lst)
    if len(lst) % 2 == 0 :
        i = int(len(lst)/2)
        j = int(len(lst)/2) - 1
        med = (lst[i] + lst[j]) / 2
    else :
        i = int((len(lst)-1) / 2)
        med = float(lst[i])
    print("list = {} : median = {}".format(temp, med))