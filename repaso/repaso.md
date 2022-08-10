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