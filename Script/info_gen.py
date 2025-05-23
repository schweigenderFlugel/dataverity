import pandas as pd
import random
import string

# Número de estudiantes a simular
num_estudiantes = 540

# === CARGA DE NOMBRES DESDE ARCHIVO ===
def cargar_nombres(archivo):
    with open(archivo, encoding='utf-8') as f:
        lineas = [line.strip() for line in f if line.strip()]
    
    try:
        idx_m = lineas.index("# Masculinos") + 1
        idx_f = lineas.index("# Femeninos") + 1
        nombres_m = lineas[idx_m:idx_f-1]
        nombres_f = lineas[idx_f:]
        return nombres_m, nombres_f
    except ValueError:
        raise ValueError("El archivo debe contener '# Masculinos' y '# Femeninos' como encabezados.")

nombres_masculinos, nombres_femeninos = cargar_nombres("nombres.txt")

# Distribución fija por edad según el ejemplo dado
edad_distribucion = (
    [6]*90 + 
    [7]*90 + 
    [8]*90 + 
    [9]*90 + 
    [10]*90 + 
    [11]*90
)

# Barajamos el orden para que no estén agrupados por edad
random.shuffle(edad_distribucion)

# Asignación de grados según la edad siguiendo la Estructura 1
def asignar_grado_por_edad(edad):
    if edad == 6:
        return 1
    elif edad == 7:
        return 2
    elif edad == 8:
        return 3
    elif edad == 9:
        return 4
    elif edad == 10:
        return 5
    elif edad == 11:
        return 6
    elif edad == 12:
        return 6  # Podría ser repitente o en edad avanzada, sigue en 6°
    else:
        return None  # fuera de rango esperado

# Puedes cambiar los porcentajes ajustando los pesos (más abajo están comentados)
def tipo_neae():
    return random.choices(
        population=['Normal', 'TDAH', 'TEA', 'Dislexia'],
        weights=[80, 10, 5, 5],  # ← Cambia estos pesos si quieres otro porcentaje
        k=1
    )[0]

def escala_1_5(): 
    return random.randint(1, 5)

def booleano_prob(p_true=0.5):  
    return random.random() < p_true

def generar_legajo():
    longitud = random.randint(4, 10)
    #return ''.join(random.choices(string.ascii_uppercase + string.digits, k=longitud))
    return ''.join(random.choices(string.digits, k=longitud))

# === Generación de géneros y nombres coherentes ===
# Distribución de género: 47% M, 53% F
generos = random.choices(['M', 'F'], weights=[47, 53], k=num_estudiantes)

# Aseguramos que no se repitan nombres (si hay suficientes)
random.shuffle(nombres_masculinos)
random.shuffle(nombres_femeninos)
nombres_asignados = []

for g in generos:
    if g == 'M':
        nombre = nombres_masculinos.pop() if nombres_masculinos else "NombreM"
    else:
        nombre = nombres_femeninos.pop() if nombres_femeninos else "NombreF"
    nombres_asignados.append(nombre)

# Asignamos los grados antes de crear el DataFrame
grados_asignados = [asignar_grado_por_edad(e) for e in edad_distribucion]

