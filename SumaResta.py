""" Este programa calcula la suma y resta de dos cifras dadas por el usuario. 
Ademas cuenta con un menu interactivo para facilitar la interaccion del usuario con el programa
"""


def sumaresta(a,b):
    """ Esta funcion calcula la suma y la resta de "a" y "b"

    Args: 
        a (str): La primera cifra. Es introducida por el usuario y convertida a float
        b (str): La segunda cifra. También introducida por el usuario y convertida a float
    
    Raises:
        ERROR: aparece cuando el usuario ha introducido algo diferente a un número (positivo o negativo)
    
    Return:
        s: la suma de "a" más "b"
        r: la resta de "a" menos "b"
        s y r serán mostrados en pantalla mediante un print()
    """

    try:
        i = float(a)
        j = float(b)
        
        s = (i + j)
        r = (i - j)
    
        print("La suma de:",a,"+",b,"es:",s)
        print("La resta de:",a,"-",b,"es:",r)
    
    except:

        print("ERROR: Coloque un numero positivo o negativo")


if __name__ == "__main__":

    while True:
        print("(1) Calcular suma y resta")
        print("(2) Salir")
        o = input("Seleccione una opcion: ")

        if o == "1":
            
            x = input("Indica la primera cifra: ")
            y = input("Indica la segunda cifra: ")

            sumaresta(x,y)
    
        elif o == "2":
            break

        else:
            print("Coloque una opcion valida (1) o (2)")

    print("Hasta luego")

