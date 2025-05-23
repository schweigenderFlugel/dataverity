# Generador de Datos Simulados de Estudiantes

Este script, `info_gen.py`, genera un archivo CSV (`simulacion_estudiantes.csv`) con datos sintéticos de estudiantes de educación primaria. El propósito principal es facilitar análisis exploratorios, pruebas de modelos de machine learning o prototipos de sistemas educativos, sin comprometer datos reales.

## 📁 Estructura del Proyecto

```
.
├── info_gen.py                # Script generador de los datos
├── nombres.txt               # Lista de nombres masculinos y femeninos
└── simulacion_estudiantes.csv # Archivo generado con los datos simulados
```

## 🔧 Requisitos

* Python 3.x
* Pandas

Instalación de dependencias:

```bash
pip install pandas
```

## ▶️ Ejecución

El script puede ejecutarse directamente desde la terminal:

```bash
python info_gen.py
```

> Asegúrate de tener un archivo `nombres.txt` en el mismo directorio, con el siguiente formato:
>
> ```
> # Masculinos
> Juan
> Pedro
> ...
> # Femeninos
> Ana
> María
> ...
> ```

## 📊 Datos Generados

Se generan 540 estudiantes con las siguientes características:

* **Identificación**: ID y legajo únicos
* **Demográficos**: Nombre, edad (6 a 11 años), género (M/F), grado (1° a 6°) y sección (A/B/C)
* **Académicos**: Asistencia (%), calificaciones en matemática y lengua, horas de clase semanales
* **Socioemocionales**: Motivación, habilidades socioemocionales, conducta de riesgo, resiliencia familiar
* **Condiciones del hogar**: Acceso a internet, libros en casa, distancia a la escuela
* **Entorno escolar**: Clima escolar, capacitación docente, antigüedad del director
* **Vulnerabilidades**: Presencia de NEAE, adecuaciones curriculares, eventos familiares adversos

## 🧪 Aplicaciones

* Visualización y análisis estadístico
* Entrenamiento y prueba de modelos predictivos educativos
* Validación de herramientas de visualización de datos
* Prototipado de dashboards educativos

## 📝 Notas

* Los datos son completamente sintéticos y no representan a personas reales.
* El archivo CSV se guarda en la misma ruta donde está ubicado el script (puedes modificar esta ruta directamente en el script si es necesario).