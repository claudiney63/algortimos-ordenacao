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
