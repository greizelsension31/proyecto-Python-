#!/usr/bin/env python
# coding: utf-8

# Obtenga la fecha en la que se ejecuta el script Para ambos archivos:
# Cree un DataFrame para cada escuela, con el formato de nombre “nombrecolegio_curso” que reúna los datos de las columnas: school, sex, age, address, Pstatus, guardian, traveltime, studytime, failures, paid, internet, health, absences, G1,G2,G3

# # DATAFRAME COMPLETA UNIDA PARA AMBOS CSV STUDENT_POR Y STUDENT_ MAT

# In[20]:


import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

Fecha = datetime.datetime.now()
print("La fecha en la que se ejecuta este script es:")
print(Fecha.strftime('%d/%m/%Y %H:%M:%S'))
 # leyendo el csv y concatenado los documentos 


datos1_semicoma=pd.read_csv(r'C:\Users\Lenovo 11 e\Desktop\SIC_GREIZEL_CURSO\student-por.csv',sep =";")


datos1_coma = datos1_semicoma.replace(to_replace=';', value=',', regex=True)
df1_concat= pd.concat([datos1_coma, datos1_semicoma ])
# haciendo copia

datos1= pd.DataFrame(df1_concat)

 # leyendo el csv y concatenado los documentos student mat 

datos2_semicoma=pd.read_csv(r'C:\Users\Lenovo 11 e\Desktop\SIC_GREIZEL_CURSO\student-mat.csv',sep =";")
datos2_coma = datos2_semicoma.replace(to_replace=';', value=',', regex=True)
# haciendo copia 

df2_concat= pd.concat([datos2_coma, datos2_semicoma])
datos2= pd.DataFrame(df2_concat)

# impriendo dataframe de los dos datos 
pd.DataFrame(datos1)
pd.DataFrame(datos2)


# # 1. Data Frame de la Escuela Mousinho da Silveira para matematicas

# 2.Cree un DataFrame para cada escuela, con el formato de nombre “nombrecolegio_curso” que reúna los datos de las columnas: school, sex, age, address, Pstatus, guardian, traveltime, studytime, failures, paid, internet, health, absences, G1,G2,G3

# In[21]:


import pandas as pd
import datetime

# Create a dataframe
MS_mat=datos2.loc[(datos2['school']=='MS')][['school', 'sex','age', 'address', 'Pstatus', 'guardian', 'traveltime','studytime', 'failures','paid', 'internet', 'health', 'absences', 'G1','G2','G3']]
Fecha = datetime.datetime.now()
print("La fecha en la que se ejecuta este script es:")
print(Fecha.strftime('%d/%m/%Y %H:%M:%S'))
pd.DataFrame(MS_mat)


# # 1. 1Data Frame de escuela Gabriel pereira de matematicas

# In[22]:


import pandas as pd
#creando el dataframe
GP_mat=datos2.loc[(datos2['school']=='GP')][['school', 'sex','age', 'address', 'Pstatus', 'guardian', 'traveltime','studytime', 'failures','paid', 'internet', 'health', 'absences', 'G1','G2','G3']]
Fecha = datetime.datetime.now()
print("La fecha en la que se ejecuta este script es:")
print(Fecha.strftime('%d/%m/%Y %H:%M:%S'))
pd.DataFrame(GP_mat)


# # 1.2 DATRAFRAME DE ESCUELA MS -Mousinho da Silveira de portugues

# In[23]:


import pandas as pd
Fecha = datetime.datetime.now()
print("La fecha en la que se ejecuta este script es:")
print(Fecha.strftime('%d/%m/%Y %H:%M:%S'))

MS_por=datos1.loc[(datos1['school']=='MS')][['school', 'sex','age', 'address', 'Pstatus', 'guardian', 'traveltime','studytime', 'failures','paid', 'internet', 'health', 'absences', 'G1','G2','G3']]
pd.DataFrame(MS_por)


# # 1. 3 DATRAFRAME DE ESCUELA GP - Gabriel Pereira de portugues

# In[24]:



Fecha = datetime.datetime.now()
print("La fecha en la que se ejecuta este script es:")
print(Fecha.strftime('%d/%m/%Y %H:%M:%S'))

