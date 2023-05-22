
# 1.   Dos motos viajan a diferentes velocidades (**vel1** y **vel2**) y están distanciados por una distancia **dis**. La moto que se encuentra detrás lleva una velocidad mayor que la primera. Se pide realizar un script en python que solicite al usuario la distancia entre las motos en km y las velocidades de las mismas y con ello devolver en cuanto tiempo la moto 2 alcanzará a la moto 1.
def ejer1():
  #Imports
  #Variables
  Vel1 = int(input('¿Cual es la velocidad de la primera moto?'))
  Vel2 = int(input('¿Cual es la velocidad de la segunda moto?'))
  if  Vel1 >= Vel2: #Se comprueba si las velocidades estan bien
    print("La Moto dos nunca va a alcanzar a la primera")
    return
  Dis = int(input('¿Cual es la distancia entre las dos?'))  #Se pide la distancia entre las motos
  if Dis <= 0:  #Se comprueba si la distancia es correcta
    print("La Moto dos ua ha alcanzado a la primera")
    return
  Time = Dis/(Vel2-Vel1) #Se calcula
  print('Si la velocidad de la moto 1 es de ',Vel1,'Km/h, la de la moto 2 es ',Vel2,'Km/h, y tienen una distancia de ',Dis,'Km.Tardaran ',Time,'h en encontrarse')


# 2. El tutor de 2º ASIR esta organizando un viaje a Granada, y requiere determinar cuánto debe cobrar a cada alumne y cuánto debe pagar a la agencia de viajes. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la guagua es de 4000 euros, sin importar el número de alumnos. Realice un script que permita determinar el pago a la compañía de guaguas y lo que debe pagar cada alumno por el viaje."""
def ejer2():
  NumAlum = int(input('Numero de Alumnado que vendran : ')) #Se pregunta el numero de alumnos
  if NumAlum >= 100:  # Se mira cuanto costara segun los alumnos que vienen
    Cost = 65
  elif NumAlum >= 50 and NumAlum <= 99:
    Cost = 70
  elif NumAlum >= 30 and NumAlum <= 49:
    Cost = 95
  else:
    Cost = int(4000/NumAlum)  #Se divide y se redondea con un int
  print('Cada alumno tendra que pagar',Cost,'euros')


# 3. Crea un script que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo).  El programa termina cuando se acierta el número (además te dice en cuantos  intentos lo has acertado), si se llega al limite de intentos te muestra el  número que había generado."""
def ejer3():
  #Imports
  from random import randrange
  #Variables
  NumRan = randrange(1,100)
  #print(NumRan) # esto de la izquierda se descomenta para ver si funciona o no
  print('')
  print('Danos un numero')
  for i in range(0,10):  #Se usa un bucle para que lo pueda intentar varias veces
    Option = int(input())
    if Option == NumRan:
      print('Correcto')
      break
    elif Option > NumRan: 
      print('Te quedan',9-i,'intentos')
      print('El numero aleatorio es mas pequeño que tu numero')
    else:
      print('Te quedan',9-i,'intentos')
      print('El numero aleatorio es mas grande que tu numero')
    if i == 9:
      print('')
      print('Se te han acabado los intentos')


# 4. Realizar un script que pida una String por teclado que contenga espacios y devuelva el número de palabrás que contenga"""
def ejer4():
  Texto = str(input("Danos un texto : "))
  Texto = Texto.strip()
  print("La frase tiene",Texto.count(" ")+1,"palabras")


# 5. Realiza un script que se le pasen 5 notas de un alumno por teclado (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
def ejer5():
  # Variables
  Notas = []
  # CanNotas = int(input('Diga la cantidad de notas que vamos a agregar :  ')) # Esto se descomenta para que la cantidad de notas la eliga el usuario
  CanNotas = 5  # Esto se comenta si se va a descomentar lo de ariba
  NotasMed = 0  # Variable vacia que usaremos luego
  for i in range(CanNotas): 
    Notas.append((float(input(f"Nota {i+1} º "))))
    if Notas[i] < 0:  #Compruebo que el numero es mayor que 0
      print('El valor no puede ser menor de 0')
      break
    elif Notas[i] > 10: #Compruebo que el numero es menor que 10
      print('El valor no puede ser mayor de 10')
      break
    else:
      NotasMed += Notas[i]
  # Lo ordeno para que el 0 sea el numero mas bajo y el 5 sea el numero mas alto
  Notas.sort()
  # Resultados
  print('')
  print('----Resultados----')
  print('La media es',NotasMed/CanNotas)
  print('La Nota Min es',Notas[0])
  print('La Nota Max es ',Notas[len(Notas)-1])


#6. Realizar un script que cree una una tabla bidimensional de 5x5 y nombre 'diagonal'. La Componentes de la tabla en su diagonales deben de ser 1 y el resto 0. Se ha de mostrar el contenido de la tabla por pantalla."""
def ejer6():
# Variables
  diagonal = []
  filas = 5
  columnas = 5
  # Crea una matrix 5x5 llena de 0
  for i in range(filas):
    diagonal.append([0]*columnas)
  for i in range(filas):
    for j in range(columnas):
      diagonal[i][j]=0
      if i == j: # Agregamos 1 si la i es igual que la j es decir en las diagonales
        diagonal[i][j]=1
      elif (i+j) == 4: # Agregamos 1 si la i mas las j es 4(4 por que empiza en 0) para hacer la diagonal inversa
        diagonal[i][j]=1
  print("Resultado")
  for fila in diagonal:   # Imprimimos el resultado
    for valor in fila:
      print(valor,end= " ")
    print()


# 7. Crea un script que pida un número y cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
def ejer7():
  # Variables
  diccionario = {}
  Num = int(input("Numero a calcular: "))
  # Bucle encargado de realizar el numero cuadrado
  for i in range(1, Num + 1):
    diccionario[i] = i * i
  print(diccionario)


# 8. Crea un script de una agenda en la que se guardan nombres y números de teléfono. En la agenda existirá un menú con las siguientes opciones: 
#  * **Añadir/modificar**: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
#  * **Buscar**: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#  * **Borrar**: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#  * **Listar**: Nos muestra todos los contactos de la agenda.
#   Implementar el script con un diccionario.
def ejer8():
# Variable
  agenda = {}
  # Menu
  def menu():
    print('Elija lo que vamos a hacer')
    print(' 1.- Añadir')
    print(' 2.- Buscar')
    print(' 3.- Borrar')
    print(' 4.- Listar')
    print(' 5.- Salir')
    MenuNum = int(input('Que desea hacer: '))
    while MenuNum < 0 or MenuNum > 5 :
      print(MenuNum ,' no tenemos esa opcion')
      MenuNum = int(input('Por favor elija la opcion : '))
    if MenuNum == 1:
      nombre = input("Nombre: ")
      telefono = int(input("Telefono: "))
      anadir(nombre,telefono)   # Llamamos a esta funcion para que se realice la accion
      repeat = input('¿Quieres salir? (s/n)')
      if repeat.lower() == 'n' or repeat.lower() == 'no':
        menu()
      else : return
    elif MenuNum == 2:
      nombre = input("Introduzca una cadena de caracteres: ")
      buscar(nombre)   # Llamamos a esta funcion para que se realice la accion
      repeat = input('¿Quieres salir? (s/n)')
      if repeat.lower() == 'n' or repeat.lower() == 'no':
        menu()
      else : return
    elif MenuNum == 3:
      nombre = input("Introduzca un nombre: ")
      borrar(nombre)   # Llamamos a esta funcion para que se realice la accion
      repeat = input('¿Quieres salir? (s/n)')
      if repeat.lower() == 'n' or repeat.lower() == 'no':
        menu()
      else : return
    elif MenuNum == 4:
      listar()

  def anadir(nombre,telefono):
      if nombre in agenda.keys():
        print(f"Ese nombre ya existe, su telefono es {agenda[nombre]}")
        opcion2 = input(f"Desea el cambiar el número de {nombre} presione Y/N: ")
        if opcion2.lower == "y" or opcion2.lower == "s":
          agenda[nombre] = input("Introduzca un nuevo número: ")
        else:
          opcion2 = input(f"Desea cambiar el nombre de {nombre} presione Y/N: ")
          if opcion2.lower == "y" or opcion2.lower == "s":
            print(f"Para hacer eso borre al usuario {nombre} y creelo de nuevo")
        print(f"El teléfono del usuario {nombre} no ha sido alterado")
        print(agenda)
      else:
        agenda[nombre] = telefono
        print(f"Se ha añadido correctamente el contacto: {nombre}")
        print(agenda)

  def buscar(caracter):
    for clave in agenda.keys():
      empiezaCon = clave.startswith(caracter)
      if empiezaCon == True:
          print("Encontramos los siguientes contactos con nombre: " + clave + " y número: " + agenda[clave])
      else:
          print("No se ha encontrado ningún contacto con ese nombre")

  def borrar(nombre):
    if nombre in agenda.keys():
      opcion2 = input(f"El nombre existe en los registros {nombre} desea eliminarlo Y/N: ")
      if opcion2 == "Y" or opcion2 == "y":
        agenda.pop(nombre)
        print(f"Se ha eliminado al contacto: {nombre}")
        print(agenda)
      else:
        print(f"El {nombre} usuario no ha sido eliminado")
        print(agenda)

  def listar():
    print(agenda)

  menu()

# 9. Crear un script que al introducir una fecha nos diga a que día juliano corresponde. El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero.Para ello debes de hacer las siguientes funciones:
#  * **LeerFecha**: Lee por teclado el día, mes y el año.
#  * **DiasDelMes**: Recibe un mes y un año y devuelve el número de días
#  * **EsBisiesto**: Recibido un año nos dice si es bisiesto o no.
#  * **Calcular_Dia_Juliano**: Recibe una fecha y nos devuelve el día juliano.
def ejer9():
  # Imports
  from datetime import datetime
  # Variables
  dia = int(input('Dia: '))
  while dia < 1 or dia > 31:  # Bucle para asegurarnos que el dia exista
    dia = int(input('Introduce un dia correcto: '))
  mes = int(input('Mes: '))
  while mes < 1 or mes > 12:  # Bucle para asegurarnos que el mes existe
    mes = int(input('Introduce un mes que exista: '))
  anyo = int(input('Año: '))

  def bisiesto(anyo):
    if anyo % 4 == 0 or (anyo % 100 == 0 and anyo % 400 == 0): # If para ver si el año es bisiteto o no
      bisiesto = True
      return bisiesto
    else:
      bisiesto = False
      return bisiesto

  def diames(mes, anyo):   # Funcion para ver los dias que tienen los  meses
    if mes == 1 or mes == 3 or mes == 5 or mes == 8 or mes == 10 or mes == 12:
      return 31
    elif mes == 2:
      if bisiesto(anyo):
        return 29
      else:
        return 28
    else: 
      return 30
    
  def juliano(dia, mes,anyo):  # Calculo del año juliano
    day = 0
    while mes > 1:
      mes -= 1
      if mes == 1 or mes == 3 or mes == 5 or mes == 8 or mes == 10 or mes == 12:
        day += 31
      elif mes == 2:
        if bisiesto(anyo):
          day += 29
        else:
          day += 28
      else: 
        day += 30
    day += dia
    return day
  
  # Resultados
  print('')
  print('----Resultados----')
  print('')
  print('Fecha: ',dia,"/",mes)
  print('Cuantos dias tiene ese mes', diames(mes, anyo))
  print('¿Es bisiesto ?', bisiesto(anyo))
  print('Día Juliano:', juliano(dia, mes, anyo))


# 10. Función CalcularMCD: Recibe dos números y devuelve el MCD utilizando el método de Euclides. 
# El método de Euclides es el siguiente:
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
def ejer10():
  # Imports
  import sys
  # Variables
  Num1 = float(input('Primer numero: '))
  Num2 = float(input('Segundo numero: '))
  def calcular(Num1,Num2):
    if Num1 > Num2:   # Ordeno los numeros
      MinNum = Num2
      MaxNum = Num1
    else:
      MinNum = Num1
      MaxNum = Num2
    if MinNum  == 0:  # Compruebo que el numero mas pequeño no sea 0
      sys.exit('Un numero entre 0 es infinito')
    while MaxNum%MinNum != 0: #Calculo el MCD
      Rest = MaxNum%MinNum
      MaxNum = MinNum
      MinNum = Rest
    print('El MCD es ',MinNum)
  calcular(Num1,Num2)

def menu():
    print('Elija el script que vas a usar')
    print(' 1.-Motos')
    print(' 2.-Agencia')
    print(' 3.-Adivinar')
    print(' 4.-Contador')
    print(' 5.-Notas')
    print(' 6.-Matrix')
    print(' 7.-Diccionario')
    print(' 8.-Agenda')
    print(' 9.-Dia Juliano')
    print(' 10.-Euclides')
    MenuNum = int(input('Numero del script : '))
    if MenuNum == 1:
      ejer1()
      menu()
    elif MenuNum == 2:
      ejer2()
      menu()
    elif MenuNum == 3:
      ejer3()
      menu()
    elif MenuNum == 4:
      ejer4()
      menu()
    elif MenuNum == 5:
      ejer5()
      menu()
    elif MenuNum == 6:
      ejer6()
      menu()
    elif MenuNum == 7:
      ejer7()
      menu()
    elif MenuNum == 8:
      ejer8()
      menu()
    elif MenuNum == 9:
      ejer9()
      menu()
    elif MenuNum == 10:
      ejer10()
      menu()
    else:
      print('Ese script no se encuentra')
      menu()

menu()