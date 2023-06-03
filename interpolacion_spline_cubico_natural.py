import numpy as np

#Estamos interpolando la funcion e^x
def funcion_interpolar(n):
    return pow(n,2) + 5

#Esta funcion nos va a devolver la interpolacion cubica
def interpolar(n):
    i = 0
    indicex = []
    indicey = []
    h = []

    #Preguntandole al usuario que digite valores de x para poder generar su respectivo f(x), es decir sus intervalos
    while i <= n:
        x = int(input('Digite un valor: \n'))
        indicex.append(x)
        i += 1
    
    for elemento in indicex:
        y = funcion_interpolar(elemento)
        indicey.append(y)
    
    #Esta contenido el valor x con el valor de la funcion f(x)
    subintervalos = np.array([indicex, indicey])

    i = 0
    #Para calcular los h
    while i < n:
        diferencia = indicex[i+1] - indicex[i]
        h.append(diferencia)
        i += 1
    
    #Para calcular los a's
    a = indicey
    
    #Para generar la matriz_A, estamos generando la matriz de 0's
    Matriz_A = np.zeros((n+1 , n+1), dtype=int)

    fila = 0
    columna = 0

    while fila < len(Matriz_A):
        while columna < len(Matriz_A):
            #Esto es en la diagonal principal, es decir calculando esa parte
            if columna == fila and (fila == 0 and columna == 0) or (fila == len(Matriz_A) - 1 and columna == len(Matriz_A) - 1):
                Matriz_A[fila][columna] = 1
            
            #Ahora fuera de los extremos de la diagonal se rellena con la formula de 2(h(0) + h(1) + ...)
            if columna == fila and (fila > 0 and columna > 0) and (fila < len(Matriz_A) - 1 and columna < len(Matriz_A) - 1):
                Matriz_A[fila][columna] = 2 * (h[columna-1] + h[columna])
            
            #Ahora rellenamos cuando el valor de la columna exceda al valor de la fila en 1
            if columna - fila == 1 and fila > 0:
                Matriz_A[fila][columna] = h[columna-1]

            #Ahora rellenamos cuando el valor de la fila exceda al valor de la columna en 1
            if fila - columna == 1 and fila < len(Matriz_A) - 1:
                Matriz_A[fila][columna] = h[fila - 1]

            columna += 1

        columna = 0
        fila += 1

    #Ahora generaremos la Matriz_B 
    Matriz_B = np.zeros((n+1,1))
    fila = 0
    columna = 0
    while fila < len(Matriz_B):
        if fila > 0 and fila < len(Matriz_B) -1:
            Matriz_B[fila][columna] = (3 * (a[fila+1] - a[fila]))/ (h[fila]) - (3 * (a[fila] - a[fila-1]))/ (h[fila - 1])
        fila += 1
    
    #Ahora calcularemos la matriz inversa para poder hallar la ecuacion matricial de AX = B donde la matriz X esta contenido los valores de c
    Matriz_A_Inversa = np.linalg.inv(Matriz_A)
    
    #Ahora calculamos la matriz X que es igual a X = A elevado a la -1 * B que hallará los valores de c
    c = np.dot(Matriz_A_Inversa, Matriz_B)
    
    #Ahora calcularemos los elementos de b para las ecuaciones interpolantes
    i = 0
    b = []
    while i < n:
        element = (a[i+1] - a[i]) / (h[i]) - (h[i]) * (c[i+1] + 2*c[i]) / 3
        b.append(element)
        i += 1
    
    #Ahora calculamos los elementos de b para las ecuaciones interpolantes
    i = 0
    d = []
    while i < n:
        element = (c[i+1] - c[i]) / 3*h[i]
        d.append(element)
        i += 1
    
    #Ahora imprimimos las ecuaciones interpolantes
    i = 0
    mensaje = ''
    while i < n:
        mensaje1 = f'{a[i]} + {b[i]}(x - {indicex[i]}) + {c[i]}(x - {indicex[i]})^2 + {d[i]}(x - {indicex[i]})^3 para x pertenece [{indicex[i]}, {indicex[i+1]}]'
        mensaje = mensaje1 + '\n' + mensaje
        i += 1
    
    return mensaje
    

cantidad_ecuaciones = int(input('Digite la cantidad de ecuaciones que se va a mostrar\n'))
print(interpolar(cantidad_ecuaciones))  