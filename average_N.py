#!/usr/bin/env python3
N = 10
count = 0
sum = 0
while count < N:
   number = float(input("Enter the number: "))
   sum = sum + number
   count =  count + 1
average = float(sum)/N
print("N = %d, Sum = %f" %(N, sum))
print ("Average = %f" %average)
