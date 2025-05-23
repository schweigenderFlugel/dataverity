# src/preprocess.py

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data(path_csv: str) -> pd.DataFrame:
    """
    Carga el CSV con la simulación de estudiantes.
    """
    df = pd.read_csv(path_csv)
    return df

def build_preprocessor(df: pd.DataFrame):
    """
    Construye un ColumnTransformer para imputar, escalar y codificar columnas.
    Ahora filtra internamente aquellas columnas que no están presentes (por ejemplo la target),
    de modo que no levante error cuando se le pase un DataFrame sin 'calificacion_matematica' o sin 'calificacion_lengua'.
    """

    # --- 1) Definir la lista “completa” de posibles columnas numéricas ---
    todas_num_cols = [
        'edad', 'grado', 'asistencia', 'calificacion_lengua', 'calificacion_matematica',
        'horas_clase_semanales', 'motivacion', 'habilidades_de_autorregulacion',
        'habilidades_interpersonales', 'habilidades_intrapersonales', 'conducta_riesgo',
        'distancia_escuela_km', 'clima_escolar', 'capacitacion_docente_anual_horas',
        'tenencia_director_anos', 'resiliencia_familiar'
    ]

    # Filtramos solo las que realmente existen en df.columns
    # Así, si el DataFrame que llega no tiene 'calificacion_matematica', no la incluirá en num_cols
    num_cols = [c for c in todas_num_cols if c in df.columns]

    # --- 2) Definir la lista “completa” de posibles columnas categóricas ---
    todas_cat_cols = [
        'genero', 'seccion', 'asistencia_inicial', 'libros_en_casa', 'internet_en_casa',
        'adecuaciones_curriculares', 'tipo_neae', 'violencia_familiar',
        'enfermedad_grave_familiar', 'catastrofe_familiar', 'conducta_riesgo_observada'
    ]

    # Filtramos solo las que realmente existen en df.columns
    cat_cols = [c for c in todas_cat_cols if c in df.columns]


    # --- 3) Imputadores y transformadores ---
    imputador_num = SimpleImputer(strategy='mean')
    imputador_cat = SimpleImputer(strategy='constant', fill_value='missing')
    scaler = StandardScaler()
    ohe = OneHotEncoder(handle_unknown='ignore')

    # Pipeline numérico: imputar + escalar
    numeric_pipeline = Pipeline([
        ('imputer', imputador_num),
        ('scaler', scaler)
    ])

    # Pipeline categórico: imputar + one-hot
    categorical_pipeline = Pipeline([
        ('imputer', imputador_cat),
        ('onehot', ohe)
    ])

    # --- 4) ColumnTransformer final ---
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, num_cols),
            ('cat', categorical_pipeline, cat_cols)
        ]
    )

    # --- 5) (Opcional) Verificación de columnas esenciales ---
    # Si hay alguna columna “importante” que no puede faltar (por ejemplo 'edad', 'grado', etc.),
    # podrías lanzar un error aquí. Pero ya no incluimos ni 'calificacion_matematica' ni 'calificacion_lengua'
    # en la validación estricta, porque sabemos que a veces entrenaremos sin ellas.
    #
    # Por ejemplo, si quieres asegurarte siempre de que al menos estén 'edad' y 'grado', podrías hacer:
    # 
    #    cols_essenciales = {'edad', 'grado', 'asistencia'}
    #    faltantes = cols_essenciales - set(df.columns)
    #    if faltantes:
    #        raise ValueError(f"Faltan columnas esenciales: {faltantes}")
    #
    # Pero en tu caso, no hace falta validar todo num_cols+cat_cols, porque filtramos antes.

    return preprocessor, num_cols, cat_cols