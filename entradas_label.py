import random

def entradas_label():
    print('Tipo de entrada: ')
    print('1. random;\n2. ordenada\n3. decrescente\n')
    escolhatype = int(input('Escolha: '))
    print('Quantidade de Entradas: ')
    print('1. 100;\n2. 250;\n3. 500;\n4. 1.000;\n5. 5.000;\n6. 30.000;\n7. 50.000;\n8. 100.000;\n9. 150.000;\n0. 200.000.')

    escolha = int(input('Escolha: '))
    if (escolhatype==1):
        if (escolha == 1):
            saida_da_entrada = [random.randrange(1, 100) for i in range(100)]
            return saida_da_entrada
        elif(escolha==2):
            saida_da_entrada = [random.randrange(1,250) for i in range(250)]
            return saida_da_entrada
        elif(escolha==3):
            saida_da_entrada=[random.randrange(1,500) for i in range(500)]
            return saida_da_entrada
        elif(escolha == 4):
            saida_da_entrada = [random.randrange(1, 1000) for i in range(1000)]
            return saida_da_entrada
        elif(escolha == 5):
            saida_da_entrada = [random.randrange(1, 5000) for i in range(5000)]
            return saida_da_entrada
        elif(escolha == 6):
            saida_da_entrada = [random.randrange(1, 30000) for i in range(30000)]
            return saida_da_entrada
        elif(escolha == 7):
            saida_da_entrada = [random.randrange(1, 50000) for i in range(50000)]
            return saida_da_entrada
        elif(escolha == 8):
            saida_da_entrada = [random.randrange(1, 100000) for i in range(100000)]
            return saida_da_entrada
        elif(escolha == 9):
            saida_da_entrada = [random.randrange(1, 150000) for i in range(150000)]
            return saida_da_entrada
        elif(escolha == 0):
            saida_da_entrada = [random.randrange(1, 200000) for i in range(200000)]
            return saida_da_entrada
    elif(escolhatype==2):
        if (escolha == 1):
            saida_da_entrada = [i for i in range(100)]
            return saida_da_entrada
        elif(escolha==2):
            saida_da_entrada = [i for i in range(250)]
            return saida_da_entrada
        elif(escolha==3):
            saida_da_entrada=[i for i in range(500)]
            return saida_da_entrada 
        elif(escolha == 4):
            saida_da_entrada = [i for i in range(1000)]
            return saida_da_entrada
        elif(escolha == 5):
            saida_da_entrada = [i for i in range(5000)]
            return saida_da_entrada
        elif(escolha == 6):
            saida_da_entrada = [i for i in range(30000)]
            return saida_da_entrada
        elif(escolha == 7):
            saida_da_entrada = [i for i in range(50000)]
            return saida_da_entrada
        elif(escolha == 8):
            saida_da_entrada = [i for i in range(100000)]
            return saida_da_entrada
        elif(escolha == 9):
            saida_da_entrada = [i for i in range(150000)]
            return saida_da_entrada
        elif(escolha == 0):
            saida_da_entrada = [i for i in range(200000)]
            return saida_da_entrada
    elif(escolhatype==3):
        if (escolha == 1):
            saida_da_entrada = [100-i for i in range(100)]
            return saida_da_entrada
        elif(escolha==2):
            saida_da_entrada = [250-i for i in range(250)]
            return saida_da_entrada
        elif(escolha==3):
            saida_da_entrada=[500-i for i in range(500)]
            return saida_da_entrada
        elif(escolha == 4):
            saida_da_entrada = [1000-i for i in range(1000)]
            return saida_da_entrada
        elif(escolha == 5):
            saida_da_entrada = [5000-i for i in range(5000)]
            return saida_da_entrada
        elif(escolha == 6):
            saida_da_entrada = [30000-i for i in range(30000)]
            return saida_da_entrada
        elif(escolha == 7):
            saida_da_entrada = [50000-i for i in range(50000)]
            return saida_da_entrada
        elif(escolha == 8):
            saida_da_entrada = [100000-i for i in range(100000)]
            return saida_da_entrada
        elif(escolha == 9):
            saida_da_entrada = [150000-i for i in range(150000)]
            return saida_da_entrada
        elif(escolha == 0):
            saida_da_entrada = [200000-i for i in range(200000)]
            return saida_da_entrada
        return None
