
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("trabajopracticoCsv")


filtro_avanzado=df['fue_lesionado_descripcion'].str.startswith("Tucuman", na=False)
df_filtrado=df[filtro_avanzado]
restar_condena=df_filtrado['duracion_condena_anios'].sub(df[])
print ("COLUMNA CATEGORIA")
print(f"Anios con condena ;{restar_condena}.\n")

if Default_limite_condenas := (restar_condena > 10):
    print ("La condena es alta ,esta lesionado")
    print("Requiere revision inmediata")
elif restar_condena< 10:
    print("Aviso:Edad menor a 10")
else:
    print ("mercado estable,sin alertas por el momento")
    #grafico de barras usando toda df
print ("\n [Generando GRAFICO de barras]")

  #
filtro_avanzado=df[df]
df_filtrado=df[filtro_avanzado]
sumo_filas=df_filtrado['..'].sum()
print ("filas")
print(f"filas;{sumo_filas}.\n")

  #Filtrar por texto parcial
filtro_avanzado=df['ultima_situacion_laboral_descripcion'].str.startswith("Desocupado/a", na=False)
df_filtrado=df[filtro_avanzado]
print(filtro_avanzado)

  #Filtrar por coincidencia exacta
iltro_avanzado=df['ultima_situacion_laboral_descripcion']
df_filtrado=df[df['Trabajador/ra de tiempo completo'] == 'Trabajador/ra de tiempo completo']
print(filtro_avanzado)

#Selección de Columnas Clave
filtro_avanzado=df['nivel_instruccion_descripcion'].head()
df_filtrado=df[filtro_avanzado]


#Selección de Columnas Clave ............
filtro_avanzado=df['estado_civil_id'].head()
df_filtrado=df[filtro_avanzado]

  #Agrupación y Resumen
filtro_avanzado=df['estado_civil_descripcion'].groupby()
df_filtrado=df[filtro_avanzado]
sumo_filas=df_filtrado['estado_civil_id'].sum()
print ("")

  #Estructura de Control Automatizada
 
if limite_alto_de_separaciones := (sumo_filas > 10):
    print ("¡te separaste muchas veses.")
    print("Requiere revision inmediata")
elif sumo_filas < 10:
    print("Aviso:Estas soltero hace 10 años")
else:
    print ("Estas bien ,sin problemas por el momento")

# Gráfico de Barras Comparativo



