# Qué es Python? 🐍
Es un lenguaje de programación multiparadigma uitilizado para diseñar aplicaciones y programas de computadoras .
# Qué es una variable?🤖
Una variable es parecida a una caja o un lugar donde puedo almacenar objetos como texto, numeros, etc, al momento de escribir una varible no puede empezar por números y debe estar en minúscula. Al momento de poner más palabras para nombrar una variable tendremos que separarlas con un guión bajo y debe tener un máximo de 15 caracteres.   

## Nombrando una variable 💻
Al momento de nombrar una variable tenemos que seguir las reglas básicas como empezar escribiendo en minúscula y con letras, si queremos escribir más palabras separarlas con guión bajo y tener un máximo de 15 caracteres.
```python 
variable_uno = 

```

## Asignando valores a una variable 📝
Podemos asignar diferentes valores ya sean números o palabras.
```python 
variable_uno = 3
variable_dos = [perro, gato]
```
## Operadores básicos 📝
los mas basicos son:
 
suma : +

resta : -

multiplicación : *

división : /

división entera : //

módulo : % 

potenciación : **



### Suma 📝
 
```python
a = 7 
b = 8 

# Creamos la variable sum para realizar la operación 

sum = a + b 

# Hacemos un print para imprimir los resultados, podemos añadir una referencia entre comillas

print('suma total:', sum)
[salida] = suma total: 15 
```
### Resta 📝

```python
a = 10
b = 5

# Creamos la variable rest para realizar la operación 

rest = a - b 

# Hacemos un print para imprimir los resultados, podemos añadir una referencia entre comillas

print('resta total:', rest)
[salida] = resta total: 5
```
### Multiplicación 📝

```python
a = 5
b = 9

# Creamos la variable multi para realizar la operación 

multi = a * b 

# Hacemos un print para imprimir los resultados, podemos añadir una referencia entre comillas

print('multiplicación total:', multi)
[salida] = multiplicación total: 45
```
### División 📝

```python
a = 100
b = 4

# Creamos la variable división para realizar la operación 

división = a / b 

# Hacemos un print para imprimir los resultados, podemos añadir una referencia entre comillas

print('división total:', división)
[salida] = división total: 25
```
### Módulo 📝

```python
a = 100
b = 4

# Creamos la variable mod para realizar la operación 

mod = a % b 

# Hacemos un print para imprimir los resultados, podemos añadir una referencia entre comillas.

print('modulo:', mod)
[salida] = modulo: 0
```
# Tipos de datos en Python 🤖

## Integer 💻
Son los numeros enteros los cuales no contienen decimáles, pueden ser positivos o negativos.

Ejemplo: 

x = 30 

y = -8

z = 100

## Float 📝
Es utilizado para reperesentar números decimáles, pueden ser positivos o negativos 

Ejemplo:

x = 10.9

y = -4.6

z = 0.7

## String 📝
Se utiliza para representar una cadena de carácteres o palabras.

Ejemplo:

print("Buenas tardes")

## Casting en Python 📝
Es la técnica que sirve para convertir un dato de un tipo a un tipo diferente.

Ejemplo: 

int(entero) a str(texto) : str(81) 

str(letras) a int(enteros) : int('28')

float(decimales) a int(enteros) : int(5.9)

## List 📝
Sirven para crear estructuras de datos de manera ordenada, no hace falta que sean del mismo tipo.

Ejemplo:
```python
list = [1,2,3,4,'l']

print(list)

[salida] =  [1,2,3,4,'l']
```

## Tuple 📝
Es una estructura de datos propia de python que permite almacenar distintos valores, son inmutables ya que no cambian una vez inicializadas.Pueden contener diferentes tipos de datos ya sean decimales, enteros, texto, etc.

Ejemplo:
```python
tuple = (1,2,3)

print(tuple)

[salida] = (1,2,3)
```
## Dictionary 📚
Es utilizado para almacenar valores de datos en pares clave:valor, sirve para coleccionar información tal como un diccionario normal y corriente de manera ordenada.

Ejemplo:
```python
diccionario = ('azul':'blue', 'verde':'green', 'rojo':'red')

print(diccionario[azul])

[salida] = blue
```
# Tomando decisiones 🤖

## Sentencia if 🖥️
En python podemos ingresar diferentes condiciones lógicas como:

igual a : a == b 

diferente de : a != b

mayor que : a > b 

menor que : a < b 

mayor o igual que : a >= b 

menor o igual que : a <= b 

Al momento de utilizar if estamos realizando una pregunta que seria ' si la condicion es asi entonces imprimo'.

Ejemplo:

a = 3 

b= 7

if b > a :
 
 print('b es mayor que a')
 
 ## sentencia elif 🖥️
Esta sentencia esta relacionada con if ya que si no cumplimos el 'if' intervine 'elif' haciendo la pregunta 'si las condiciones anteriores no funcionan, entonces intente con esta nueva condición'. 

Ejemplo:

a = 11

b= 11

if a > b:

print('a es mayor a b')

elif a == b:

print('a es igual a b')

## Ciclo For 🖥️
E bucle for recorre la colección elemento por elemento depeniendo de los elementos que haya seran la cantidad de veces que se repita, el elemento puede estar compuesto por cualquier dato no importa si son str, int o float lo único que tomara en cuenta sera la cantidad de elementos que haya.

Ejemplo:
```python
coleccion = [1,2,3,'hola']
for i in coleccion:
print(f'elemento:{i}')
[salida] = 
elemento: 1 
elemento: 2 
elemento: 3
elemento: hola
```

## Ciclo While 🖥️
Se lo conoce por ser un bucle indeterminado de iteraciones donde necesitamos que se cumpla una condición para que el bucle se siga ejecutando.

Ejemplo:
```python
import math

numero = int(input('ingrese un numero:'))
while numero < 0 :
 print('error')
numero = int(input('ingrese un numero:'))
print(f'su raiz cuadrada es: {(math.sqrt(numero))}')

```
## Break 🖥️
Es una palabra reservada y sirve para romper un ciclo.

Ejemplo: 

```python
a= 0

for i in range(11):
    a += 1
    print('i:',i, 'a:',a)
    if a ==10:
        break

```
## Continue 🖥️
Es una palabra reservada, comparte semejanzas con el break pero en vez de romper el ciclo continua con uno diferente.

Ejemplo:

```python
a= 0

for i in range(10):
    a += 2
    print('i:',i, 'a:',a)
    if a >= 2 and a <=18:
        continue
    print('el valor de j:',j)    
    
``` 
