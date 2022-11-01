inp = [int(e) for e in input("Enter Input : ").split()]
for i in range(len(inp[:-1])) :
    if inp[i] > inp[i+1]:
        print("No")
        exit()
print("Yes")