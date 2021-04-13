print("Funciones en Phyton")
#reutilizacion de codigo  Don t Repeat yourself
# sea más fácil de mantener DRY
print("Hello word!")

numeros=list(range(2, 20))
print(numeros)
str(12)
range(10,20,3)
#cuantos argumentos hay en esta función.
numeros2=list(range(0,100,5))
print(numeros2)
print(len(numeros2))

def mi_func():
    print("spam")
    print("spam")
    print("spam")
mi_func()


def hello():
    print("Hi!")
hello()

Hello

def Hello():
    print("hello word!")
Hello()


def sayHi():
    print("Hi!")
sayHi()


#Argumentos
def print_whit_exclamation(word):
    print(word+"!")
print_whit_exclamation("spam")
print_whit_exclamation("eggs")
print_whit_exclamation("python")


#¿Cuál es el resultado de este código?
def print_double(x):
    print(2*x)
print_double(3)


def print_sum_twice(x,y):
    print(x+y)
    print(x+y)
print_sum_twice(5, 8)

#Argumentos
def function(variable):
    variable += 1
    print(variable)


function (7)
print(variable)


x= int(input("numero"))
def even(x):
    if x%2 ==0:
        print("Yes")
    else:
        print("No")
print(even(2))
#Que me devuelva el valor mayor entre dos numeros

def max(x, y):
    if x >= y:
        return x
    else :
        return y 

print(max(4,7))
z=max(8,5)
print(z)

# completa los espacios en blanco para definir una función que compare las loguitudes de 
# sus argumentos y devuelva el más corto

def shortest_string(x,y):
    if len(x)<= len(y):
        return  x
    else:
        return y


#devolución de valores de funciones 
#una vez que devuelvas un valor de un función, esta deja de ser ejecutada inmediatamente
#cualquier código luego de la sentencia retun nunca ocurrirá.

def add_numbers(x, y):
    total = x+y
    print("This won't be printed")
    return total
    print("This won't be printed") # las cosas despues de el return no ocurren 

print(add_numbers(4,5))

def print_numbers():
    print(1)
    print(2)
    return
    print(4)
    print(6)


x=365
y=7
#this is a comment

print(x % y) #fin the remainder
#print(x//y)
#another comment

#DOCSTRINGS (cadena de documentación) cumple un propósito similar de los 
#comentarios pero están diseñados por explicar el código.
#Sin embargo, son más específicos y tienen una sintaxis distinta. Son creados colocando una cadena multilinea
#que contenga un explicación de la función por debajo de la primera línea de la función.

def shout(word):
    """
    Print a word with an exclamation
    mark following it
    """
    print(word+"!")
shout("hola")


def multiply (x,y):
    return x*y

a=4
b=7
operation = multiply
print(operation(a,b)) 


def shout(word):
    return word + "!"
speak = shout
output = speak("shout")
print(output)

def add(x,y):
    return x+y
def do_twice(func, x, y):
    return func(func(x,y), func(x,y))

a = 5
b = 10
print(do_twice(add, a,b))



def square(x):
    return x*x

def test(func, x):
    print(func(x))

test(square,42)

#Módulos 
import ramdom
for i in range(5):
    value = ramdom.randit(1, 6)
    print(value)


def cuad(j,i=1,x=2*j-1,suma=1,b=(j**2))
    while i <= x:
    i=i+1
    if (i%2 ==0):
        print(i,"no suma")
    if (i%2 !=0):
        #print(i)
        suma+=i
        if (suma==b):
            print('La suma de los',j, 'primeros numeros impares es',suma, 'y esto es es igual a',j,'elevado al cuadrado,por lo tanto se determina esta igualdad')
           
    print("¡Terminado!")


# Suma de los valores im