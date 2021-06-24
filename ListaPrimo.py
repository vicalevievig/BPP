def sacar_primo(n):
    if n >= 2:
        for i in range(2,n):
            if (n%i == 0):
                return False
            
        return True
         

try:

    n = int(input("De cuantos elementos quiere la lista?: "))

    if n >= 1:
        numeros =[]
        cont = 1
        while cont <= n:
            x = int(input("coloque un numero: "))
            numeros.append(x)
            cont += 1
        print()
        print("La lista creada es:")    
        print(numeros)


        resp = list(filter(sacar_primo, numeros))

        print()
        print("Los numeros primos de la lista son:")
        print(resp)
    else:
        print("ERROR: coloque un numero mayor o igual a 1")
except: 
    print("ERROR: coloque un numero")