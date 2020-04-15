# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def Mean(arr):
    mean = 0
    for i in arr:
        mean += i
    return mean/len(arr)
def Median(arr):
    sortarr = sorted(arr)
    if(len(arr)%2!=0):
        median = sortarr[(len(arr)-1)/2]    
    elif(len(arr)%2==0):
        median = (sortarr[int(len(arr)/2)] + sortarr[int(len(arr)/2-1)])/2
    return median
def Mode(arr):
    data = collections.Counter(arr)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    sortmode = sorted(mode_val)
    return sortmode.pop(0)

n = int(input())
num_list = list(int(num) for num in input().strip().split())[:n]
print(Mean(num_list))
print(Median(num_list))
print(Mode(num_list))
