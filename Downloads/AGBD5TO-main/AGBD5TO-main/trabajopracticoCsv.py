
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
filtro_avanzado=df[['nivel_instruccion_descripcion','nivel_instruccion_descripcion_id']]
df_filtrado=df[filtro_avanzado]
print(filtro_avanzado.head())

#Selección de Columnas Clave ............
filtro_avanzado=df['estado_civil_id'].head()
df_filtrado=df[filtro_avanzado]
print(filtro_avanzado)

  #Agrupación y Resumen
filtro_avanzado=df['estado_civil_descripcion'].groupby()
df_filtrado=df[filtro_avanzado]
sumo_filas=df_filtrado['estado_civil_id'].sum()
print ("sum()")
print 

  #Estructura de Control Automatizada
 
if limite_alto_de_separaciones := (sumo_filas > 10):
    print ("¡te separaste muchas veses.")
    print("Requiere revision inmediata")
elif sumo_filas < 10:
    print("Aviso:Estas soltero hace 10 años")
else:
    print ("Estas bien ,sin problemas por el momento")

# Gráfico de Barras Comparativo



#  ejecercicio 9
filtro_avanzado = (df['nivel_instruccion_descripcion'] == 'Universitario Completo') & (df['nivel_instruccion_descripcion_id'] >= 5)
df_filtrado = df.loc[filtro_avanzado, ['nivel_instruccion_descripcion_id', 'nivel_instruccion_descripcion', 'id_usuario']]
print(df_filtrado.head())
print(f'\nFilas seleccionadas: {len(df_filtrado)}')

# si hubiera quedado igual si usabamos un filto en vezz de  &,ademas el codigo s ve mejor esteticaamente haciendo tmabien que se entienda mejor.
 

#  ejecercicio diez
print('Nulos por columna:')
print(df.isnull().sum())


# Paso  eliminar filas con nulos
df_sin_nulos = df.dropna()

columna_num = 'nivel_instruccion_descripcion_id' 
media_columna = df[columna_num].mean()//sacamos promedio

df_rellenado = df.copy()
df_rellenado[columna_num] = df_rellenado[columna_num].fillna(media_columna)
  
print(" dropna()")
print(df_sin_nulos.head())

print("\n Versión con fillna()")
print(df_rellenado.head())


filtro_avanzado = (df['nivel_instruccion_descripcion'] == 'Universitario Completo') & (df['nivel_instruccion_descripcion_id'] >= 5)
df_filtrado = df.loc[filtro_avanzado, ['nivel_instruccion_descripcion_id', 'nivel_instruccion_descripcion', 'id_usuario']]
print(df_filtrado.head())
print(f'\nFilas seleccionadas: {len(df_filtrado)}')




df_filtrado = df.query("nivel_instruccion_descripcion == 'Universitario Completo' and nivel_instruccion_descripcion_id >= 5")[
    ['nivel_instruccion_descripcion_id', 'nivel_instruccion_descripcion', 'id_usuario']
]
print(df_filtrado.head())
print(f'\nFilas seleccionadas: {len(df_filtrado)}')
)



filtro_avanzado = (df['nivel_instruccion_descripcion'] == 'Universitario Completo') & (df['nivel_instruccion_descripcion_id'] >= 5)
resultado_original = df.loc[filtro_avanzado, ['nivel_instruccion_descripcion_id', 'nivel_instruccion_descripcion', 'id_usuario']]
 

limite_id = 5


resultado_query = df.query('nivel_instruccion_descripcion == "Universitario Completo" and nivel_instruccion_descripcion_id >= @limite_id')[
    ['nivel_instruccion_descripcion_id', 'nivel_instruccion_descripcion', 'id_usuario']
]
 
print('Con corchetes:')
print(resultado_original.head()) 

print('\nCon .query():')
print(resultado_query.head())

print('\n¿Son iguales?', resultado_original.equals(resultado_query))
¿El resultado de .query() es idéntico al de su filtro_avanzado? ¿Por qué?
Sí da exactamente lo mismo y el .equals() tira True. Es porque los dos comandos hacen el mismo filtro , lo único que cambia es la forma en que lo escribimos en el código. Las filas que entran y salen de la tabla terminan siendo las mismas.

