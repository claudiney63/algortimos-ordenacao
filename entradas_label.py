import random

def entradas_label():
    print('Tipo de entrada: ')
    print('1. random;\n2. ordenada\n3. decrescente\n')
    escolhatype = int(input('Escolha: '))
    print('Quantidade de Entradas: ')
    print('1. 100;\n2. 250;\n3. 500;\n4. 1.000;\n5. 5.000;\n6. 30.000;\n7. 50.000;\n8. 100.000;\n9. 150.000;\n0. 200.000.')

    with open("100numbers.txt", "r") as arquivo:
        cemnumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            cemnumbers.append(int(fields[i]))

    with open("250numbers.txt", "r") as arquivo2:
        cclnumbers=[]
        for line in arquivo2.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            cclnumbers.append(int(fields[i]))
            
    with open("500numbers.txt", "r") as arquivo3:
        cccccnumbers=[]
        for line in arquivo3.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            cccccnumbers.append(int(fields[i]))
            
    with open("1000numbers.txt", "r") as arquivo:
        knumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            knumbers.append(int(fields[i]))
            
    with open("5000numbers.txt", "r") as arquivo:
        cincoknumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            cincoknumbers.append(int(fields[i]))

    with open("30000numbers.txt", "r") as arquivo:
        trintaknumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            trintaknumbers.append(int(fields[i]))
            
    with open("50000numbers.txt", "r") as arquivo:
        cinquentaknumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            cinquentaknumbers.append(int(fields[i]))
            
    with open("100000numbers.txt", "r") as arquivo:
        cemknumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            cemknumbers.append(int(fields[i]))
            
    with open("150000numbers.txt", "r") as arquivo:
        centoecinquentaknumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            centoecinquentaknumbers.append(int(fields[i]))

    with open("200000numbers.txt", "r") as arquivo:
        duzentosknumbers=[]
        for line in arquivo.readlines():
            fields = line.split(',')
        for i in range(len(fields)):
            duzentosknumbers.append(int(fields[i]))
            
    escolha = int(input('Escolha: '))
    if (escolhatype==1):
        if (escolha == 1):
            saida_da_entrada = cemnumbers
            return saida_da_entrada
        elif(escolha==2):
            saida_da_entrada = cclnumbers
            return saida_da_entrada
        elif(escolha==3):
            saida_da_entrada=cccccnumbers
            return saida_da_entrada
        elif(escolha == 4):
            saida_da_entrada = knumbers
            return saida_da_entrada
        elif(escolha == 5):
            saida_da_entrada = cincoknumbers
            return saida_da_entrada
        elif(escolha == 6):
            saida_da_entrada = trintaknumbers
            return saida_da_entrada
        elif(escolha == 7):
            saida_da_entrada = cinquentaknumbers
            return saida_da_entrada
        elif(escolha == 8):
            saida_da_entrada = cemknumbers
            return saida_da_entrada
        elif(escolha == 9):
            saida_da_entrada = centoecinquentaknumbers
            return saida_da_entrada
        elif(escolha == 0):
            saida_da_entrada = duzentosknumbers
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
