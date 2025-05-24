# src/generate_recommendations.py

import io
import pandas as pd
from pathlib import Path

def load_data(data_path: str) -> pd.DataFrame:
    """
    Carga el CSV de simulación de estudiantes.
    """
    return pd.read_csv(data_path)


def generar_recomendaciones_para_alumno(row: pd.Series) -> list:
    """
    row: Serie con datos de un estudiante específico (incluye todas las columnas crudas).
    Devuelve una lista de cadenas, cada una es un texto de recomendación.
    """
    recomendaciones = []

    # --- 1) Calificación en Matemática ---
    if 'calificacion_matematica' in row.index:
        try:
            nota_mate = float(row['calificacion_matematica'])
        except:
            nota_mate = None

        if nota_mate is None or pd.isna(nota_mate):
            recomendaciones.append("No disponible nota de Matemática.")
        elif nota_mate < 4.0:
            recomendaciones.append(
                "Calificación en Matemática baja (<4.0). Reforzar con ejercicios prácticos, tutorías y revisión de conceptos básicos."
            )
        elif nota_mate < 6.0:
            recomendaciones.append(
                "Calificación en Matemática moderada (4.0–6.0). Aumentar práctica con guías y problemas de nivel intermedio."
            )
        else:
            recomendaciones.append("Desempeño en Matemática aceptable. Mantener rutina de ejercicios.")

    # --- 2) Calificación en Lengua ---
    if 'calificacion_lengua' in row.index:
        try:
            nota_len = float(row['calificacion_lengua'])
        except:
            nota_len = None

        if nota_len is None or pd.isna(nota_len):
            recomendaciones.append("No disponible nota de Lengua.")
        elif nota_len < 4.0:
            recomendaciones.append(
                "Calificación en Lengua baja (<4.0). Trabajar comprensión lectora y expresión escrita/oral; fomentar la lectura en casa."
            )
            # Si la nota es baja, chequeamos habilidades sociales
            if ('habilidades_interpersonales' in row.index and 
                (pd.isna(row['habilidades_interpersonales']) or row['habilidades_interpersonales'] <= 2)):
                recomendaciones.append(
                    "Habilidades interpersonales bajas (≤2). Incluir actividades grupales o talleres de comunicación."
                )
            if ('habilidades_intrapersonales' in row.index and 
                (pd.isna(row['habilidades_intrapersonales']) or row['habilidades_intrapersonales'] <= 2)):
                recomendaciones.append(
                    "Habilidades intrapersonales bajas (≤2). Trabajar autoconocimiento y autoestima mediante dinámicas de reflexión."
                )
            if ('habilidades_de_autorregulacion' in row.index and 
                (pd.isna(row['habilidades_de_autorregulacion']) or row['habilidades_de_autorregulacion'] <= 2)):
                recomendaciones.append(
                    "Habilidades de autorregulación bajas (≤2). Enseñar técnicas de planificación y organización para mejorar rendimiento en Lengua."
                )
        elif nota_len < 6.0:
            recomendaciones.append(
                "Calificación en Lengua media (4.0–6.0). Reforzar áreas específicas (gramática, ortografía, comprensión)."
            )
        else:
            recomendaciones.append("Desempeño en Lengua adecuado. Seguir practicando lectura y escritura.")

    # --- 3) Motivación y Clima Escolar ---
    if 'motivacion' in row.index:
        try:
            mot = float(row['motivacion'])
        except:
            mot = None

        if mot is None or pd.isna(mot) or mot <= 2:
            recomendaciones.append(
                "Motivación baja (≤2). Indagar causas (clima escolar, dificultades familiares) y aplicar dinámicas lúdicas o mentorías personalizadas."
            )
        else:
            recomendaciones.append("Motivación aceptable. Reforzar con elogios y seguimiento cercano.")

    if 'clima_escolar' in row.index:
        try:
            clima = float(row['clima_escolar'])
        except:
            clima = None

        if clima is None or pd.isna(clima) or clima <= 2:
            recomendaciones.append(
                "Clima escolar bajo (≤2). Evaluar convivencia en el aula y promover actividades de integración grupal."
            )
        else:
            recomendaciones.append("Clima escolar adecuado. Mantener acciones de cohesión y clima positivo.")

    # --- 4) Recursos en casa: Libros e Internet ---
    if 'libros_en_casa' in row.index and row['libros_en_casa'] == False:
        recomendaciones.append(
            "Sin libros en casa. Facilitar acceso a bibliografía escolar o coordinar préstamo de textos de biblioteca."
        )
    if 'internet_en_casa' in row.index and row['internet_en_casa'] == False:
        recomendaciones.append(
            "Sin internet en casa. Evaluar alternativas: acceso a espacios con Wi-Fi o entrega de material impreso para reforzar Lengua y Matemática."
        )

    # --- 5) Adecuaciones Curriculares y Tipo NEAE ---
    if 'adecuaciones_curriculares' in row.index and row['adecuaciones_curriculares'] == False:
        recomendaciones.append(
            "No presenta adecuaciones curriculares. Revisar si requiere apoyos o adaptaciones educativas individuales."
        )
    if 'tipo_neae' in row.index and isinstance(row['tipo_neae'], str) and row['tipo_neae'].lower() != 'normal':
        recomendaciones.append(
            f"Tipo de NEAE: {row['tipo_neae']}. Asegurar que reciba las adaptaciones y apoyos pedagógicos adecuados."
        )

    # --- 6) Factores Familiares (Violencia, Enfermedad, Catástrofe, Resiliencia) ---
    if 'violencia_familiar' in row.index and row['violencia_familiar'] == True:
        recomendaciones.append(
            "Se detecta violencia familiar. Coordinar con orientación psicopedagógica y referir a servicios de apoyo."
        )
    if 'enfermedad_grave_familiar' in row.index and row['enfermedad_grave_familiar'] == True:
        recomendaciones.append(
            "Existe enfermedad grave en familia. Proveer contención emocional y considerar adaptaciones temporales en clases."
        )
    if 'catastrofe_familiar' in row.index and row['catastrofe_familiar'] == True:
        recomendaciones.append(
            "Se identifica catástrofe familiar. Gestionar derivación a psicólogo y acompañamiento especializado."
        )
    if 'resiliencia_familiar' in row.index:
        try:
            resi = float(row['resiliencia_familiar'])
        except:
            resi = None
        if resi is not None and resi <= 2:
            recomendaciones.append(
                "Resiliencia familiar baja (≤2). Diseñar actividades de fortalecimiento de redes de apoyo intra-familia."
            )

    # --- 7) Distancia a la Escuela ---
    if 'distancia_escuela_km' in row.index:
        try:
            dist = float(row['distancia_escuela_km'])
        except:
            dist = None
        if dist is not None and dist > 5.0:
            recomendaciones.append(
                f"Distancia a la escuela elevada ({dist:.1f} km). Evaluar transporte escolar o estrategias de traslado alternativas."
            )

    # --- 8) Horas de clase semanales / Capacitación docente / Tenencia del director ---
    if 'horas_clase_semanales' in row.index:
        try:
            horas = float(row['horas_clase_semanales'])
        except:
            horas = None
        if horas is not None and horas < 20:
            recomendaciones.append(
                "Pocas horas de clase semanales (<20). Valorar refuerzos fuera del horario lectivo o talleres extra."
            )

    if 'capacitacion_docente_anual_horas' in row.index:
        try:
            cap_doc = float(row['capacitacion_docente_anual_horas'])
        except:
            cap_doc = None
        if cap_doc is not None and cap_doc < 10:
            recomendaciones.append(
                "Capacitación docente anual baja (<10 h). Promover cursos y talleres para fortalecer estrategias de enseñanza."
            )

    if 'tenencia_director_anos' in row.index:
        try:
            ten_dir = float(row['tenencia_director_anos'])
        except:
            ten_dir = None
        if ten_dir is not None and ten_dir < 2:
            recomendaciones.append(
                "Director con poco tiempo en el cargo (<2 años). Vigilar la estabilidad institucional y liderazgo."
            )

    # --- 9) Conducta de Riesgo Observada ---
    if 'conducta_riesgo_observada' in row.index and row['conducta_riesgo_observada'] == True:
        recomendaciones.append(
            "Conducta de riesgo observada en el aula. Derivar a orientación psicológica y realizar seguimiento cercano."
        )

    return recomendaciones


def generate_all_recommendations(data_path: str, output_dir: str) -> pd.DataFrame:
    """
    - Carga el CSV con los datos de estudiantes.
    - Para cada estudiante (cada fila), invoca generar_recomendaciones_para_alumno.
    - Devuelve y guarda un DataFrame con columnas:
        id_estudiante, nombre, grado, seccion, recomendaciones (como texto largo).
    """
    # 1. Cargar datos
    df = load_data(data_path)

    resultados = []

    # 2. Iterar por cada fila/alumno
    for _, row in df.iterrows():
        recs_lista = generar_recomendaciones_para_alumno(row)
        recs_str = " | ".join(recs_lista) if recs_lista else ""

        # Construyo el diccionario de salida, incluyendo los campos solicitados
        resultados.append({
            'id_estudiante': row.get('id_estudiante', None),
            'nombre': row.get('nombre', ""),
            'grado': row.get('grado', ""),
            'seccion': row.get('seccion', ""),
            'recomendaciones': recs_str
        })

    # 3. Crear DataFrame y guardar a CSV
    df_recs = pd.DataFrame(resultados,
                           columns=['id_estudiante', 'nombre', 'grado', 'seccion', 'recomendaciones'])

    # os.makedirs(output_dir, exist_ok=True)
    # output_path = os.path.join(output_dir, 'recomendaciones_personalizadas.csv')
    buffer = io.StringIO()
    df_recs.to_csv(buffer, index=False)
    buffer.seek(0)

    return df_recs, buffer


# if __name__ == '__main__':
    # Ajusta esta ruta si tu CSV está en otra ubicación
# base_url = Path(__file__).resolve(strict=True).parent
# path = (base_url / ".." / "data" / "simulacion_estudiantes.csv").resolve()  
# output_dir = (base_url / ".." / "outputs").resolve()

# Llamamos a la generación de recomendaciones en bloque
# generate_all_recommendations(path, output_dir)