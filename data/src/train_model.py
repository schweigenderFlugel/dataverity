import os
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from preprocess import build_preprocessor

def load_data(data_path: str) -> pd.DataFrame:
    return pd.read_csv(data_path)

def train_random_forest(data_path: str, output_dir: str, target_col: str = 'calificacion_matematica'):
    # 1. Cargar datos
    df = load_data(data_path)

    # 2. Separar X e y
    y = df[target_col]
    # Creamos un DataFrame que ya NO incluye el target
    df_sin_target = df.drop(columns=[target_col, 'id_estudiante', 'legajo', 'nombre'], errors='ignore')

    # 3. Dividir en train/test
    X_train, X_test, y_train, y_test = train_test_split(
        df_sin_target, y, test_size=0.2, random_state=42
    )

    # 4. Construir el preprocesador sobre df_sin_target
    preprocessor, num_cols, cat_cols = build_preprocessor(df_sin_target)

    # 5. Crear Pipeline
    pipeline = Pipeline([
        ('preproc', preprocessor),
        ('reg', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # 6. Entrenar el modelo
    pipeline.fit(X_train, y_train)

    # 7. Predecir y evaluar
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # 8. Guardar métricas
    os.makedirs(output_dir, exist_ok=True)
    metrics_df = pd.DataFrame({
        'target': [target_col],
        'mse': [mse],
        'r2': [r2]
    })
    metrics_df.to_csv(os.path.join(output_dir, f'metricas_{target_col}.csv'), index=False)

    # 9. Guardar el modelo entrenado
    model_path = os.path.join(output_dir, f'random_forest_{target_col}.joblib')
    joblib.dump(pipeline, model_path)
    print(f"Modelo para '{target_col}' guardado en: {model_path}")

    return pipeline, num_cols, cat_cols

if __name__ == '__main__':
    data_path = os.path.join('..', 'data', 'simulacion_estudiantes.csv')
    output_dir = os.path.join('..', 'outputs')

    # Entrenar para Matemática
    train_random_forest(data_path, output_dir, target_col='calificacion_matematica')

    # Entrenar para Lengua
    train_random_forest(data_path, output_dir, target_col='calificacion_lengua')