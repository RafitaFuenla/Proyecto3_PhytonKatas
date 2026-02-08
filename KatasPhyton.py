# %% [markdown]
# ### PROYECTO KATAS PHYON

# %% [markdown]
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

# %%
def contar_letras(texto):
    frecuencias = {}

    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1

    return frecuencias


resultado = contar_letras("Cuantas letras tendra esto")
print(resultado)

# %% [markdown]
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

# %%
numeros = [90, 12, 45, 76, 8, 54, 3] # Creo lista con numeros

def duplicar (n): # Establezco funcion de duplicar
    return n * 2 

numeros_doble = list(
    map(duplicar,numeros)) # Aplico map() con funcion de duplicar y lista nueva para guardar los duplicados

print(numeros_doble)


# %% [markdown]
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# %%
lista = ["casa", "caseta", "perro", "escasa"] #Creo lista con palabaras
objetivo = "cas" #Creado el objetivo a buscar


def buscar_palabra(lista, objetivo): # Creamos definicion que busque el objetivo dentro de la lista
    resultado = [] # Creamos lista vacia para añadir el resultado
    for item in lista: # Recorremos lista
        if objetivo.lower() in item.lower(): # Objetivo (min) esta en item (min)
            resultado.append(item) #Agremos a lista vacia
    return resultado
    
print (buscar_palabra(lista, objetivo))
        

# %% [markdown]
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

# %%
num = [8, 15, 3, 20, 7] # Creo 2 listas con numeros
num2 = [5, 10, 1, 12, 2]

def diferencia (a, b): # Establezco funcion de restar
    return a - b 

diferencia_numeros = list(
    map(diferencia,num,num2)) # Aplico map() con funcion de restar y lista nueva para guardar los duplicados

print (diferencia_numeros)

# %% [markdown]
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

# %%
lista_num = [4, 6, 1, 5, 9, 3, 9]
nota_aprobado = 5

def media_y_comprobar_nota(lista_num, nota_aprobado=5):
    media = sum(lista_num) / len(lista_num)

    if media >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"

    return media, estado


print(media_y_comprobar_nota(lista_num))


# %% [markdown]
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

# %%
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(7))


# %% [markdown]
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

# %%
lista_tupla = [("rafa", 37),("maria",40)] # Creo una lsita con tuplas

def tupla_to_string(tupla): 
        return tupla[0] + " " + str(tupla[1]) # Funcion para pasar int a str

tupla_string = list(map(tupla_to_string, lista_tupla)) # Mapeado de la lista
        
print(tupla_string)

# %% [markdown]
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

# %%

def division_input (num1,num2): #Crear funcion de diviison de dos numeros
    return num1 / num2

try : 
    numero1_usuario = int(input(f"Introduce un numero")) # Pedimos por consola dos numeros y lo ¿casteamos? a int
    numero2_usuario = int(input(f"Introduce otro numero")) 
    print(division_input(numero1_usuario,numero2_usuario))
    
except ZeroDivisionError: # Añadimos excepciones para los input e impresion (no dividir entre cero)
    print(f'No se puede dividir entre 0')
    
except ValueError: # Añadimos excepciones para los input e impresion (tipo de dato incorrecto)
    print(f'Hay que introducir NUMEROS')

# %% [markdown]
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

# %%
mascotas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Perro", "Gato", "Conejo", "Hámster", "Loro", "Iguana", "Hurón"]
mascotas_excluidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def filtrar_mascotas (animal):
    return animal not in mascotas_excluidas #Creamos funcion con "busqueda" de un item en la lista

list(filter(filtrar_mascotas, mascotas)) # Filtramos con lista y funcion

# %% [markdown]
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# %%
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55] # Lista de numeros

def calcular_promedio(num):
    if len(num)==0: # Comprobamos si hay algun elemento en la lista
       raise Exception ("Lista vacia") # Guardamos excepcion de error y mensaje
    return sum(num)/len(num) #Funcion para sumar y dividir entre el numero de elementos de la lista

