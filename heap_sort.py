from heapq import heappop, heappush

def heapsort(list1):
     heap = []
     for ele in list1:
         heappush(heap, ele)

     sort = []

     #  os elementos são levantados na pilha
     while heap:
         sort.append(heappop(heap))

     return sort