# === Simulación de datos ===
data = {
    # Identificador único del estudiante (del 1 al número total de estudiantes)
    'id_estudiante': range(1, num_estudiantes + 1),

    # Legajo estudiantil único del estudiante (cadena alfanumérica de 4 a 10 caracteres)
    'legajo': [generar_legajo() for _ in range(num_estudiantes)],

    # Edad del estudiante (entre 6 y 12 años, típico de educación primaria)
    'edad': edad_distribucion,

    # Nombre del estudiante (Asignado al azar de 'nombres.txt')
    'nombre': nombres_asignados,

    # Género del estudiante: 'M' (masculino) o 'F' (femenino), generado aleatoriamente
    # Puedes personalizar la función genero() para incluir más opciones o ajustar proporciones
    'genero': generos,

    # Grado escolar del estudiante (del 1 al 6, equivalente a años de educación primaria)
    'grado': grados_asignados,

    # Booleanos con probabilidad personalizada
    'asistencia_inicial': [booleano_prob(0.9) for _ in range(num_estudiantes)],   # 0.9 = 90% True
    'internet_en_casa': [booleano_prob(0.85) for _ in range(num_estudiantes)],    # 0.85 = 85% True
    'adecuaciones_curriculares': [booleano_prob(0.25) for _ in range(num_estudiantes)],  # 0.25 = 25% True
    'violencia_familiar': [booleano_prob(0.1) for _ in range(num_estudiantes)],   # 0.1 = 10% True
    'enfermedad_grave_familiar': [booleano_prob(0.15) for _ in range(num_estudiantes)],  # 0.15 = 15% True
    'catastrofe_familiar': [booleano_prob(0.05) for _ in range(num_estudiantes)], # 0.05 = 5% True
    'conducta_riesgo_observada': [booleano_prob(0.2) for _ in range(num_estudiantes)],   # 0.2 = 20% True
    'asistencia': [round(random.uniform(70.0, 100.0), 2) for _ in range(num_estudiantes)], # Porcentaje entre 70% y 100% con 2 decimales
    'calificacion_matematica': [round(random.uniform(1.0, 10.0), 1) for _ in range(num_estudiantes)], # escala de 1.0 a 10.0, con 1 decimal
    'calificacion_lengua': [round(random.uniform(1.0, 10.0), 1) for _ in range(num_estudiantes)], # escala de 1.0 a 10.0, con 1 decimal
    'horas_clase_semanales': [random.randint(20, 35) for _ in range(num_estudiantes)], # Entre 20 y 35 horas
    'motivacion': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
    'habilidades_de_autorregulacion': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
    'habilidades_interpersonales': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
    'habilidades_intrapersonales': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
    'conducta_riesgo': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
    'libros_en_casa': [booleano_prob(0.65) for _ in range(num_estudiantes)], # 0.65 = 65% True
    'distancia_escuela_km': [round(random.uniform(0.1, 15.0), 2) for _ in range(num_estudiantes)], # Distancia en km entre 0.1 a 15.0
    'clima_escolar': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
    'capacitacion_docente_anual_horas': [random.randint(0, 80) for _ in range(num_estudiantes)], # Entre 0 y 80 horas
    'tenencia_director_anos': [random.randint(1, 30) for _ in range(num_estudiantes)], # entre 1 a 30 años
    'tipo_neae': [tipo_neae() for _ in range(num_estudiantes)],
    'resiliencia_familiar': [escala_1_5() for _ in range(num_estudiantes)], # Escala de 1 a 5
}

# Crear DataFrame
df = pd.DataFrame(data)

# === ASIGNACIÓN DE SECCIÓN ===
# Asignar secciones A, B, C a cada grado con 30 estudiantes por sección
secciones = []
for grado in range(1, 7):
    mask = df['grado'] == grado
    indices = df[mask].index.tolist()
    random.shuffle(indices)
    for i, idx in enumerate(indices):
        if i < 30:
            secciones.append((idx, 'A'))
        elif i < 60:
            secciones.append((idx, 'B'))
        else:
            secciones.append((idx, 'C'))

# Aplicar secciones
df['seccion'] = ''
for idx, sec in secciones:
    df.at[idx, 'seccion'] = sec

# Reordenar las columnas según lo solicitado
columnas_ordenadas = [
    "id_estudiante", 
    "legajo",
    "nombre",
    "edad", 
    "genero", 
    "grado", 
    "seccion",  # ← NUEVA COLUMNA
    "asistencia_inicial", 
    "asistencia", 
    "calificacion_matematica", 
    "calificacion_lengua", 
    "horas_clase_semanales", 
    "motivacion", 
    "habilidades_de_autorregulacion", 
    "habilidades_interpersonales", 
    "habilidades_intrapersonales", 
    "conducta_riesgo", 
    "libros_en_casa", 
    "internet_en_casa", 
    "distancia_escuela_km", 
    "clima_escolar", 
    "capacitacion_docente_anual_horas", 
    "tenencia_director_anos", 
    "adecuaciones_curriculares",
    "tipo_neae", 
    "violencia_familiar",
    "enfermedad_grave_familiar",
    "catastrofe_familiar",
    "resiliencia_familiar",
    "conducta_riesgo_observada"
]

df = df[columnas_ordenadas]

# Guardar como CSV
csv_path = "C:/Users/User/Desktop/NoCountry/proyectoexpress4/Script/simulacion_estudiantes.csv"
df.to_csv(csv_path, index=False)

print(df['grado'].value_counts())

csv_path