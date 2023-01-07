### CALCULAR NÚMEROS PRIMOS

numero=int (input ("introduce un numero:"))

def esPrimo (numero):
    numero=abs(numero)
if numero==0 or numero==1 or numero==2:
    print (f"el {numero} es primo")
    exit()
primo=True
if numero%2==0:
    print(f"no es primo")
    exit()
for i in range (2,numero,2):
    if numero%i==0:
        primo=False
if primo==True:
    print(f"es primo")
else:
    print(f"no es primo")

esPrimo(numero)

### MENÚ DE OPCIONES CALCULO DE SUPERFICIES

from cmath import pi

def menu():
    print ("______MENU______")
    print()
    print ("1. 📌Superficie del CUADRADO")
    print ("2. 📌Superficie del RECTÁNGULO")
    print ("3. 📌Superficie del TRAPECIO")
    print ("4. 📌Superficie del TRIÁNGULO")
    print ("5. 📌Superficie del CÍRCULO")
    print ("6. 📌Superficie del ROMBOIDE")
    print ("7. 📌No calcular nada y salir")
    print()

def supcuad():
    lado=float(input("Introduce el lado del cuadrado: "))
    areacua=lado**2
    print(f"La superficie de tu cuadrado es {areacua}")

def suprect():
    ancho=float(input("Introduce el ancho del rectangulo: "))
    alto=float(input("Introduce el alto del rectangulo: "))
    arearect=ancho*alto
    print(f"La superficie de tu rectangulo es {arearect}")

def suptrap():
    base1=float(input("Introduce la 1ºbase del trapecio: "))
    base2=float(input("Introduce la 2ºbase del trapecio: "))
    altura=float(input("Introduce la altura del trapecio: "))
    areatrap=((base1+base2)*altura)/2
    print(f"La superficie de tu rectangulo es {areatrap}")

def suptrian():
    base=float(input("Introduce la base del triángulo: "))
    altura=float(input("Introduce la altura del triángulo: "))
    areatrian=(base*altura)/2
    print(f"La superficie de tu rectangulo es {areatrian}")

def supcir():
    radio=float(input("Introduce el radio del circulo: "))
    areacir=pi*radio**2
    print(f"La superficie de tu rectangulo es {areacir}")

def supromb():
    base=float(input("Introduce la base del romboide: "))
    altura=float(input("Introduce la altura del romboide: "))
    arearomb=base*altura
    print(f"La superficie de tu rectangulo es {arearomb}")


##FUNCION DATOS PERSONAS

def IntroducirPersonas(ListaPersonas):
    continuar=""

    while continuar!="N":
        persona=[]
        persona.append( input ("introduce dni: ").upper())
        persona.append( input ("introduce nombre: ").capitalize)
        persona.append( input ("introuce apellido: ").capitalize)
        persona.append( int (input ("introduce edad: ")))

        ListaPersonas.append(persona)
        print (ListaPersonas)

continuar=input ("quieres introducir mas personas: S/N:" )
continuar= continuar.upper()

def VerNombres(ListaPersonas):
    for indice, persona in enumerate(ListaPersonas):
        print(f"/***Dato Persona {indice+1}****/")
        print (f"DNI: {persona^[0]}")
        print()

def BorrarPersona (ListaPersonas):
    nombre= input ("Introduce un nombre a borrar: ").capitalize()
    
    if nombre in ListaPersonas:    
        ListaPersonas.remove (nombre)
        print (f"{nombre} se ha borrado correctamente")
    else:
        print (f"{nombre} no está en nuestra lista")

def BuscarPersona (ListaPersonas):
    nombre= input ("Introduce un nombre a borrar: ").capitalize()
    if nombre in ListaPersonas:    
        print (f"{nombre} sí está")
    else:
        print (f"{nombre} no está en nuestra lista")



def ImprimirMenu():
    print ("/***** MENU *****/")
    print ("1) Introducir Nuevo Nombre")
    print ("2) Ver los nombres")
    print ("3) Borrar un nombre")
    print ("4) Buscar Nombre")
    print ("5) Salir")


