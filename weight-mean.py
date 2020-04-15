# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(arr1, arr2, size):
    sum = 0
    weight = 0
    list = zip(arr1,arr2)
    for i,j in list:
        sum += i*j
    for j in arr2:
        weight += j
    return sum/weight

size = int(input())
arr1 = list(int(num) for num in input().strip().split())[:size]
arr2 = list(int(num) for num in input().strip().split())[:size]
print(mean(arr1,arr2,size))