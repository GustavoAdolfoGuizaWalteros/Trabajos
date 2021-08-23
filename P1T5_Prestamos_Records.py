# -*- coding: utf-8 -*-
"""P1T5.1_Prestamos_Records.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/GustavoAdolfoGuizaWalteros/Deep-Learning-1/blob/main/Trabajos/P1T5_1_Prestamos_Records.ipynb

#**Prestamos_records.csv**

---

#**TABLA GENERAL**
"""

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")
df.head(10) #Cambia cuantas filas se visualiza

"""#**Filtros**

#Record Creation date

##Filtrar por Dia, mes y año
"""

import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

#print(type(df.RECORD_CREATION_DATE))#Saber el tipo de la tabla
#print(df.RECORD_CREATION_DATE)#Tipo de Epoch timestamps
#print((dict(df.RECORD_CREATION_DATE).values()))#Mostrar en modo diccionario los valores
#print(list(df.RECORD_CREATION_DATE))#Mostrar en lista las fechas

#Mucha documentacion leida y no sirvio nada de lo que probe :(

"""#MONTO DEL PRESTAMO

##Ver y contar cantidades de prestamo en un rango determinado
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

dictMontoPres = dict(df.value_counts("MONTO_DEL_PRESTAMO"))

for i in range(len(dictMontoPres)):
  print(f"",list(dictMontoPres.values())[i],"Personas han pedido un prestamo de:",list(dictMontoPres.keys())[i])

"""##Graficar lo anterior (Grafico de pila sin estar apilado)"""

fig, ax = plt.subplots()
ax.stackplot(list(dictMontoPres.values()), list(dictMontoPres.keys()))
ax.set_title('Monto del prestamo')
ax.set_xlabel('Cantidad de personas')
ax.set_ylabel('Cantidad de dinero')

plt.show()

"""#RANGO DEL CREDITO

##Ver, filtrar y contar los rangos existentes
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

dictRanCred = dict(df.value_counts("RANGO_DEL_CREDITO"))

for i in range(len(dictRanCred)):
  print(f"En el rango de credito",list(dictRanCred.keys())[i],"hay",list(dictRanCred.values())[i],"prestamos")

for j in range(len(df.RANGO_DEL_CREDITO)):
  if type(list(dictRanCred.keys())[i]) is float:
    list(dictRanCred.keys())[i] = "0" #Cambia todos los Null a String

print(f"Cantidad de prestamos activos:",sum(dictRanCred.values())) #Los prestamos activos en total
print(f"Datos Nulos:",len(df.RANGO_DEL_CREDITO) - sum(dictRanCred.values())) #Cuenta la cantidad de datos Nulos

"""##Graficar lo anterior(Grafico de barras lateral)"""

plt.rcdefaults()
fig, ax = plt.subplots()

rangos = (list(dictRanCred.keys()))
rangosTam = np.arange(len(rangos))
cantidad = (list(dictRanCred.values())) 

ax.barh(rangosTam, cantidad, align='center')
ax.set_yticks(rangosTam)
ax.set_yticklabels(rangos)
ax.set_xlabel('Cantidad')
ax.set_ylabel('Rangos')
ax.set_title('Rango Del Credito')

plt.show()

"""#DEUDA EXISTENTE(CODIGO Y GRAFICO)

##Ver, filtrar y contar los rangos existentes
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

dictDeudaEx = dict(df.value_counts("DEUDA_EXISTENTE"))

for i in range(len(dictDeudaEx)):
  print(f"En el rango",list(dictDeudaEx.keys())[i],"Hay un total de",list(dictDeudaEx.values())[i],"prestamos con deudas.")

for j in range(len(df.DEUDA_EXISTENTE)):
  if type(list(dictDeudaEx.keys())[i]) is float:
    list(dictDeudaEx.keys())[i] = "0" #Cambia todos los Null a String

print(f"Cantidad de prestamos con deudas activos:",sum(dictDeudaEx.values())) #Los prestamos activos en total
print(f"Datos Nulos:",len(df.DEUDA_EXISTENTE) - sum(dictDeudaEx.values())) #Cuenta la cantidad de datos Nulos

"""##Graficar lo anterior(Grafico de barras lateral)"""

plt.rcdefaults()
fig, ax = plt.subplots()

rangos = (list(dictDeudaEx.keys()))
rangosTam = np.arange(len(rangos))
cantidad = (list(dictDeudaEx.values())) 

ax.barh(rangosTam, cantidad, align='center')
ax.set_yticks(rangosTam)
ax.set_yticklabels(rangos)
ax.set_xlabel('Cantidad')
ax.set_ylabel('Rangos')
ax.set_title('Prestamos Activos')

