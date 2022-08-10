# Repaso Python

Para comenzar a programar en Python con librerias, necesitamos saber los conceptos básicos de la programación. En este repaso, vamos a ver los conceptos básicos de la programación y cómo aplicarlos en Python.

## Variables
Las variables son espacios de memoria que almacenan datos. En Python, las variables se declaran de la siguiente manera:

```python
variable = 1
```

En este caso, la variable `variable` almacena el valor `1`. En Python existen diferentes tipos de datos que podemos almacenar en una variable. Estos son:

- `int`: Números enteros
- `float`: Números decimales
- `str`: Cadenas de texto
- `bool`: Valores booleanos

```python
variable = 1 # int
variable = 1.0 # float
variable = "Yaqhu" # str
variable = True # bool
```

Debemos recordar que los valores booleanos (bool) solo pueden ser `True` o `False`.

## Input

El input es una función que nos permite pedirle al usuario que ingrese un valor. En Python, la función input se utiliza de la siguiente manera:

```python
variable = input("Ingresa un valor: ")
```

En este caso, la variable `variable` almacena el valor que el usuario ingrese. Si el usuario ingresa el valor `1`, la variable `variable` almacena el valor `1`.

## Output

El output es una función que nos permite mostrar un valor en la consola. En Python, la función print se utiliza de la siguiente manera:

```python
print("Hola mundo")
```

En este caso, la función print muestra el texto `Hola mundo` en la consola.

## Operadores

Los operadores son símbolos que nos permiten realizar operaciones matemáticas. En Python, existen diferentes tipos de operadores:

- `+`: Suma
- `-`: Resta
- `*`: Multiplicación
- `/`: División
- `//`: División entera
- `%`: Módulo
- `**`: Potencia

```python
1 + 1 = 2 # Suma
1 - 1 = 0 # Resta
2 * 2 = 4 # Multiplicación
4 / 2 = 2 # División
4 // 2 = 2 # División entera
4 % 2 = 0 # Módulo
2 ** 2 = 4 # Potencia
```
La división entera (`//`) nos permite obtener el resultado de la división sin decimales. 

El modulo nos permite obtener el residuo de una división. Por ejemplo, si dividimos 4 entre 2, el residuo es 0. Si dividimos 5 entre 2, el residuo es 1.

## Condicionales

Los condicionales nos permiten ejecutar un bloque de código si se cumple una condición. En Python, existen diferentes tipos de condicionales:

- `if`: Si se cumple una condición, se ejecuta un bloque de código
- `elif`: Si se cumple una condición, se ejecuta un bloque de código
- `else`: Si no se cumple ninguna condición, se ejecuta un bloque de código

```python
if 1 == 1:
    print("1 es igual a 1")
elif 1 == 2:
    print("1 es igual a 2")
else:
    print("1 no es igual a 1 ni a 2")
```

## Ciclos o bucles

Los ciclos o bucles nos permiten ejecutar un bloque de código varias veces. En Python, existen diferentes tipos de ciclos:

- `while`: Mientras se cumpla una condición, se ejecuta un bloque de código
- `for`: Para cada elemento de una lista, se ejecuta un bloque de código

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

Como hemos visto mientras se cumpla la condición `i < 10`, se ejecuta el bloque de código. En este caso, el bloque de código es `print(i)`. Además, en cada iteración, se incrementa el valor de `i` en 1.

```python
for i in range(10):
    print(i)
```

En este caso, el ciclo `for` recorre cada elemento de la lista `range(10)`. En este caso, la lista `range(10)` contiene los números del 0 al 9. Por lo tanto, el bloque de código se ejecuta 10 veces.

## Funciones

Las funciones son bloques de código que realizan una tarea específica. En Python, las funciones se declaran de la siguiente manera:

```python
def funcion():
    print("Hola mundo")
```

Para ejecutar una función, debemos llamarla:

```python
funcion()
```

Las funciones pueden recibir parámetros:

```python
def funcion(parametro):
    print(parametro)
```

Para ejecutar una función con parámetros, debemos llamarla y pasarle los parámetros:

```python
funcion("Yaqhu Developers")
```

Las funciones pueden retornar un valor:

```python
def funcion():
    return "Hola mundo"
```

Para obtener el valor retornado por una función, debemos llamarla y asignarla a una variable:

```python
variable = funcion()
```

## Listas

Las listas son estructuras de datos que nos permiten almacenar varios valores. En Python, las listas se declaran de la siguiente manera:

```python   
lista = [1, 2, 3, 4, 5]
```

Para acceder a un elemento de una lista, debemos indicar el índice del elemento:

```python
lista[0] # 1
lista[1] # 2
lista[2] # 3
lista[3] # 4
lista[4] # 5
```