# ¿Cuál de las dos formas les parece más clara para leer?
 # La de .query() es  más limpia. Te ahorrás de escribir df['columna'] a cada rato . Además, queda re parecido a cómo hablamos nosotros o a cómo se escribe en inglés usando el and en vez del &.
  # ¿Qué ventaja tiene usar @ en lugar de escribir el valor directamente en el texto?
   # Está buenísimo porque si después querés cambiar el número del filtro (por ejemplo, pasar de 5 a 9), cambiás solamente la variable de arriba.# 


# Incluir categorías seleccionadas
filtro_avanzado= ['Desocupado/a', 'Ocupado/a']
df_incluidos = df[df['ultima_situacion_laboral_descripcion'].isin(filtro_avanzado)]
print('Solo  Desocupado/a y Ocupado/a:')
print(df_incluidos)

df_excluidos = df[~df['ultima_situacion_laboral_descripcion'].isin( Buscando empleo)]
 
print(f'Filas incluidas ({len(df_incluidos)}):')
print(df_incluidos)
print(f'\nFilas excluidas ({len(df_excluidos)}):')
print(df_excluidos)

total = len(df)
suma  = len(df_incluidos) + len(df_excluidos)
print(f'\nTotal original: {total}  |  Incluidos + Excluidos: {suma}')
print(f'¿Coinciden? {total == suma}')



print('=== DataFrame completo ===')
print(df['nivel_instruccion_descripcion'].value_counts())
print('Valores únicos:', df['nivel_instruccion_descripcion'].unique())
print('Cantidad de categorías:', df['columna_texto'].nunique())
print('Porcentajes:')
print((df['nivel_instruccion_descripcion'].value_counts(normalize=True) * 100).round(1))

df_filtrado = df[filtro_avanzado]
 
print('\n=== DataFrame filtrado ===')
print(df_filtrado['nivel_instruccion_descripcion'].value_counts())
print('Valores únicos:', df_filtrado['nivel_instruccion_descripcion'].unique())
print('Cantidad de categorías:', df_filtrado['nivel_instruccion_descripcion'].nunique())
print('Porcentajes:')
print((df_filtrado['nivel_instruccion_descripcion'].value_counts(normalize=True) * 100).round(1))

 #¿Cambia la distribución de categorías entre el DataFrame completo y el filtrado? ¿Qué dice eso?
 #Sí,  cambia. Al meter el filtro dejamos afuera a un montón de gente y nos quedamos con un grupo re específico. Que cambien los porcentajes significa que ese grupo tiene una onda re distinta al promedio de toda la tabla entera; no se comportan igual que el resto.

 #¿Hay alguna categoría que desapareció completamente al aplicar el filtro?
 # Sí, Al filtrar para quedarnos solo con "Universitario Completo", todas las demás categorías como "Primaria" o "Secundaria" desaparecieron por completo del mapa porque el filtro los saco a todas.

# ¿value_counts() y groupby().count() dan el mismo resultado? ¿Cuándo usarían cada uno?
#  Sí, los números te dan igual pero te los muestran distinto. El value_counts() lo usaría cuando quiero ver algo rápido de una sola columna, porque ya te lo ordena de mayor a menor. El groupby().count() lo usaría más para cuando te pide algo más complejo, tipo armar una tablita y comparar varias columnas a la vez.

# Paso 1: exportar el DataFrame filtrado
df_filtrado = df[filtro_avanzado]
df_filtrado.to_csv('mi_resultado_filtrado.csv', index=False)
print(f'Archivo exportado: {len(df_filtrado)} filas guardadas.')
 
# Paso 2: correlación del DataFrame completo
correlacion = df.corr(numeric_only=True)
print('\nMatriz de correlación:')
print(correlacion.round(2))
 
# Pasos 3 y 4: heatmap y guardar
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlacion,
    annot=True,
    fmt='.2f',
    cmap='gray',   # cambiar por la que elijan
    linewidths=0.5,
    vmin=-1, vmax=1
)
plt.title('Correlación entre variables — Mi Dataset', fontweight='bold')
plt.tight_layout()
plt.savefig('heatmap_mi_dataset.png', dpi=150)
plt.show()

# Paso 5: identificar el par más y menos correlacionado
mask = np.triu(np.ones(correlacion.shape), k=0).astype(bool)
correlacion_sin_diag = correlacion.where(~mask)
 
par_max = correlacion_sin_diag.stack().idxmax()
par_min = correlacion_sin_diag.stack().idxmin()
print(f'\nPar más correlacionado:   {par_max[0]} ↔ {par_max[1]}')
print(f'Par menos correlacionado: {par_min[0]} ↔ {par_min[1]}')