GP_por=datos1.loc[(datos1['school']=='GP')][['school', 'sex','age', 'address', 'Pstatus', 'guardian', 'traveltime','studytime', 'failures','paid', 'internet', 'health', 'absences', 'G1','G2','G3']]
pd.DataFrame(GP_por)


# # union de data en una sola data de los estudiantes de matematicas y portugues de la escuela MS

# In[25]:


import pandas as pd

Data_student_MS = pd.concat([MS_mat, MS_por])
Data_student_MS


# # UNION DE DATA EN UN SOLO DATAFRAME DE LA ESCUELA GP

# In[26]:


import pandas as pd

Data_student_GP = pd.concat([GP_mat, GP_por])
Data_student_GP


# # 2. 0 Verifique que no haya data de valor nulo (NaN), en caso de encontrar algún valor NaN se deberá eliminar toda la fila

# # verificacion de data de valor nulo para el csv student portugues

# In[27]:


import pandas as pd
import numpy as np
datapor=pd.read_csv(r'C:\Users\Lenovo 11 e\Desktop\SIC_GREIZEL_CURSO\student-por.csv',sep =";")

pd.DataFrame(datapor)
datapor.isnull()
datapor.isnull().sum().sum()


# # verificacion de data de valor nulo para el csv student matematicas

# In[28]:



datamat=pd.read_csv(r'C:\Users\Lenovo 11 e\Desktop\SIC_GREIZEL_CURSO\student-mat.csv',sep =";")
pd.DataFrame(datamat)
datamat.isnull()
datamat.isnull().sum().sum()


# # 3.0 Para cada escuela muestre un gráfico circular(pastel) donde se evidencie el porcentaje de estudiantes hombres y mujeres de cada curso

# # 3. 1GRAFICO CIRCULAR - ESCUELA Mousinho da Silveira del curso de matematicas

# In[29]:


# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MS_mat.loc[(MS_mat['sex']=='F')]
fig, ax = plt.subplots()
MS_mat.sex.value_counts().plot(kind = "pie", labels = ["Mujeres", "Hombres"], title = "Escuela MS Porcentaje de hombres y mujeres en el curso de matematica")
plt.show()


# # 3.2 GRAFICO CIRCULAR - ESCUELA Mousinho da Silveira del curso de portugues

# In[30]:


# import pandas as pd

MS_por.loc[(MS_por['sex']=='F')]
fig, ax = plt.subplots()
MS_por.sex.value_counts().plot(kind = "pie", labels = ["Mujeres", "Hombres"], title = "Escuela MS Porcentaje de hombres y mujeres en el curso de portugues")
plt.show()


# # 3. 4GRAFICO CIRCULAR - ESCUELA Gabriel Pereira del curso de matematicas

# In[31]:


# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

GP_mat.loc[(GP_mat['sex']=='F')]
fig, ax = plt.subplots()
GP_mat.sex.value_counts().plot(kind = "pie", labels = ["Mujeres", "Hombres"], title = "Escuela GP Porcentaje de hombres y mujeres en el curso de matematica")
plt.show()


# # 3. 5 GRAFICO CIRCULAR - ESCUELA Gabriel Pereira del curso de portugues

# In[32]:


import numpy as np
import matplotlib.pyplot as plt

GP_por.loc[(GP_por['sex']=='F')]
fig, ax = plt.subplots()
GP_por.sex.value_counts().plot(kind = "pie", labels = ["Mujeres", "Hombres"], title = "Escuela GP Porcentaje de hombres y mujeres en el curso de portugues")
plt.show()


# # 4. 0 Para cada escuela muestre un gráfico de barras donde se muestre la cantidad de estudiantes que tienen la misma edad

# #  4.1 gráfico de barras donde se muestre la cantidad de estudiantes que tienen la misma edad de la Escuela Mousinho de silveira

# In[33]:


Data_student_MS.groupby("age").size().plot(kind = "bar", title = "cantidad de estudiantes que tienen la misma edad en la escuela MS")
plt.show()


# #    4. 2 Gráfico de barras donde se muestre la cantidad de estudiantes que tienen la misma edad de la Escuela GABRIEL PEREIRA

# In[34]:


Data_student_GP.groupby("age").size().plot(kind = "bar", title = "cantidad de estudiantes que tienen la misma edad en la escuela GP")
plt.show()


# #  5. 0 Muestre el promedio de las edades de cada curso de cada escuela

