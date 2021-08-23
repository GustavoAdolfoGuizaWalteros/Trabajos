# -*- coding: utf-8 -*-
"""P1T5.1_user_timestamp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/GustavoAdolfoGuizaWalteros/Deep-Learning-1/blob/main/Trabajos/P1T5_2_user_timestamp.ipynb

#user_timestamp

---

#Tabla General
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/user_timestamp.csv")
df.head(10)

"""##Analisis de datos"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/user_timestamp.csv")

#Analisis de user_id
listadoGeneral = list(df.user_id)
print(type(listadoGeneral[71995]))#Los Null son Float y los valores tambien
print(df.user_id)#Datos en General:71996
print(sum(dict(df.value_counts("user_id")).values()))#Total de valores que no son Null: 61582

#Analisis de timestamp
listadoGeneral = list(df.timestamp)
print(type(listadoGeneral[71995]))#Los Null son Float
print(df.timestamp)#Datos en General:71996
print(sum(dict(df.value_counts("user_id")).values()))#Total de valores que no son Null: 61582

"""#Filtros

##Usuario mas recuente vs menos frecuente
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/user_timestamp.csv")

#El User #1 Con mas entrads al sistema
dictUserId = dict(df.value_counts("user_id"))
print(f"La mayor cantidad de entradas al sistema es del User:",list(dictUserId)[0],"Con un total de",max(dictUserId.values()),"entradas al sistema")
#Se puede cambiar el Max() por min para saber el que menos tiene y el [-1] para el ultimo
print(f"La mayor cantidad de entradas al sistema es del User:",list(dictUserId)[-1],"Con un total de",min(dictUserId.values()),"entradas al sistema")

"""##Usuario mas recuente vs menos frecuente (Grafico de barras)"""

names = str(list(dictUserId)[0]), str(list(dictUserId)[-1])
values = max(dictUserId.values()), min(dictUserId.values()) #Se ingresa los valores de cada variable

#plt.figure(figsize=(3, 3)) #Tamaño de la imagen para imprimir

plt.bar(names, values)
plt.suptitle("Usuario mas recuente vs menos frecuente")
plt.show()

"""##Frecuencia de tiempos"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/luisFernandoCastellanosG/Machine_learning/master/DataScience/DataSet's/user_timestamp.csv")

dictUserId = dict(df.value_counts("user_id"))
dictTime = dict(df.value_counts("timestamp"))

df_userMax = df[df["user_id"]==list(dictUserId)[0]]
print(df_userMax)

dictdf_userMax = dict(df_userMax.timestamp)
listdictdf_userMax = list(dictdf_userMax.values())

dictdf_userMax2 = dict(df_userMax.user_id)
listdictdf_userMax2 = list(dictdf_userMax2.values())

print(f"Tiempos",listdictdf_userMax)
print(f"Usuario",listdictdf_userMax2)

for i in range(len(listdictdf_userMax)):
  newTimeString = float(listdictdf_userMax[i].replace(":",""))/10000
print(newTimeString)

"""##Frecuencia de tiempos (Grafico)"""

for i in range(100):

  plt.plot([listdictdf_userMax2[i]], [listdictdf_userMax[i]])
plt.show()