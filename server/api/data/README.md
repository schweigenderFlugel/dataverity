# Asesor de consultoría educativa Basada en IA

Este proyecto implementa un sistema basado en inteligencia artificial para analizar datos de estudiantes desde un archivo CSV y generar recomendaciones personalizadas orientadas a mejorar el rendimiento académico y bienestar estudiantil. Se enfoca en áreas clave como Matemática, Lengua, habilidades socioemocionales, contexto familiar y escolar, entre otros.

## 📁 Estructura del Proyecto

```

proyecto/
├── .IAenv/                          # Entorno virtual Python (no versionado)
├── data/
│   └── simulacion\_estudiantes.csv  # Archivo CSV de entrada con datos simulados de estudiantes
├── outputs/                         # Carpeta de salida para modelos y recomendaciones
├── REQUIREMENTS.txt                # Lista de dependencias del proyecto
├── src/
│   ├── preprocess.py               # Preprocesamiento de datos
│   ├── train\_model.py             # Entrenamiento de modelos de predicción
│   └── generate\_recommendations.py # Generación de recomendaciones personalizadas
└── README.md                       # Este archivo

````

## 🔍 Objetivo

El sistema tiene como meta procesar un dataset de estudiantes, entrenar modelos predictivos para el rendimiento académico (en Matemática y Lengua), y generar recomendaciones personalizadas por estudiante para apoyar su desarrollo.

## ⚙️ Requisitos

Antes de comenzar, asegúrate de tener un entorno virtual y ejecutar:

```bash
pip install -r REQUIREMENTS.txt
````

## 🚀 Ejecución del Proyecto

### 1. Entrenamiento de Modelos

Ejecuta el script para entrenar dos modelos `RandomForestRegressor`: uno para Matemática y otro para Lengua. Se generan modelos serializados (`.joblib`) y métricas (`.csv`):

```bash
cd src
python train_model.py
```

Esto generará los siguientes archivos en `outputs/`:

* `random_forest_calificacion_matematica.joblib`
* `random_forest_calificacion_lengua.joblib`
* `metricas_calificacion_matematica.csv`
* `metricas_calificacion_lengua.csv`

### 2. Generación de Recomendaciones

A partir del archivo CSV original y las variables disponibles, se genera un reporte personalizado para cada estudiante:

```bash
python generate_recommendations.py
```

Salida:

* `outputs/recomendaciones_personalizadas.csv`

Este archivo contiene columnas como:

* `id_estudiante`
* `nombre`
* `grado`
* `seccion`
* `recomendaciones`: texto detallado con sugerencias adaptadas al perfil del estudiante.

## 🧠 Lógica de Recomendaciones

El motor de recomendaciones analiza múltiples dimensiones, incluyendo pero no limitado a:

* Rendimiento en Matemática y Lengua
* Habilidades intrapersonales e interpersonales
* Motivación, clima escolar, distancia a la escuela
* Presencia de libros/internet en casa
* Situaciones familiares (violencia, enfermedad, catástrofe)
* Necesidades educativas especiales (NEAE)

Cada dimensión puede activar recomendaciones específicas, que se concatenan en un solo campo por estudiante.

## 📌 Notas

* La carpeta `.IAenv/` no debe ser versionada ni cargada en repositorios.
* El script de entrenamiento omite explícitamente columnas como `id_estudiante`, `nombre`, y `legajo` para evitar sesgos.
* El sistema es extensible a más variables y nuevos modelos si se desea integrar otras áreas de análisis.

## 📄 Licencia

MIT. Libre de uso con fines educativos y de mejora del aprendizaje automatizado.

---