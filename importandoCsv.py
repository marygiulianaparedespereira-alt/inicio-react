import pandas as pd 

#solo ponemos el nombre exacto del archivo, entre comillas
df=pd.read_csv("sneep-2024.csv")
print("OKEY! archivo cargando correctamente")
#mostrando las primeras filas  del dataframe
print(df.head())
#mostrando resultado del año sea igual a 2022
#resultado= df[df['censo_anio']==2022]
#print(resultado)
#total =df['censo_anio'].count()
#print(f"total:{total}")

#provinciaid=df['privincia_id']
#print(provinciaid)

provincia=df['provincia_id'].sum()
print(f"provincias:{provincia}")


filtro_avanzado=df['provincia_descripcion'].str.startswith("Tucuman", na=False)
filtro_nuevo=df['establecimiento_id']>134
df_filtrado=df[filtro_avanzado]
sumo_establecimiento=df_filtrado['establecimiento_id'].sum()
print ("establecimentos")
print(f"monto analizado;{sumo_establecimiento:.2f}.\n")

filtro_numero=df['establecimiento_id']>500