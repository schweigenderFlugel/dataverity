import csv

with open('profiles1.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  field = [
    "id_estudiante", 
    "edad", 
    "genero", 
    "grado", 
    "asistencia_inicial", # Asistemcia inicial: si el estudiante estuvo en preescolar
    "asistencia", 
    "calificacion_matematica", 
    "calificacion_lengua", 
    "horas_clase_semanales", 
    "motivacion", 
    "habilidades_de_autoregulacion", 
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
    "tipo_neae", # Si tiene autismo, entre otras condiciones especiales
    "violencia_familiar",
    "enfermedad_grave_familiar",
    "catastrofe_familiar",
    "resilencia_familiar",
    "conducta_riesgo_observada",
  ]

  writer.writerow(field)
  writer.writerow(["Oladele Damilola", "40", "Nigeria"])
  writer.writerow(["Alina Hricko", "23", "Ukraine"])
  writer.writerow(["Isabel Walter", "50", "United Kingdom"])