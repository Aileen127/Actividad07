
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
            positivo += 1
        elif n < 0:
            negativo += 1
    print(f"Hay {positivo} números positivos")
    print(f"Hay {negativo} números positivos")
def multiplos_3(numero): # 1.3
    multiplo =  numero % 3
    for n in numeros:
        contador = 0
        if multiplo == 0:
           contador += 1
        else:
            print("No es multiplo de 3")
    print(f" {contador} números son multiplos de 3")
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
def numero_mayor(numeros):# 5.1
    maximo = max(numeros)
    print(f"El número máximo es {maximo}")
def numero_menor(numeros): # 5.2
    minimo = min(numeros)
    print(f"El número minimo es {minimo}")
def cuantos_repiten(numeros): # 5.3
    maximo = max(numeros)
    minimo = min(numeros)
    frecuencia_maximo = numeros.count(maximo)
    frecuencia_minimo = numeros.count(minimo)
    print(f"La frecuencia de máximos es de: {frecuencia_maximo}")
    print(f"La frecuencia de mínimos es de: {frecuencia_minimo}")
# Inicio opcion 6
def suma(a,b): # 6.1
    return a + b
def resta(a,b): # 6.2
    return a - b
def multiplicacion(a,b): #6.3
    return a * b
def division(a,b): # 6.4
    return a / b

# Menu
while True:
    print("\nBienvenido al menú")
    print("1.Ingresar una lista de n números reales y mostrar: \n 1. Suma total \n2. Promedio\n3. Cantidad de positivos negativos y ceros \n4. Cuántos son múltiplos de 3")
    print("2. Area y perimetro de rectangulo")
    print("3. Verificar si un número es primo")
    print("4. Calcular el promedio e indicar \n 1. Cuántas son mayores o iguales a 85 \n 2. Cuántas están en zona de riesgo")
    print("5. Ingresar una lista n números enteros y mostrar \n El  número mayor \n 2. El número menor \n 3. frecuencia")
    print("6. Calculadora de operaciones básicas (suma, resta, multiplicación, división) ")
    print("7. Salir")

    option = input("Ingresa una opción (1-7): ")

    match option:
        case "1":
            numeros = []
            while True:
                numero = float(input("Ingresa los números que deseas evaluar, ingresa 0 si ya NO deseas ingresar más números: "))
                if numero != 0:
                    numeros.append(numero)
                elif numero == 0:
                    break
            print(f"La suma total es de: {suma_total(numeros)}")
            print(f"El promedio total es de: {promedio(numeros)}")
            positivos_negativos(numeros)
            multiplos_3(numero)
        case []
        case "7":
            break
