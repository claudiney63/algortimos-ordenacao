#função que considera último elemento como pivot,
#coloca o pivô em sua posição exata e coloca os
#elementos menores à esquerda do pivot e maiores
#elementos à direita do pivot. 
  
def partition (a, start, end):  
    i = (start - 1)  
    pivot = a[end] # elemento pivot  
      
    for j in range(start, end):  
        # Se elemento atual for menor que ou igual ao pivot 
        if (a[j] <= pivot):  
            i = i + 1  
            a[i], a[j] = a[j], a[i]  
      
    a[i+1], a[end] = a[end], a[i+1]  
  
    return (i + 1)  
      
# função para implementar classificação rápida 
def quick(a, start, end): # a[] = array a ser classificado, start = início índice, end = finalização índice
    if (start < end):  
        p = partition(a, start, end) #p está particionado no índice
        quick(a, start, p - 1)  
        quick(a, p + 1, end)  
  
          
def printArr(a): # Função para imprimir o array  
    for i in range(len(a)):  
        print (a[i], end = " ")  
  
      
a = [68, 13, 1, 49, 58]  
print("Before sorting array elements are - ")  
printArr(a)  
quick(a, 0, len(a)-1)  
print("\nAfter sorting array elements are - ")  
printArr(a)  