
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
def es_primo(numero):
    if numero < 2:
        print("Es primo")
        for n in range(2, numero):
            if numero % n == 0:
                print("No es primo")
# Inicio opcion 4
def promedios_(nota): # 4
    promedio = sum(nota) / len(nota)
    return promedio
def promedio_mayor(nota): # 4.1
    contador = 0
    for n in nota:
        if n >= 85:
            contador += 1
        else:
            print("Dato inválido, intente de nuevo")

    print(f"Hay {contador} promedios mayores o iguales a 85")
def zona_riesgo(nota):
    contador = 0
    for n in nota:
        if n in nota:
            if n < 60:
                contador += 1
            else:
                print("Dato inválido, intente de nuevo")
    print(f"Hay {contador} promedios en zona de riesgo")
# Inicio opcion 5
def numero_mayor(numeros):
    maximo = max(numeros)
    print(f"El número máximo es {maximo}")
def numero_menor(numeros):
    minimo = min(numeros)
    print(f"El número minimo es {minimo}")
def cuantos_repiten(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    for n in range(0, numeros):
        if n == maximo:
