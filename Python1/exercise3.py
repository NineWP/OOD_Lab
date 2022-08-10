# Summation of each digit program

print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))
sum = 0
while(num > 0):
    sum += int(num % 10)
    num = num//10

print("Summation of each digit =  {:d}".format(sum))