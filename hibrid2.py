def partition (a, inicio, fim):  
    i = (inicio - 1)
    pivot = a[fim] # elemento pivot  
      
    for j in range(inicio, fim):  
        # Se elemento atual for menor que ou igual ao pivot 
        if (a[j] <= pivot):  
            i = i + 1  
            a[i], a[j] = a[j], a[i]  
      
    a[i+1], a[fim] = a[fim], a[i+1]  
  
    return (i + 1)
      
# função para implementar classificação rápida 
def quick(a, inicio, fim): # a[] = array a ser classificado, início do índice, finalização do índice
    if (inicio < fim):
        p = partition(a, inicio, fim) #p está particionado no índice
        quick(a, inicio, p - 1)  
        quick(a, p + 1, fim)

# função para dividir as listas nas duas sublistas 
def merge_sort(list1, left_index, right_index):  
    if left_index >= right_index:  
        return  
  
    middle = (left_index + right_index)//2  
    merge_sort(list1, left_index, middle)  
    merge_sort(list1, middle + 1, right_index)  
    merge(list1, left_index, right_index, middle)  
  
# Definindo uma função para mesclar a lista
def merge(list1, left_index, right_index, middle):  
  
    # Criando subpartes de uma lista 
    left_sublist = list1[left_index:middle + 1]  
    right_sublist = list1[middle+1:right_index+1]  
  
    # Valores iniciais para variáveis que usamos para manter
    # faixa de onde estamos em cada list1  
    left_sublist_index = 0  
    right_sublist_index = 0  
    sorted_index = left_index  
  
    # atravessar ambas as cópias até  excedermos um elemento  
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):  
  
        # atravessar ambas as cópias até  excedermos um elemento
        # # parte e em seguida avançar na sublista_esquerda (aumentando o ponteiro)  
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:  
            list1[sorted_index] = left_sublist[left_sublist_index]  
            left_sublist_index = left_sublist_index + 1  
        # Caso contrário, adicione na sublista correta
        else:  
            list1[sorted_index] = right_sublist[right_sublist_index]  
            right_sublist_index = right_sublist_index + 1  
  
        # avançar na parte classificada  
        sorted_index = sorted_index + 1  
       
    # vamos percorrer os elementos restantes e adicioná-los   
    while left_sublist_index < len(left_sublist):  
        list1[sorted_index] = left_sublist[left_sublist_index]  
        left_sublist_index = left_sublist_index + 1  
        sorted_index = sorted_index + 1  
  
    while right_sublist_index < len(right_sublist):  
        list1[sorted_index] = right_sublist[right_sublist_index]  
        right_sublist_index = right_sublist_index + 1  
        sorted_index = sorted_index + 1  

def vivoSort(arr):
    n = len(arr)
    minRun = 64 #Tamanho mínimo do subarray, segundo recomendações de pesquisas sobre tim sort
    # sendo essa a quantidade de elementos desse subconjunto

    #Ordenando os subarrays individuais de tamanho minimo
    for inicio in range(0, n, minRun):
        fim = min(inicio + minRun - 1, n - 1) 
        quick(arr, 0, n - 1)

    # Começando a mesclagem a partir do tamanho mínimo do subarray
    tamanho = minRun
    while tamanho < n:

        # escolhendo o ponto de partida do array à esquerda
        # as sub-listas que serão mescladas são arr[esuerda..esquerda+tamanho-1]
        # e arr[esquerda+tamanho, esquerda+2*tamanho-1]
        # depois de mesclar, fazemos o salto em 2*tamanho
        for esquerda in range(0, n, 2 * tamanho):

            # Encontrando o ponto de divisão entre as sub-listas
            meio = min(n - 1, esquerda + tamanho - 1)
            direita = min((esquerda + 2 * tamanho - 1), (n - 1))

            # Mesclando as sublistas arr[esquerda..meio] e arr[meio+1..direita]
            merge(arr, esquerda, direita, meio)

        tamanho = 2 * tamanho
    return arr

# araay = [i for i in range(200000)]

# vivoSort(araay)

# print(araay)