# # 5. 1 promedio de edades del curso de matematicas de la escuela Gabriel pereira

# In[35]:


print("Promedio de las edades en la escuela GP del curso de matematicas: ")
print(GP_mat['age'].mean())


# # promedio de edades del curso de PORTUGUES de la escuela Gabriel pereira

# In[36]:


print("Promedio de las edades en la escuela GP del curso de Portugues: ")
print(GP_por['age'].mean())


# # promedio de edades del curso de matematicas de la escuela Mousihno silveira

# In[37]:


print("Promedio de las edades en la escuela MS del curso de matematicas: ")
print(MS_mat['age'].mean())


# # promedio de edades del curso de portugues de la escuela Mousihno silveira

# In[38]:


print("Promedio de las edades en la escuela MS del curso de portugues: ")
print(MS_por['age'].mean())


# # 6.0 Muestre el promedio de las notas G1, G2, G3 de cada curso de cada escuela

# # promedio de G1 del curso de matematicas de la escuela Gabriel pereira

# In[39]:


print('El promedio de notas  de los estudiantes de la Gabriel Pereira de de matematicas es de : ')
print('El G1:')
GP_mat['G1'].mean()


# # PROMEDIO DE NOTAS DEL G2 DEL CURSO DE MATEMATICAS DE GABRIEL PEREIRA

# In[40]:


print('El promedio de notas  de los estudiantes de la Gabriel Pereira de de matematicas es de : ')
print('El G2:')
GP_mat['G2'].mean()


# # Promedio de notas del  G3 del curso de matematicas del GABRIEL PEREIRA

# In[41]:


print('El promedio de notas  de los estudiantes de la Gabriel Pereira de de matematicas es de : ')
print('El G3:')
GP_mat['G3'].mean()


# # 6. 1 promedio de nota del G1 , G2 Y G3 del curso de portugues de la escuela gabriel Pereira

# In[42]:


print('El promedio de notas  de los estudiantes de la Gabriel Pereira de portugues es de : ')
print('El G1:')
GP_por['G1'].mean()


# In[43]:


print('El promedio de notas  de los estudiantes de la Gabriel Pereira de portugues es de : ')
print('El G2:')
GP_por['G2'].mean()


# In[44]:


print('El promedio de notas  de los estudiantes de la Gabriel Pereira de portugues es de : ')
print('El G3:')
GP_por['G3'].mean()


# #  6. 2 promedio de nota del G1 , G2 Y G3 del curso de matematicas de la escuela Mousihno Silveira

# In[45]:


print('El promedio de notas  de los estudiantes de la Mousihno silveira de de matematicas es de : ')
print('El G1:')
MS_mat['G1'].mean()


# In[46]:


print('El promedio de notas  de los estudiantes de la  Mousihno silveira de de matematicas es de : ')
print('El G2:')
MS_mat['G2'].mean()


# In[47]:


print('El promedio de notas  de los estudiantes de la Mousihno silveira de de matematicas es de : ')
print('El G3:')
MS_mat['G3'].mean()


# # 6.4 promedio de nota del G1 , G2 Y G3 del curso de portugues de la escuela Mousihno Silveira

# In[48]:


print('El promedio de notas  de los estudiantes de la mousihno silveira de de portugues es de : ')
print('El G1:')
MS_por['G1'].mean()


# In[49]:


print('El promedio de notas  de los estudiantes de la mousihno silveira de de portugues es de : ')
print('El G2:')
MS_por['G2'].mean()


# In[50]:


print('El promedio de notas  de los estudiantes de la mousihno silveira de de portugues es de : ')
print('El G3:')
MS_por['G3'].mean()


# # 7. 0 Grafique el promedio de las notas en un gráfico de barras horizontal

# # grafica de promedio de notas de la escuela Mousihno silveira por cada curso de matematicas y portugues

# In[51]:


MS_mat.groupby("G1").size().plot(kind = "barh", title = "Graficos de notas de G1 la escuela  MS de matematicas ")
plt.show()
MS_mat.groupby("G2").size().plot(kind = "barh", title = "Graficos de notas de G2 de la escuela MS de matematicas ")
plt.show()
MS_mat.groupby("G3").size().plot(kind = "barh", title = "Graficos de notas de G3 la escuela  MS de matematicas ")
plt.show()
MS_por.groupby("G1").size().plot(kind = "barh", title = "Graficos de notas de G1 la escuela  MS de portugues")
plt.show()
MS_por.groupby("G2").size().plot(kind = "barh", title = "Graficos de notas de G2 de la escuela MS de portugues")
plt.show()
MS_por.groupby("G3").size().plot(kind = "barh", title = "Graficos de notas de G3 la escuela  MS de portugues")
plt.show()