plt.show()

"""#Notas del agente(Codigo y Grafico)

##Filtrar valores NULL, rellenarlos y comparar los valores nulos con los llenos
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

listNotasAg = list(df.NOTAS_DEL_AGENTE)#Lo convierto en lista para manejarlo mas facil
countNormal, countNull = 0, 0

for i in range(len(listNotasAg)):
  if type(listNotasAg[i]) is str:#Filtra los que tienen valores String
    countNormal += 1
  else: #Por alguna razon que desconzco el Null/None es Float xD y solo por eso se puede filtrar
    countNull += 1
    listNotasAg[i] = "No existe informacion dada por el agente."#Cambia los Null por un String

totalDatos=countNormal+countNull
print(f"La cantidad de datos no nulos es:",countNormal,"\nY La cantidad de datos nulos es:",countNull)#Esto es lo de comprar valores nulos con los llenos
print(f"La suma de todos los datos es:",totalDatos)
print(f"Cantidad de datos Null rellenados:",listNotasAg.count("No existe informacion dada por el agente."))#Cuenta cuantos datos se cambiaron de Null a String

"""##Graficar cantidad de datos Null a comparacion con los String (Grafico de barras)"""

names = ["Datos String", "Datos Null"]
values = [countNormal, countNull] #Se ingresa los valores de cada variable

#plt.figure(figsize=(3, 3)) #Tamaño de la imagen para imprimir

plt.bar(names, values)
plt.suptitle("Cantidad de datos Null a comparacion con los String")
plt.show()

"""#Ubicacion de la oficina (Codigo y Grafico)

##Filtrar, hacer porcentajes y decir donde hay mas prestamos
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

nomU = list(set(list(df.UBICACION_DE_LA_OFICINA))) #Saque los datos y lo reduje para que no se repitieran

for i in range(len(nomU)): #Ya no seran 8000 datos para mirar si no solo 6    
  countNomU = df[df['UBICACION_DE_LA_OFICINA'] == nomU[i]]
  print(f"La oficina de",nomU[i],"tiene",len(countNomU.axes[0]),
          "prestamos realizados, que equivale al",(len(countNomU.axes[0]) / len(df.UBICACION_DE_LA_OFICINA))*100,"% a nivel nacional.") #Se hacen las operaciones y se escribe en orden

dictNomU = dict(df.value_counts("UBICACION_DE_LA_OFICINA"))#Convertimos en diccionario
maxDictNomU = max(dictNomU,key=lambda key: dictNomU[key])#Dentro del diccionario buscamos el valor mas alto

print(f"\n La mayor cantidad de prestamos es",max(df.value_counts("UBICACION_DE_LA_OFICINA")),"de",maxDictNomU)#Se agregan los resultados
print(f"\n",df.value_counts("UBICACION_DE_LA_OFICINA"),f"\n") #Aca comprobamos que de verdad se pusieron los datos correctos

"""##Graficar el proceso anterior (Grafico Circular)"""

labels = list(dictNomU.keys())#Los nombres
sizes = list(dictNomU.values())#Los valores
explode = (0.1, 0, 0, 0, 0, 0)#Para decidir cual valor va a destacar

fig1, ax1 = plt.subplots() #Para generar el grafico
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=45)
ax1.axis('equal')

plt.show()

"""#Prestamo Incumplido (Codigo y Grafico)

##Filtrar y contar (Codigo)
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/prestamos_records.csv")

countF = df[df['PRESTAMO_INCUMPLIDO'] == "FALSO"] #Cuenta cuantos Falso hay en la tabla
print(f"Cantidad de gente que no cumple: ",len(countF.axes[0])) #Saca el numero exacto

countV = df[df['PRESTAMO_INCUMPLIDO'] == "VERDADERO"] #Cuenta cuantos Verdadero hay en la tabla
print(f"Cantidad de gente que cumple: ",len(countV.axes[0])) #Saca el numero exacto

print(f"Total para comprobar que tomo todos los datos de la tabla: ",len(countV)+len(countF)) #Suma para comprobar que sume 8000

"""##Filtrar, contar y graficar (Grafico de barras)"""

names = ["Verdadero", "Falso"]
values = [len(countV.axes[0]), len(countF.axes[0])] #Se ingresa los valores de cada variable

plt.figure(figsize=(3, 3)) #Tamaño de la imagen para imprimir

plt.bar(names, values)
plt.suptitle("Prestamo Incumplido")
plt.show()