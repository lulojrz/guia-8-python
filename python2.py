from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import Union
import random
#guia 8
#Pilas
#ejercicios 1
def generar_nros_al_azar(cant:int,desde:int,hasta:int)-> Pila[int]:
    res : Pila[int] = Pila()
    if cant and (desde <= hasta):
       for num in range(cant):
         nuevo_numero:int = random.randint(desde,hasta)  
         res.put(nuevo_numero)

    return res
 
 
 
#ejercicio 2
def cantidad_elemento(pila:Pila[int])->int:
   pila_contar = pila
   cont = 0
   
   while pila_contar.empty() == False:
      pila_contar.get()
      cont+=1
     
   return cont
      


#ejercicio 3
def maximo(x:list[int])-> int:
    if not x:
        return None
    
    maximo_enlista:int= x[0]
    for num in range(1,len(x)):
        if x[num] > maximo_enlista:
            maximo_enlista = x[num]
            
    return maximo_enlista
 
def buscar_el_maximo(pila:Pila[int])->int:
   pila_max = pila
   copia_pila = []
   while pila_max.empty()==False:
      num = pila_max.get()
      print(num)
      copia_pila.append(num)
      
   return maximo(copia_pila)
      
   
#ejercicio 4
def buscar_nota_maxima(notas: Pila[(str,int)])-> (str,int):
   pila_copia = notas
   pila_lista = []
   lista_notas = []
   while pila_copia.empty()==False:
    nota = pila_copia.get()
    pila_lista.append(nota)
    
   for estudiante in pila_lista:
      lista_notas.append(estudiante[1])

   nota_maxima = maximo(lista_notas)
   
   for estudiante in pila_lista:
      if estudiante[1] == nota_maxima:
         return estudiante
         
  
    
      
    
    
pila_notas = Pila()
pila_notas.put(("marcos",9))
pila_notas.put(("mateo",10))
pila_notas.put(("sebastian",8))

#print(buscar_nota_maxima(pila_notas))

#ejercicio 5
def esta_bien_balanceada(s:str)-> bool:
   cont_par_ini = Pila()
   cont_par_fin=Pila()
   par_ini = 0
   par_fin = 0
   for caracter in s :
      if caracter =="(":
         cont_par_ini.put("si")
      
      if caracter == ")":
         cont_par_fin.put("si")
         
   while cont_par_ini.empty() == False:
      cont_par_ini.get()
      par_ini+=1
      
   while cont_par_fin.empty() == False:
      cont_par_fin.get()
      par_fin+=1
      
   return par_fin == par_ini
      

#ejercicio 6








#ejercicio 7
pila_1 = Pila()
pila_2 = Pila()
pila_1.put(1)
pila_1.put(3)
pila_1.put(5)
pila_1.put(7)
pila_1.put(9)
#pila_1 = 1 3 5 7 9 
pila_2.put(2)
pila_2.put(4)
pila_2.put(6)
pila_2.put(8)
pila_2.put(10)
#pila_2 = 2 4 6 8 10
def intercalar(p1:Pila,p2:Pila)-> Pila:
   res = Pila()
   while p1.empty() == False  or p2.empty() == False:
      par = pila_2.get()
      res.put(par)
      impar = pila_1.get()
      res.put(impar)
      
   return res

#nueva_pila = intercalar(pila_1,pila_2)
#while nueva_pila.empty() == False:
#   print(nueva_pila.get())  
      

   
   
#COLAS
#ejercicio 8
def generar_nros_al_azar_cola(cant:int,desde:int,hasta:int)-> Cola:
   res = Cola()
   if desde <= hasta:
    for num in range(cant):
       num = random.randint(desde,hasta)
       res.put(num)
       
   return res
      
cola = generar_nros_al_azar(4,5,10)
#while cola.empty() == False:
#   print(cola.get())


#ejercicio 9
def cantidad_elementos_cola(c:Cola)->  int:
   cont = 0
   while c.empty() == False:
      cola.get()
      cont+=1
      
   return  cont

 
#ejercicio 10
def buscar_maximo(c:Cola)->  int:
   cola_hecha_arreglo = []
   if c :
      while c.empty() == False:
         num = c.get()
        # para ver los numeros de la cola print(num)
         cola_hecha_arreglo.append(num)
         
   maximo_en_cola = maximo(cola_hecha_arreglo)
   return maximo_en_cola
         
#print(buscar_maximo(cola))


#ejercicio 11
cola_notas = Cola()
cola_notas.put(("juan",8))
cola_notas.put(("sebas",5))
cola_notas.put(("pablo",3))

def minimo(x:list[int])-> int:
    if not x:
        return None
    
    minimo:int= x[0]
    for num in range(1,len(x)):
        if x[num] < minimo:
            minimo= x[num]
            
    return minimo
 


def buscar_nota_minima(c:Cola[(str,int)]) ->  (str,int):
   cola_copia = c
   cola_hecha_arreglo = []
   lista_notas = []
   while cola_copia.empty() == False:
      num = cola_copia.get()
      cola_hecha_arreglo.append(num)
      
   for estudiante in cola_hecha_arreglo:
      lista_notas.append(estudiante[1])
      
   min = minimo(lista_notas) 
   
   for estudiante in cola_hecha_arreglo:
      if estudiante[1] == min:
         
       return estudiante
      
      
#print(buscar_nota_minima(cola_notas))
 
#ejercicio 12     
cola_1 = Cola()
cola_2 = Cola()
cola_1.put(1)
cola_1.put(3)
cola_1.put(5)
cola_1.put(7)
cola_1.put(9)
cola_2.put(2)
cola_2.put(4)
cola_2.put(6)
cola_2.put(8)
cola_2.put(10)

