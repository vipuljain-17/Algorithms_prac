#Main function of bubbleSort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

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
bubbleSort(arr)

#print the array/list eiher using print fuction directly
#or use print_list() fuction by passing arr as argument
print_list(arr)
