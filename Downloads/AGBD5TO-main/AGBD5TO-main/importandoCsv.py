import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns




#solo ponemos el nombre exacto del archivo, entre comillas
df=pd.read_csv("sneep-2024.csv")
#print("OKEY! archivo cargando correctamente")
#filtro
#mostrando las primeras filas  del dataframe
#print(df.head())
#mostrando resultado del año sea igual a 2022
#resultado= df[df['censo_anio']==2022]
#print(resultado)
#total =df['censo_anio'].count()
#print(f"total:{total}")

#provinciaid=df['privincia_id']
#print(provinciaid)

#provincia=df['provincia_id'].sum()
#print(f"provincias:{provincia}")


filtro_avanzado=df['provincia_descripcion'].str.startswith("Tucuman", na=False)
#filtro_nuevo=df['establecimiento_id']>134
df_filtrado=df[filtro_avanzado]
sumo_edad=df_filtrado['edad'].sum()
print ("EDADES")
print(f"monto analizado;{sumo_edad}.\n")


//df_filtrado=df[filtro_avanzado]
sumo_tabla=df_filtrado["x"].count(["x"])
# ejercicio 2
filtro_avanzado=df['nacionalidad_descripcion'].str.startswith("Argentina", na=False)
df_filtrado=df[filtro_avanzado]
identicos_nacio=df_filtrado['Argentina']=='Argentina'
print ("nacionalidad")
print(f"nacionalidad  analizado;{identicos_nacio}.\n")

##ejercicio 3


#filtro_numero=df['establecimiento_id']>500
#clave morse quiere decir que primero sumo y lurgo lo guardo em la varriable
if Default_limite_alto := (sumo_edad>50):
    print ("¡Alerta El monto total supera el limite  establecido.")
    print("Requiere revision inmediata")
elif sumo_edad < 10:
    print("Aviso:Edad menor a 10")
else:
    print ("mercado estable,sin alertas por el momento")
    #grafico de barras usando toda df
print ("\n [Generando GRAFICO de barras]")
sns.set_theme (style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="edad",
    y="provincia_descripcion",
    errorbar=None,
    palette="viridis",

)
plt.title("Edades" ,fontsize=14)
plt.xticks(rotation=20)
#guardo grafico generado 
plt.savefig("Grafico_barra.png",dpi=300)
plt.close()
    

print ("\n¡Hecho! Los graficos se guardaron correctamente en tu carpeta")