# # 7. 1grafica de promedio de notas de la escuela Gabriel pereira por cada curso de matematicas y portugues

# In[52]:


GP_mat.groupby("G1").size().plot(kind = "barh", title = "Graficos de notas de G1 la escuela  GP de matematicas ")
plt.show()
GP_mat.groupby("G2").size().plot(kind = "barh", title = "Graficos de notas de G2 de la escuela GP de matematicas ")
plt.show()
GP_mat.groupby("G3").size().plot(kind = "barh", title = "Graficos de notas de G3 la escuela  GP de matematicas ")
plt.show()
GP_por.groupby("G1").size().plot(kind = "barh", title = "Graficos de notas de G1 la escuela  GP de portugues")
plt.show()
GP_por.groupby("G2").size().plot(kind = "barh", title = "Graficos de notas de G2 de la escuela GP de portugues")
plt.show()
GP_por.groupby("G3").size().plot(kind = "barh", title = "Graficos de notas de G3 la escuela  GP de portugues")
plt.show()


# # 8. 0 Halle el valor máximo de las ausencias y considere dicho valor como el total de clases del curso, de manera que pueda sacar un porcentaje de asistencia para cada estudiante

# In[53]:


from numpy import random
import pandas as pd

Ausencias = []
TotalGP = Data_student_GP['absences'].max()
for j in Data_student_GP['absences']:
    Ausencias.append(j)
    
print("\n")
print(f"EL MAXIMO DE AUSENCIAS EN LA ESCUELA GABRIEL PEREIRA ES DE {TotalGP}")
df= pd.DataFrame(Ausencias)
print(df)


# In[54]:


totalMS=maxValues_ausencias_MS = Data_student_MS['absences'].max() 

print(F"EL MAXIMO DE AUSENCIAS EN LA ESCUELA MOUSIHNO SILVEIRA ES DE {totalMS}") 


# # Cree una nueva columna llamada “approved” en la cual determine si el estudiante aprueba o reprueba el curso (1 para aprueba, 0 para reprueba), considerando:
# •	Si el estudiante tiene un porcentaje de asistencia menor al 80% del curso reprueba 
# •	Si el estudiante tiene un porcentaje de asistencia mayor al 80% del curso, pero la nota G3 es menor a 10 reprueba
# •	Si el estudiante tiene un porcentaje de asistencia m mayor al 80% del curso, pero la nota G3 está entre 10 y 15 aprueba y se asigna 1 a la columna extra
# •	Si el estudiante tiene un porcentaje de asistencia mayor al 80% del curso y la nota G3 es mayor a 15 aprueba y se asigna 0 a la columna extra
# 

# In[55]:


from numpy import random
import pandas as pd

# Agregar columna "Porcentaje de asistencia"
Data_student_GP["Porcentaje de asistencia"] = Data_student_GP["absences"].max()

# Agregar columna "Resultado"
Data_student_GP["Resultado"] = 0
# Crear diccionario que asigne valores numéricos a las etiquetas
resultado_dict = {"Aprueba": 1, "Reprueba": 0}

for index, row in Data_student_GP.iterrows():
    # Aplicar condiciones
    if row["Porcentaje de asistencia"] < 0.8 and row["G3"] < 10:
        Data_student_GP.loc[index, "Resultado"] = resultado_dict["Reprueba"]
    elif row["Porcentaje de asistencia"] >= 0.8 and row["G3"] < 10:
        Data_student_GP.loc[index, "Resultado"] = resultado_dict["Reprueba"]
    elif row["Porcentaje de asistencia"] >= 0.8 and 10 <= row["G3"] <= 15:
        Data_student_GP.loc[index, "Resultado"] = resultado_dict["Aprueba"]
        Data_student_GP.loc[index, "extra"] = 1
    elif row["Porcentaje de asistencia"] >= 0.8 and row["G3"] > 15:
        Data_student_GP.loc[index, "Resultado"] = resultado_dict["Aprueba"]
        Data_student_GP.loc[index, "extra"] = 0

