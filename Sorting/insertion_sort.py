#A python code/implementation of Insertion Code

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        value = arr[i]
        j = i-1

        while j>0 and value < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        
        arr[j + 1] = value

def print_list(arr):
    print("Sorted list/array: ",end = ' ')
    n = len(arr)
    for i in range(n-1):
        print(f"{arr[i]}," , end='')
    print(arr[n-1])

#Take the input of the unsorted array/list
#For example give [4 5 8 15 8 1]
print("Enter the values of list/array: ",end = '')
arr = list(map(int,input().split()))

#call the fuction by giving the arr as input
insertionSort(arr)

#print the array/list eiher using print fuction directly
#or use print_list() fuction by passing arr as argument
print_list(arr)