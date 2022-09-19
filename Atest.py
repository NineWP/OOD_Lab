# Read the input
n = int(input())

def rec(n):
    if n==0:
        print(0)
    else:
        print(-n)
        rec(n-1)
rec(n)