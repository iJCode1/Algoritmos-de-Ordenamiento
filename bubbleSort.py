print("Metodo BubbleSort en Python!")

# Paso 1: Crear la funcion que realizara el metodo.

def bubbleSort1(array):
    n = len(array) #Con len() se obtiene el tamaño de un vector.
    for i in range(n): # Se crea el Primer For: Nos ayudara a recorrer dependiendo el tamaño del vector/lista
        print (array)
        for j in range(0, n-i-1): #Se crea un for anidado, el cual nos ayudara a comprobar los valores para que funcione el metodo.
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

precios = [127,40, 800, 23, 67, 2302, 190, 1, 3452, 2]

bubbleSort1(precios)

print("El arreglo ordenado Ascendentemente es:")
for i in precios:
    print(i),