Si intentamos acceder a un elemento que no existe, obtendremos un error:

```python
lista[5] # IndexError: list index out of range
```
En cambio, si intentamos acceder a `lista[-1]`, obtendremos el último elemento de la lista:

```python
lista[-1] = 5
```

Estos indices no solo nos permiten acceder a los elementos de una lista, también nos permiten modificarlos:

```python
lista[0] = 10
lista[1] = 20
lista[2] = 30
lista[3] = 40
lista[4] = 50
```

Las listas también nos permiten almacenar diferentes tipos de datos:

```python
lista = [1, 2.0, "Yaqhu", True]
```

Las listas también nos permiten almacenar otras listas:

```python
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Para acceder a un elemento de una lista anidada, debemos indicar el índice de la lista y el índice del elemento:

```python
lista[0][0] # 1
lista[0][1] # 2
lista[0][2] # 3
lista[1][0] # 4
lista[1][1] # 5
lista[1][2] # 6
lista[2][0] # 7
lista[2][1] # 8
lista[2][2] # 9
``` 

Las listas también nos permiten agregar elementos:

```python
lista = [1, 2, 3]
lista.append(4)
lista.append(5)
```

Para ello utilizamos el método `append()`. Este método recibe un parámetro, el elemento que queremos agregar a la lista.

Las listas también nos permiten eliminar elementos:

```python
lista = [1, 2, 3, 4, 5]
lista.pop(0)
```

Para ello utilizamos el método `pop()`. Este método recibe un parámetro, el índice del elemento que queremos eliminar de la lista. En este caso, eliminamos el primer elemento de la lista que es `1`.

Las listas también nos permiten ordenar sus elementos:

```python
lista = [5, 4, 3, 2, 1]
lista.sort()
```

Para ello utilizamos el método `sort()`. Este método no recibe ningún parámetro. En este caso, ordenamos los elementos de la lista de menor a mayor. Si queremos ordenar los elementos de mayor a menor, debemos utilizar el método `sort(reverse=True)`.

Las listas también nos permiten invertir sus elementos:

```python
lista = [1, 2, 3, 4, 5]
lista.reverse()
```

Para ello utilizamos el método `reverse()`. Este método no recibe ningún parámetro. En este caso, invertimos los elementos de la lista.

Las listas también nos permiten contar la cantidad de veces que un elemento se encuentra en la lista:

```python
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
lista.count(1) # 2
lista.count(2) # 2
lista.count(3) # 2
lista.count(4) # 2
lista.count(5) # 2
```

Para ello utilizamos el método `count()`. Este método recibe un parámetro, el elemento que queremos contar. En este caso, contamos la cantidad de veces que se encuentra el número `1` en la lista.

Las listas también nos permiten obtener el índice de un elemento:

```python
lista = [1, 2, 3, 4, 5]
lista.index(1) # 0
lista.index(2) # 1
lista.index(3) # 2
lista.index(4) # 3
lista.index(5) # 4
```

Para ello utilizamos el método `index()`. Este método recibe un parámetro, el elemento del que queremos obtener el índice. En este caso, obtenemos el índice del número `1` en la lista.

Las listas también nos permiten insertar un elemento en un índice determinado:

```python
lista = [1, 2, 3, 4, 5]
lista.insert(0, 0)
lista.insert(6, 6)
```

Para ello utilizamos el método `insert()`. Este método recibe dos parámetros, el índice y el elemento que queremos insertar. En este caso, insertamos el número `0` en el índice `0` y el número `6` en el índice `6`.

Las listas también nos permiten eliminar un elemento:

```python
lista = [1, 2, 3, 4, 5]
lista.remove(1)
lista.remove(5)
```

Para ello utilizamos el método `remove()`. Este método recibe un parámetro, el elemento que queremos eliminar. En este caso, eliminamos el número `1` y el número `5`.

Las listas también nos permiten eliminar todos los elementos:

```python
lista = [1, 2, 3, 4, 5]
lista.clear()
```

Para ello utilizamos el método `clear()`. Este método no recibe ningún parámetro. En este caso, eliminamos todos los elementos de la lista.

Las listas también nos permiten copiar una lista:

```python
lista = [1, 2, 3, 4, 5]
lista_copia = lista.copy()
```

Para ello utilizamos el método `copy()`. Este método no recibe ningún parámetro. En este caso, copiamos la lista `lista` en la lista `lista_copia`.

Las listas también nos permiten extender una lista:

```python
lista = [1, 2, 3, 4, 5]
lista.extend([6, 7, 8, 9, 10])
```

Para ello utilizamos el método `extend()`. Este método recibe un parámetro, la lista que queremos extender. En este caso, extendemos la lista `lista` con la lista `[6, 7, 8, 9, 10]`.

Las listas también nos permiten obtener el máximo de una lista:

```python
lista = [1, 2, 3, 4, 5]
lista.max() # 5
```

Para ello utilizamos el método `max()`. Este método no recibe ningún parámetro. En este caso, obtenemos el máximo de la lista `lista`.

Las listas también nos permiten obtener el mínimo de una lista:

```python
lista = [1, 2, 3, 4, 5]
lista.min() # 1
```

Para ello utilizamos el método `min()`. Este método no recibe ningún parámetro. En este caso, obtenemos el mínimo de la lista `lista`.

Las listas también nos permiten obtener la suma de una lista:

```python
lista = [1, 2, 3, 4, 5]
lista.sum() # 15
```

Para ello utilizamos el método `sum()`. Este método no recibe ningún parámetro. En este caso, obtenemos la suma de la lista `lista`.

Las listas también nos permiten obtener el promedio de una lista:

```python
lista = [1, 2, 3, 4, 5]
lista.avg() # 3.0
```

Para ello utilizamos el método `avg()`. Este método no recibe ningún parámetro. En este caso, obtenemos el promedio de la lista `lista`.

Las listas también nos permiten obtener la longitud de una lista:

```python
lista = [1, 2, 3, 4, 5]
lista.len() # 5
```

Para ello utilizamos el método `len()`. Este método no recibe ningún parámetro. En este caso, obtenemos la longitud de la lista `lista`.

## Bucles anidados

Los bucles anidados son bucles que se encuentran dentro de otros bucles. Por ejemplo:

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i, j)
```

