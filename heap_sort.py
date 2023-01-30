comp=0
import time
inicio=time.time()
tamanho=100
def heapify(arr, n, i):
    global comp
    largest = i  # Initialize largest as root 
    l = 2 * i + 1  # left = 2*i + 1 
    r = 2 * i + 2  # right = 2*i + 2 
    comp+=3
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r   
    if largest != i: 
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)
        
def heapSort(arr):
    global comp
    n = len(arr)  
    for i in range(n // 2 - 1, -1, -1):
        comp+=1
        heapify(arr, n, i) 
    for i in range(n - 1, 0, -1):
        comp+=1
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)
    print(comp)
    return arr
       