# Imprimir conjunto de datos completo
print(pd.DataFrame(Data_student_GP))


# In[56]:


from numpy import random
import pandas as pd

from numpy import random
import pandas as pd

# Agregar columna "Porcentaje de asistencia"
Data_student_MS["Porcentaje de asistencia"] = Data_student_MS["absences"].max()

# Agregar columna "Resultado"
Data_student_MS["Resultado"] = 0
# Crear diccionario que asigne valores numéricos a las etiquetas
resultado_dict = {"Aprueba": 1, "Reprueba": 0}

for index, row in Data_student_MS.iterrows():
    # Aplicar condiciones
    if row["Porcentaje de asistencia"] < 0.8 and row["G3"] < 10:
        Data_student_MS.loc[index, "Resultado"] = resultado_dict["Reprueba"]
    elif row["Porcentaje de asistencia"] >= 0.8 and row["G3"] < 10:
        Data_student_MS.loc[index, "Resultado"] = resultado_dict["Reprueba"]
    elif row["Porcentaje de asistencia"] >= 0.8 and 10 <= row["G3"] <= 15:
        Data_student_MS.loc[index, "Resultado"] = resultado_dict["Aprueba"]
        Data_student_MS.loc[index, "extra"] = 1
    elif row["Porcentaje de asistencia"] >= 0.8 and row["G3"] > 15:
        Data_student_MS.loc[index, "Resultado"] = resultado_dict["Aprueba"]
        Data_student_MS.loc[index, "extra"] = 0

# Imprimir conjunto de datos completo
print(pd.DataFrame(Data_student_MS))


# In[57]:


import matplotlib.pyplot as plt

# Contar número de aprobados y reprobado
aprobados = Data_student_MS[Data_student_MS["Resultado"] == 1].shape[0]
reprobados = Data_student_MS[Data_student_MS["Resultado"] == 0].shape[0]

# Dibujar gráfico circular
labels = ["Aprobados", "Reprobados"]
sizes = [aprobados, reprobados]
colors = ["#0000FF", "#FF0000"]

plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct="%1.1f%%")

plt.axis("equal")
plt.title("Porcentaje de aprobados y reprobados de la escuela mousihno silveira")

plt.show()


# In[58]:


import matplotlib.pyplot as plt

# Contar número de aprobados y reprobados
aprobados = Data_student_GP[Data_student_GP["Resultado"] == 1].shape[0]
reprobados = Data_student_GP[Data_student_GP["Resultado"] == 0].shape[0]

# Dibujar gráfico circular
labels = ["Aprobados","Reprobados"]
sizes = [aprobados, reprobados]
colors = ["#0000FF", "#FF0000"]

plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct="%1.1f%%")

plt.axis("equal")
plt.title("Porcentaje de aprobados y reprobados de la escuela Gabriel pereira ")

plt.show()


# In[59]:


import datetime

# Obtener fecha y hora actual
now = datetime.datetime.now()

# Generar nombre de archivo CSV
filename = "Resultado " + now.strftime("%Y-%m-%d %H-%M-%S") + ".csv"

# Guardar DataFrame en archivo CSV
Data_student_MS.to_csv(filename)

import datetime

# Obtener fecha y hora actual
now = datetime.datetime.now()

# Generar nombre de archivo CSV
filename = "Resultado " + now.strftime("%Y-%m-%d %H-%M-%S") + ".csv"

# Guardar DataFrame en archivo CSV
Data_student_MS.to_csv(filename)


# In[60]:


import datetime

# Obtener fecha y hora actual
now = datetime.datetime.now()

# Generar nombre de archivo CSV
filename = "Resultado " + now.strftime("%Y-%m-%d %H-%M-%S") + ".csv"

# Guardar DataFrame en archivo CSV
Data_student_GP.to_csv(filename)

import datetime

# Obtener fecha y hora actual
now = datetime.datetime.now()

# Generar nombre de archivo CSV
filename = "Resultado " + now.strftime("%Y-%m-%d %H-%M-%S") + ".csv"

# Guardar DataFrame en archivo CSV
Data_student_GP.to_csv(filename)


# In[ ]:




