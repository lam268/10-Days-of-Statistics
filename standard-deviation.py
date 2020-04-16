# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import pstdev 
n=int(input())
arr=sorted(map(int,input().split()))

print(round(pstdev(arr),1))