def intercalar_colas (c1:Cola,c2:Cola)->Cola:
   cola_mixta = Cola()
   while c1.empty() == False or c2.empty() == False:
      cola_mixta.put(c1.get())
      cola_mixta.put(c2.get())
      
   return cola_mixta

      
#cola_evaluar = intercalar_colas(cola_1,cola_2)
#while cola_evaluar.empty() == False :
 #  print(cola_evaluar.get())   


#ejercicio 13
#13.1
def armar_secuencia_bingo()->Cola:
   res = Cola()
   numeros = list(range(0,100))
   while len(numeros)  > 0:
      posicion = random.randint(0,len(numeros)-1)#randint incluye extremos
      elemento= numeros.pop(posicion)
      res.put(elemento)
   
      
   return res

#cola= armar_secuencia_bingo()
#while cola.empty() == False:
 #  print(cola.get())
bolillero_cola = armar_secuencia_bingo()
 
#ejercicio 13.2
def armar_cartoncito()-> list[int]:
   carton = []
   numeros = list(range(0,100))
   for num in range(12):
      posicion= random.randint(0,99)
      if posicion in carton:
         posicion = random.randint(0,99)
      else:
       carton.append(posicion)
      
   return carton

cartoncito_cola = armar_cartoncito()

def jugar_carton_bingo(carton:list[int],bolillero: Cola)->int:
   cantidad_carton = len(carton)
   cont = 0
   while cantidad_carton>0:
      num = bolillero.get()
      cont+=1
      if num in carton:
         cantidad_carton-=1
         
   return cont
   

#ejercicio 14
cola_pacientes = Cola()
cola_pacientes.put((1,"juan","urgencias"))
cola_pacientes.put((3,"javier","cirujano"))
cola_pacientes.put((6,"pablo","urgencias"))
cola_pacientes.put((8,"marcos","odontologo"))
cola_pacientes.put((9,"mateo","pediatra"))



def pacientes_urgentes(c:Cola[(int,str,str)]) -> int:
   cola_lista = c
   cola_hecha_arreglo = []
   cont = 0
   while cola_lista.empty() == False:
      paciente = cola_lista.get()
      cola_hecha_arreglo.append(paciente)
      
   for paciente in cola_hecha_arreglo:
      if paciente[0] < 4:
         cont+=1
         
   return cont

#print(pacientes_urgentes(cola_pacientes))      
 
#ejercicio 15
     
      
#DICCIONARIOS
#EJERCICIO 16
def calcular_promedio_por_estudiante(notas:tuple[tuple[str,int]]) -> dict[str,float]:
   promedio_diccionarios:dict = {}
   suma_notas = {}
   conteo_notas = {}
   for nombre , nota in notas :
      if nombre!="" and nota in range(11):
       if nombre in suma_notas:
            suma_notas[nombre] += nota
            conteo_notas[nombre] += 1
       else:
            suma_notas[nombre] = nota
            conteo_notas[nombre] = 1
  
   for nombre in suma_notas :
         promedio_diccionarios[nombre] = suma_notas [nombre] / conteo_notas[nombre]
         
   return promedio_diccionarios



#EJERCICIO 17

      
def visitar_sitio(historiales_dict:dict[str,Pila[str]],usuario:str,sitio:str):
   if historiales_dict !="" and usuario!= "" and str!="":
      if usuario in historiales_dict:
        historiales_dict[usuario].put(sitio)
      else:
         historiales[usuario] = Pila()
         historiales[usuario].put(sitio)
         
         
def navegar_atras(historiales_dict:dict[str,Pila[str]],usuario:str)->str:
   sitio = ""
   if usuario in historiales_dict:
      sitio= historiales_dict[usuario].get()
        
   return sitio

         
#EJERCICIO 18
def agregar_producto(diccionario : dict[str, dict[Union[int, float]]],producto:str,precio:float,cantidad:float):
   if precio>= 0 and cantidad >=0 and producto!="":
      if producto not in diccionario:
         diccionario[producto]={
            "Cantidad":cantidad,
            "Precio":precio
         }
   

def actualizar_stock(diccionario:dict[str,dict[Union[int,float]]],nombre:str,cantidad:float):
   if cantidad >=0 and nombre!="" and  nombre in diccionario:
      diccionario[nombre]["Cantidad"]=cantidad
      
      
def actualizar_precio(diccionario:dict[str,dict[Union[int,float]]],nombre:str,precio:float):
   if precio >=0 and nombre!="" and  nombre in diccionario:
      diccionario[nombre]["Precio"]= precio
     
def calcular_inventario(diccionario:dict[str,dict[Union[int,float]]])-> float:
   cont = 0
   for producto in diccionario.values():
      cont+=producto["Cantidad"] * producto["Precio"]
      
   return cont

#EJERCICIO 19
#MANEJO DE ARCHIVOS
def contar_lineas(archivo:str)->int:
   cont = 0
   if archivo :
      archivo = open(archivo,"r")
      lista = archivo.readlines()
      archivo.close()
      cont = len(lista)
      
   return cont

def existe_palabra(archivo:str, palabra:str)->bool:
   afirmacion = False
   if archivo :
      archivo = open(archivo,"r")
      lista=archivo.readlines()
      archivo.close()
      if palabra in lista:
         afirmacion= True
         
   return afirmacion     

def cantidad_de_apariciones(archivo:str,palabra:str)->int:
   cont = 0
   if archivo and palabra:
      archivo=open(archivo,"r")
      lista = archivo.readlines()
      archivo.close()
      for linea in lista:
         if palabra in linea:
            cont+=1
            
            
   return cont


#EJERCICIO 20
#EJERCICIO 21
#EJERCICIO 24
