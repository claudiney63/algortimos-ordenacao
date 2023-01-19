# Criando a função de inserção
def insertion_sort(list1):  
  
        # Laço externo para atravessar através de 1 para len(list1)  
        for i in range(1, len(list1)):  
  
            value = list1[i]  
  
            # Move elementos da lista1[0..i-1], que são
            # maior que valor, para uma posição à frente
            # da sua posição atual  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        return list1   
  