try: 
    print(calcular_promedio(numeros))
except Exception as error:
    print(error) #imprimimos mensaje guardado en raise


# %% [markdown]
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# %%
try:
    edad = int(input(f"Introduce tu edad"))# Pedimos por consola edad y lo casteamos a int
    if edad < 0 or edad > 120: # Comprobamos rango de edad correcto
        raise Exception ("Edad fuera de rango") # Guardamos excepcion de error y mensaje

except ValueError: # Error de datos no numericos
    print("Introduce datos numericos") 

except Exception as error: # Error de excepcion y mensaj guardado
    print(error)

# %% [markdown]
# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

# %%
frase_mundo = "Hola de nuevo mundo" 
frase_mundo.split() # Separamos el string en apalbras

def longitud_palabra(palabra): # Creamos funcion para contar letras de una palabra
    return len(palabra)


print(list(map(longitud_palabra, frase_mundo.split()))) # Imprimimos meapado de lista con funcion de separar palabras y contar letras de cada palabra

# %% [markdown]
# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# %%
tupla_string = list(map(tupla_to_string, lista_tupla)) # Mapeado de la lista

# %% [markdown]
# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

# %%
frutas_filter = ["manzana", "pera", "melón", "uva"] 
letra_buscar = "m" # Variable con letra  a buscar

resultado = list(filter(lambda palabra: palabra[0] == letra_buscar, frutas_filter))  # Creo  filtrado de funcion lambda con busqueda por filtro

print(resultado) 

# %% [markdown]
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# %%
lista_numeros_sumar3 = [8, 4, 5, 9, 10, 2]

resultado_suma = list(map(lambda numero: numero + 3, lista_numeros_sumar3)) #Funcion lambda que suma 3 a cada elemento de la lista

print(resultado_suma)


# %% [markdown]
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

# %%
cadena_texto = 'Esto es la cadena de texto que usaremos'
cadena_texto.split() # Separamos el string en apalbras
n_letras = 4



def longitud_palabra(palabra): # Creamos funcion para contar letras de una palabra y comprobar si la longitud es mayor que la solicitada
    return len(palabra) > n_letras

resultado = list(filter(longitud_palabra, cadena_texto.split())) # Filtramos creando lista de palabras mayores a n letras


print(resultado) 

# %% [markdown]
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce(). 

# %%
from functools import reduce

lista_numeros = [5, 7, 2]

resultado = reduce(lambda acumulado, numero: acumulado * 10 + numero, lista_numeros); #Junta cada numero con el siguiente, multiplicando por 10 y sumando el siguiente numero

print(resultado)



# %% [markdown]
# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# %%
estudiantes = [ # Lista con estudiantes 
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 72},
    {"nombre": "María", "edad": 19, "calificacion": 91},
    {"nombre": "Carlos", "edad": 21, "calificacion": 98}
]
comprobar_calificacion = 90 # Calificaion a comprobar

resultado = list(filter(lambda estudiante: estudiante["calificacion"] >= comprobar_calificacion, estudiantes)) # Lista con filtrado de funcion lambda, en la cual cmprueba la califiacion mayor o igual que la solicitada

print(resultado)


# %% [markdown]
# 19. Crea una función lambda que filtre los números impares de una lista dada.

# %%
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado = list(filter(lambda numero:numero %2!=0, numeros)) #Comrpobamos con lambda si el numero no es par

print(resultado)

# %% [markdown]
# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

# %%
lista_mixta = [1, "hola", 3, "mundo", 5, "Python", 7] 

resultado = list(filter(lambda lista:isinstance(lista, int),lista_mixta)) #Comprobamos tipo de dato de la lista con ISinINSTANCE y escogemos int.

print(resultado)

# %% [markdown]
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

# %%
cubo = lambda numero:numero ** 3

print(cubo(8))

# %% [markdown]
# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

# %%
from functools import reduce # Importamos funcion reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado = reduce((lambda acumulado, numero: acumulado * numero), numeros) #Reduce con lambda. Acumulado por el siguiente numero y repetimos.

print(resultado)

# %% [markdown]
# 23. Concatena una lista de palabras. Usa la función reduce().

# %%
palabras = ["Hola", "mundo", "desde", "Python"]

resultado = reduce((lambda acumulado, string: acumulado + string), palabras) #Reduce con lambda. Acumulado sumado a la siguiente palabra y repetimos.

print(resultado)

# %% [markdown]
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

# %%
numeros = [100, 10, 5, 2]

resultado = reduce((lambda acumulado, numero: acumulado - numero), numeros) #Reduce con lambda. Acumulado resta siguiente numero y repetimos.

print(resultado)

# %% [markdown]
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

# %%
cadena_texto = "Cuantos caracteres tendra esto"

def longitud_palabra(palabra): # Creamos funcion para contar caracteres de una cadena de texto
    return len(palabra) 

print(longitud_palabra(cadena_texto))

# %% [markdown]
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# %%
n1 = 8
n2 = 3

resto = lambda num1, num2: num1 % num2 #Lambda con comprobacion del resto entre dos numeros

print(resto(n1,n2))

# %% [markdown]
# 27. Crea una función que calcule el promedio de una lista de números.

# %%
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def calcular_promedio(num):
    return sum(num)/len(num) #Funcion para sumar y dividir entre el numero de elementos de la lista

print(calcular_promedio(numeros))

# %% [markdown]
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# %%
lista_duplicada = ["gato", "cerveza", "perro", 7, "vino", 7, "cerveza"]

def buscar_duplicado(lista):                    # Buscamos el primer elemento repetido
    elementos_vistos = []                       # Creo lista vacia para guardar los elementos ya vistos por pimera vez
    for elemento in lista:                      # Recorro la lista
        if elemento in elementos_vistos:        # Esta el elemento en la lista? 
            return elemento                     # Si esta en la lista de los ya vistos, es que es el primero que esta repetido, salimos del bucle. elemto encontrado
        else:
            elementos_vistos.append(elemento)   # Como NO esta repedito, lo añadimos a la lista vaica para seguir comprobando los siguientes elementos.

print(buscar_duplicado(lista_duplicada))


# %% [markdown]
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

# %%
convertir = 12345678901234

def enamascarar_texto(variable):                # Creamos funcion
    texto = str(variable)                       # COnvertimos variable a string
    cantidad_enmascarar = len(texto) - 4        # Guardamos longitud -4 de la variable
    enmascarado = "#" * cantidad_enmascarar     # El numero de longitud -4 lo convertimos a #
    ultimos_4 = texto[-4:]                      # Obtenemos los últimos 4 caracteres con un slicing (inicio -4: final)
    resultado = enmascarado + ultimos_4         # Juntamos todo
    return resultado

print(enamascarar_texto(convertir))

# %% [markdown]
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# %%
palabra1 = "amor"
palabra2 = "roma"

def anagramas(p1,p2):
    if sorted(p1) == sorted(p2): # Ordenamos las palabras alfabeticamente y comprobamos si son identicas
        return "Son iguales"
    else:
        return "No son anagramas" 
        

print(anagramas(palabra1, palabra2))

# %% [markdown]
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

# %%
entrada = input("Ingresa nombres separados por comas: ")            # Pido todos los nombres separados con coma
nombres = entrada.split(",")                                        # COn el metodo split, separo todos los nombres por la coma y se crea una lista con cada uno de los nombres

nombre_a_buscar = input("Ingresa el nombre que quieres buscar")     # Pido el nombre a buscar

def buscar_nombre(lista, nombre):                                   # Defino metodo
    if nombre in lista:                                             # Buscando el nombre dentro de la lista
        return "El nombre esta en la lista"                         # Si esta, imprimo mensaje
    else:                                                           # Si no, excpecion de error
        raise Exception ("Nombre no encontrado")                    # Guardamos excepcion de error y mensaje

try: 
    print(buscar_nombre(nombres, nombre_a_buscar))      
except Exception as error:
    print(error)                                                    # Imprimimos mensaje guardado en raise

# %% [markdown]
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# %%
empleados = [                                                       # Lista de empleados y puesto
    {"nombre": "Ana", "puesto": "Gerente"},
    {"nombre": "Luis", "puesto": "Desarrollador"},
    {"nombre": "Maria", "puesto": "Diseñadora"}
]

empleado_a_buscar = input("Que empleado quieres buscar?")           # Pido empleado a buscar

def buscar_empleado(dicc, empleados_bus):                           # Defino metodo
    for empleado in dicc:                                           # For recorriendo la lista
        if empleado["nombre"] == empleados_bus:                     # Accedo al nombre y comprado con el nombre a buscar
            return empleado["nombre"] + " es " + empleado["puesto"] # Si es el mismo, imprime mensaje confirmacion
    else:
        return "La persona no trabaja aqui"                         # Si no, imprime mensaje negacion

print(buscar_empleado(empleados, empleado_a_buscar))

# %%
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = list(map(lambda a, b: a + b, lista1, lista2))  # Lista mapeada de lamda con funcion de suma cada uno de los elementos de la lista 1 y 2

print(resultado)

# %% [markdown]
# 34. Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# Implementar el método quitar_rama para eliminar una rama en una posición específica.
# Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
# Caso de uso:
#         a. Crear un árbol.
#         b. Hacer crecer el tronco una unidad.
#         c. Añadir una nueva rama.
#         d. Hacer crecer todas las ramas una unidad.
#         e. Añadir dos nuevas ramas.
#         f. Retirar la rama situada en la posición 2.
#         g. Obtener información sobre el árbol.

# %%
class Arbol:
    def __init__(self): # Creamos el abjeto con su contructor 
        self.tronco = 1 # Lo incializaos en 1
        self.ramas = [] # Lista vacia


    def crecer_tronco(self):    # Suma 1 a longitud tronco
       self.tronco += 1

    def nueva_rama(self,numero_ramas = 1):  # Añade 1 a la lista por defecto
        for i in range(numero_ramas):       # Con paramentro etra en bucle y añade numero de items solicitado
            self.ramas.append(1)    


    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]  # Recorre cada elemento de self.ramas, lo llama rama, y construye una nueva lista donde suma 1 a cada elemento de la lsita.


    def quitar_rama(self, posicion):
        if posicion >= len(self.ramas) or posicion < 0:
            print("No se puede eliminar una rama que aun no existe")
        else:
            self.ramas.pop(posicion)     # QUitamos una rama de la posicion indicada

    def info_arbol(self):
        resultado = f"El arbol tiene una longitud del tronco de {self.tronco} unidades, ramas tiene {len(self.ramas)} y la longitud de estas es de {self.ramas}" # Toda la info del arbol
        return resultado

a=Arbol()

a.crecer_tronco()
a.nueva_rama()
a.crecer_ramas()
a.nueva_rama(2)
a.quitar_rama(1)
print(a.info_arbol())


# %% [markdown]
# 35. Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
# Implementar agregar_dinero para aumentar el saldo del usuario.
# Caso de uso:
#         a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#         b. Agregar 20 unidades al saldo de Bob.
#         c. Transferir 80 unidades de Bob a Alicia.
#         d. Retirar 50 unidades del saldo de Alicia.

# %%
class UsuarioBanco:                                     # Definimos clase
    def __init__(self, nombre, saldo, cuenta):          # Creamos contructor
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = cuenta
        
    def retirar_dinero (self, extraer = 0):             # Funcion de retirada con paramentro por defecto    
        if extraer > self.saldo:                        # Si el saldo a extraer es superior al saldo en cuenta
            raise ValueError('Saldo insuficiente')      # Salta excepcion
        else:
            self.saldo = self.saldo - extraer           # Si todo esta bien, restamos saldo


    def transferir_dinero (self, cantidad, usuarioA):   # Funcion de traspaso de dinero. Introducir cantidad y al usuario al que transferir
        self.retirar_dinero(cantidad)                   # Retiramos dinero al usuario que transfiere
        usuarioA.agregar_dinero(cantidad)               # Ingresamos dinero al usuario que recibe

    def agregar_dinero (self, agregar = 0):             # Funcion de ingreso con paramentro por defecto    
        self.saldo = self.saldo + agregar               

Alicia = UsuarioBanco ("Alicia", 100, True)             # Creamos los usuarios
Bob = UsuarioBanco ("Bob", 50, True)

print(f"Saldo inicial Bob: {Bob.saldo}")
print(f"Saldo inicial Bob: {Alicia.saldo}")

Bob.agregar_dinero(20)
Bob.transferir_dinero(80, Alicia)
Alicia.retirar_dinero(50)

print(f"Saldo final Bob: {Bob.saldo}")
print(f"Saldo final Alicia: {Alicia.saldo}")

# %% [markdown]
# 36. Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto.

# %%
frase = "hola mundo hola mundo bonito"

def contar_palabras(texto):  
    palabras = texto.split()                    # Separamos el string en paalbras
    palabras_repetidas = {}                     # Creamos diccionario vacio
    for palabra in palabras:                    # recorreomos el "split"
        if palabra in palabras_repetidas:       #¿Esta la palabra en el diccionario?
            palabras_repetidas[palabra] = palabras_repetidas[palabra]+1     # Sumamos 1 si esta ya la palabra
        else:
            palabras_repetidas[palabra] = 1     # Como no esta, le asignamos el valor de 1
    return palabras_repetidas                   # Retornamos el resultado del diccionario

def reemplazar_palabras(texto, palabra_original, palabra_nueva):    # Reemplazamos texto buscando la palabra que remplazar por la nueva palabra
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):   # Eliminamos UNA sola palabra
    return texto.replace(palabra, "", 1)


def procesar_texto(texto, opcion, *args):                   # Creamos funcion para elegir la funcion que queramos con argumentos establecidos en cada funcion
    if opcion == "contar":                                  # Contamos palabras
        return contar_palabras(texto)
        
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1]) # Reemplazamos palabras  
        
    elif opcion == "eliminar":                              # Eliminamos
        return eliminar_palabra(texto, args[0])


print(procesar_texto(frase, "contar")) # Contamos 
print(procesar_texto(frase, "reemplazar", "mundo", "universo")) # Reemplazamos 
print(procesar_texto(frase, "eliminar", "mundo")) # Eliminamos 

# %% [markdown]
# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

# %%
def momento_dia(tiempo):        # Creamos funcion
    if tiempo <= (6*60):        # Multiplicamos horas, por 60 minutos, ya que el tiempo esta en minutos. Rango de 00:00 a 06:00
        print("Es de noche")    
    elif tiempo <= (14*60):     # Rango de 06:01 a 14:00   
        print("Es de dia")
    elif tiempo <= (21*60):     # Rango de 14:01 a 21:00
        print("Es de tarde")
    elif tiempo <= (24*60)-1:   # Rango de 21:01 a 23:59
        print("Es de noche")

while True:                                                         # Creamos bucle para compprobar datos introducidos
    hora_usuario = input("Introduce la hora con formato HH:MM")     # Pedimos hora con formato a aplicar

    try:
        hora_str, minutos_str = hora_usuario.split(":")             # Separamos las horas de los minutos quitando ":"
        hora = int(hora_str)                                        # Convertimos string de horas a int
        minutos = int(minutos_str)                                  # Convertimos string de minutos a int
        
        
        if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:    # Verificamos el rango de hora
            print("El formato esta fuera de rango, introduce una hora entre las 00:00 y 23:59")
            continue
        
        tiempo_usuario = (hora * 60) + minutos                      # Convertimos el tiempo a minutos totales (minHora+min)
        break
    
    except:                                                         # Si hay error de formato en el input, mostramos mensaje
        print("Formato incorrecto, introduce HH:MM")
        continue


momento_dia(tiempo_usuario)

