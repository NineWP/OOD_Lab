# enter hh mm ss and convert to seconds

print("*** Converting hh.mm.ss to seconds ***")
time_input = input("Enter hh mm ss : ")
time = [int(x) for x in time_input.split()]

# check if it valid or not
for i in time :
    if i >= 60 or i < 0 :
        print("mm({}) is invalid!".format(i))
        exit()

second = time[0]*3600 + time[1]*60 + time[2] # hh mm ss

print("{:02d}:{:02d}:{:02d} = {:,} seconds".format(time[0], time[1], time[2], second))