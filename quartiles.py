# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
n=int(input())
arr=sorted(map(int,input().split()))

print(int(median(arr[:n//2])))
print(int(median(arr)))
print(int(median(arr[(n+1)//2:])))
