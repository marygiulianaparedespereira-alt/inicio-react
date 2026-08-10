import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("trabajopracticoCsv")


filtro_avanzado=df['fue_lesionado_descripcion'].str.startswith("Tucuman", na=False)
df_filtrado=df[filtro_avanzado]
restar_condena=df_filtrado['duracion_condena_anios'].sub(df[])
print ("COLUMNA CATEGORIA")
print(f"Anios con condena ;{restar_condena}.\n")

if Default_limite_condenas := (restar_condena <):
    print ("La condena es alta ,esta lesionado")
    print("Requiere revision inmediata")
elif restar_condena< 10:
    print("Aviso:Edad menor a 10")
else:
    print ("mercado estable,sin alertas por el momento")
    #grafico de barras usando toda df
print ("\n [Generando GRAFICO de barras]")
