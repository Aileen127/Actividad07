
def suma_total(numero): #1.1
    suma = 0
    for n in numero:
        if numero != '0':
            suma += n
        else:
            print("Ingresa un dato valido por favor.")
    return suma
def promedio(numero):# 1.2
    return sum(numero) / len(numero)
def positivos_negativos(numero): #1.3
    positivo = 0
    negativo = 0
    for n in numero:
        if n > 0:
            positivo += n
        elif n < 0:
            negativo += n
    print(f"Hay {positivo} números positivos")
    print(f"Hay {negativo} números positivos")
def multiplos_3(numero): # 1.3
    return numero % 3 == 0
# Inicio funciones opcion 2
def area(base, altura): # 2.1
    return base * altura
def perimetro(l1,l2, l3, l4 ): # 2.2
    return l1 + l2 + l3 + l4
# Inicio opcion 3


