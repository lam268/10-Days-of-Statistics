# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
n = int(input())
num_list = list(int(num) for num in input().strip().split())[:n]
weight = list(int(num) for num in input().strip().split())[:n]
arr = []
N = 0
for i in range(n):
    arr += [num_list[i]] * weight[i]
    N += weight[i]
    arr.sort()

re = median(arr[(N+1)//2:])-median(arr[:N//2])

print(round(float(re),1))


