'''
Description:
You have been given an array A of size N consisting of positive integers. You need to
find and print the product of all the number in this array Modulo 10^9 + 7 

Input Format:
The first line contains a single integer N denoting the size of the array. 
The next line contains N space separated integers denoting the elements of 
the array
Output Format:
Print a single integer denoting the product of all the elements of the array 
Modulo 10^9 + 7 

SAMPLE INPUT 
5
1 2 3 4 5

SAMPLE OUTPUT 
120
'''
N = raw_input("Enter the size of the array:\n")
l = list(raw_input("Enter elements :\n").split(" "))
l = [int(i) for i in l]
m = 1
for each in l:
    m = (m * each)%(10**9+7)
print m    