En este caso, tenemos un bucle `for` que se encuentra dentro de otro bucle `for`. El primer bucle `for` recorre los números del `1` al `10`. El segundo bucle `for` recorre los números del `1` al `10`. Por cada iteración del primer bucle `for`, se ejecuta el segundo bucle `for` y se imprime el valor de `i` y `j`.

## Bucles infinitos

Los bucles infinitos son bucles que no tienen una condición de parada. Por ejemplo:

```python
while True:
    print("Hola")
```

En este caso, tenemos un bucle `while` que se ejecuta siempre. Por cada iteración, se imprime el texto `Hola`.

## Bucles con `break`

Los bucles con `break` son bucles que se ejecutan hasta que se cumple una condición. Por ejemplo:

```python
while True:
    print("Hola")
    if input("¿Desea salir? (s/n): ") == "s":
        break
```

En este caso, tenemos un bucle `while` que se ejecuta siempre. Por cada iteración, se imprime el texto `Hola` y se pregunta si se desea salir. Si se ingresa la letra `s`, se rompe el bucle `while` y se termina la ejecución del programa.

## Bucles con `continue`

Los bucles con `continue` son bucles que se ejecutan hasta que se cumple una condición. Por ejemplo:

```python
while True:
    print("Hola")
    if input("¿Desea salir? (s/n): ") == "s":
        continue
    break
```

En este caso, tenemos un bucle `while` que se ejecuta siempre. Por cada iteración, se imprime el texto `Hola` y se pregunta si se desea salir. Si se ingresa la letra `s`, se continua la ejecución del bucle `while`. Si se ingresa cualquier otra letra, se rompe el bucle `while` y se termina la ejecución del programa.

## Bucles con `else`

Los bucles con `else` son bucles que se ejecutan hasta que se cumple una condición. Por ejemplo:

```python
while True:
    print("Hola")
    if input("¿Desea salir? (s/n): ") == "s":
        break
else:
    print("Adiós")
```

En este caso, tenemos un bucle `while` que se ejecuta siempre. Por cada iteración, se imprime el texto `Hola` y se pregunta si se desea salir. Si se ingresa la letra `s`, se rompe el bucle `while` y se termina la ejecución del programa. Si se ingresa cualquier otra letra, se ejecuta el código que se encuentra después del `else` y se imprime el texto `Adiós`.

## Bucles con `pass`

Los bucles con `pass` son bucles que se ejecutan hasta que se cumple una condición. Por ejemplo:

```python
while True:
    print("Hola")
    if input("¿Desea salir? (s/n): ") == "s":
        pass
    break
```

En este caso, tenemos un bucle `while` que se ejecuta siempre. Por cada iteración, se imprime el texto `Hola` y se pregunta si se desea salir. Si se ingresa la letra `s`, se ejecuta el código que se encuentra después del `pass` y se rompe el bucle `while` y se termina la ejecución del programa.

## Siguientes pasos

Ahora que ya conoces los conceptos básicos de Python es tiempo de que pongas en práctica lo aprendido. Para ello, te recomiendo que realices los siguientes ejercicios:

- [Ejercicios de Python](https://platzi.com/clases/1557-python/20201-ejercicios-de-python/)