# %% [markdown]
# 38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
#         0 - 69: insuficiente
#         70 - 79: bien
#         80 - 89: muy bien
#         90 - 100: excelente

# %%
def comprobar_calificacion(nota):       # Creamos funcion con rangos e ifs correspondientes
    if nota <= 69:
        print("Insuficiente")
    elif nota <= 79:
        print("Bien")
    elif nota <= 89:
        print("Muy bien")
    elif nota <= 100:
        print("Excelente")
    


while True:                                                                         # Bucle infinito para validacion de datos y vovler a pedir nuevamente el input
    try:
        calificacion = int(input("Que nota obtuviste (del 0 al 100)"))              # Solicitud de input, casteado a int.

        if calificacion <= 0 or calificacion >= 100:                                # Comprobar rango de numero introducido, si fuera de rango, imprimimos mensaje (menor o igual que cero o mayor o igual que 100)
            print("La nota esta fuera de rango, introduce un numero de 0 a 100")
            continue                                                                # Vuelve al inicio del while (pide número otra vez)
        break                                                                       # Solo llega aquí si NO entró en el if, es decir, si el número está bien, eale del bucle y continúa el programa
        

    except:                                                                         # En caso de introducir formato no numerico, imprimimos error
        print("Formato incorrecto, introduce un numero del 0 al 100")
        continue                                                                    # Vuelve al inicio del while (pide número otra vez)

comprobar_calificacion(calificacion)

# %% [markdown]
# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# %%
import math                                         # Importamos modulos con funcion de PI

def calcular_area(figura, datos):                   # Definimimos funcion
    if figura == "rectangulo":                      # Cambiamos figura por "rectangulo" e intercambiamos datos de tupla 
        base = datos[0]                             # Accedemos a datos de tupla para guardar en variable de base
        altura = datos [1]                          # Accedemos a datos de tupla para guardar en variable de altura
        area_rectangulo = base * altura             # Calculamos area
        return area_rectangulo
    
    
    elif figura == "circulo":
        radio = datos[0]
        area_ciruclo = math.pi * (radio * radio)    # Utilizamos modilo math.pi y calculamos el area del ciruclo
        return area_ciruclo
    
    
    elif figura == "triangulo":
        base = datos[0]
        altura = datos [1]
        area_triangulo = base * altura / 2
        return area_triangulo

print(calcular_area("rectangulo", (5, 10) ))
print(calcular_area("circulo", (3,) )) 
print(calcular_area("triangulo", (4, 6) ))


# %% [markdown]
# 40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
#     a. Solicitar al usuario el precio original de un artículo.
#     b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#     c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#     d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
#     e. Mostrar el precio final de la compra, considerando o no el descuento.
#     f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

# %%
precio_original = int(input("¿Cuanto ha costado el producto?"))         # Solcitamos precio del poducto

def calculo_dto (precio):                                               # Definicimos funcion para palicar o no dto
    dto = input("¿Tiene cupon de descuento? (si/no))")                  # Preguntamos a usuario si tiene o no dto
    
    if dto == "si":                                                     # Si dto es "si"
        valor_descuento = int(input("¿Que valor tiene el descuento?"))  # Solicitamos valor de dto
        
        if valor_descuento > 0:                                         # Validacion de dto para que sea superior a 0
            precio_con_descuento = precio * (1- valor_descuento/100)    # Calculo del precio aplicando el dto
            return precio_con_descuento                                 # Return del precio final
        else:                                                           # Si la validacion de >0 es falsa, imprimimos mensaje error y returnamos precio original
            print("Descuento no válido")
            return precio

    elif dto == "no":                                                   # Si dto es "no"
        return precio                                                   # Returnamos el precio original sin dto

precio_final = calculo_dto(precio_original)                             # Ejecutamos funcion con el precio original del primer input
print(f"Precio final: {precio_final:.2f}€")                             # Imprimos precio final con formato de redondeo a dos decimales (: → voy a aplicar formato, .2 → 2 decimales, f → número flotante (float))



