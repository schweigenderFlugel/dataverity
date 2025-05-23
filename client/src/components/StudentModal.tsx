import { useState } from "react";
import {
  Description,
  Dialog,
  DialogPanel,
  DialogTitle,
} from "@headlessui/react";
import { defaultStudentData } from "@/utils/default-student-data";
import type { StudentForm } from "@/interfaces/student-form";

interface Props {
  isOpen: boolean;
  onClose: () => void;
  initialData?: StudentForm;
  onSubmit: (data: StudentForm) => void;
}

/**
 * Componente modal para agregar o editar un estudiante
 * @description Este componente se utiliza para mostrar un modal que permite al usuario agregar o editar la información de un estudiante.
 * @param {isOpen} - Indica si el modal está abierto o cerrado.
 * @param {onClose} - Función que se ejecuta al cerrar el modal.
 * @param {initialData} - Datos iniciales del estudiante (opcional).
 * @param {onSubmit} - Función que se ejecuta al enviar el formulario.
 * @returns
 */
const StudentModal: React.FC<Props> = ({
  isOpen,
  onClose,
  initialData,
  onSubmit,
}) => {
  const [formData, setFormData] = useState<StudentForm>(
    initialData ?? defaultStudentData
  );

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const target = e.target as HTMLInputElement;
    const { name, type, value } = target;
    const val =
      type === "checkbox"
        ? target.checked
        : type === "number"
        ? Number(value)
        : value;
    setFormData((prev) => ({ ...prev, [name]: val }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
    onClose();
  };

  return (
    <Dialog
      open={isOpen}
      onClose={onClose}
      className="fixed inset-0 z-100 overflow-y-auto"
    >
      <div className="flex items-center justify-center min-h-screen px-4">
        <DialogPanel className="w-full max-w-4xl m-2 p-6 bg-white rounded shadow-xl border border-(--color-primary)">
          <DialogTitle className="text-lg font-semibold">
            Agregar Estudiante
          </DialogTitle>
          <Description className="text-sm text-(--color-primary-dark)">
            Completa los datos del estudiante.
          </Description>
          <form
            onSubmit={handleSubmit}
            className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4"
          >
            {/* Legajo */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Legajo</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Número de identificación del estudiante.
              </p>
              <input
                name="legajo"
                value={formData.legajo}
                onChange={handleChange}
                className="input"
                placeholder="Legajo"
                required
              />
            </div>

            {/* Nombre */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Nombre</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nombre completo del estudiante.
              </p>
              <input
                name="nombre"
                value={formData.nombre}
                onChange={handleChange}
                className="input"
                placeholder="Nombre"
                required
              />
            </div>

            {/* Edad */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Edad</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Edad del estudiante (5 a 13 años).
              </p>
              <input
                name="edad"
                type="number"
                value={formData.edad}
                onChange={handleChange}
                className="input"
                placeholder="Edad"
                min={5}
                max={13}
                required
              />
            </div>

            {/* Género */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Género</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Seleccione el género del estudiante.
              </p>
              <select
                name="genero"
                value={formData.genero}
                onChange={handleChange}
                className="input"
              >
                <option value="M">Masculino</option>
                <option value="F">Femenino</option>
              </select>
            </div>

            {/* Grado */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Grado</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Grado escolar actual (1 a 6).
              </p>
              <input
                name="grado"
                type="number"
                value={formData.grado}
                onChange={handleChange}
                className="input"
                placeholder="Grado"
                min={1}
                max={6}
                required
              />
            </div>

            {/* Sección */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Sección</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Seleccione la sección del grado.
              </p>
              <select
                name="seccion"
                value={formData.seccion}
                onChange={handleChange}
                className="input"
              >
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
              </select>
            </div>

            {/* Asistencia inicial */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Asistencia inicial</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿El estudiante asistió al inicio del ciclo?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="asistencia_inicial"
                  checked={formData.asistencia_inicial}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Asistencia (%) */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Asistencia (%)</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Porcentaje de asistencia total.
              </p>
              <input
                name="asistencia"
                type="number"
                value={formData.asistencia}
                onChange={handleChange}
                className="input"
                placeholder="Asistencia (%)"
                min={0}
                max={100}
                required
              />
            </div>

            {/* Calificación Matemática */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Calificación en Matemática
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nota obtenida en Matemática (0 a 10).
              </p>
              <input
                name="calificacion_matematica"
                type="number"
                value={formData.calificacion_matematica}
                onChange={handleChange}
                className="input"
                placeholder="Matemática"
                min={0}
                max={10}
                required
              />
            </div>

            {/* Calificación Lengua */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Calificación en Lengua</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nota obtenida en Lengua (0 a 10).
              </p>
              <input
                name="calificacion_lengua"
                type="number"
                value={formData.calificacion_lengua}
                onChange={handleChange}
                className="input"
                placeholder="Lengua"
                min={0}
                max={10}
                required
              />
            </div>

            {/* Horas clase semanales */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Horas de clase semanales</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Cantidad de horas de clase por semana.
              </p>
              <input
                name="horas_clase_semanales"
                type="number"
                value={formData.horas_clase_semanales}
                onChange={handleChange}
                className="input"
                placeholder="Horas semanales"
                required
              />
            </div>

            {/* Motivación */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Motivación</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nivel de motivación (1 a 5).
              </p>
              <input
                name="motivacion"
                type="number"
                value={formData.motivacion}
                onChange={handleChange}
                className="input"
                placeholder="Motivación"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Habilidades de autorregulación */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Habilidades de autorregulación
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nivel de autorregulación (1 a 5).
              </p>
              <input
                name="habilidades_de_autorregulacion"
                type="number"
                value={formData.habilidades_de_autorregulacion}
                onChange={handleChange}
                className="input"
                placeholder="Autorregulación"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Habilidades interpersonales */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Habilidades interpersonales
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nivel de habilidades interpersonales (1 a 5).
              </p>
              <input
                name="habilidades_interpersonales"
                type="number"
                value={formData.habilidades_interpersonales}
                onChange={handleChange}
                className="input"
                placeholder="Interpersonales"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Habilidades intrapersonales */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Habilidades intrapersonales
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nivel de habilidades intrapersonales (1 a 5).
              </p>
              <input
                name="habilidades_intrapersonales"
                type="number"
                value={formData.habilidades_intrapersonales}
                onChange={handleChange}
                className="input"
                placeholder="Intrapersonales"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Conducta de riesgo */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Conducta de riesgo</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nivel de conducta de riesgo (1 a 5).
              </p>
              <input
                name="conducta_riesgo"
                type="number"
                value={formData.conducta_riesgo}
                onChange={handleChange}
                className="input"
                placeholder="Conducta Riesgo"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Libros en casa */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Libros en casa</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿El estudiante tiene libros en casa?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="libros_en_casa"
                  checked={formData.libros_en_casa}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Internet en casa */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Internet en casa</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿El estudiante tiene acceso a internet en casa?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="internet_en_casa"
                  checked={formData.internet_en_casa}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Distancia a la escuela */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Distancia a la escuela (km)
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Distancia desde la casa a la escuela en kilómetros.
              </p>
              <input
                name="distancia_escuela_km"
                type="number"
                value={formData.distancia_escuela_km}
                onChange={handleChange}
                className="input"
                placeholder="Distancia (km)"
                step="0.01"
                required
              />
            </div>

            {/* Clima escolar */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Clima escolar</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Percepción del clima escolar (1 a 5).
              </p>
              <input
                name="clima_escolar"
                type="number"
                value={formData.clima_escolar}
                onChange={handleChange}
                className="input"
                placeholder="Clima escolar"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Capacitación docente anual */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Capacitación docente anual (horas)
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Horas de capacitación docente recibidas al año.
              </p>
              <input
                name="capacitacion_docente_anual_horas"
                type="number"
                value={formData.capacitacion_docente_anual_horas}
                onChange={handleChange}
                className="input"
                placeholder="Capacitación docente (hrs)"
                required
              />
            </div>

            {/* Tenencia director */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">
                Años del director en la escuela
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                Cantidad de años que el director lleva en la escuela.
              </p>
              <input
                name="tenencia_director_anos"
                type="number"
                value={formData.tenencia_director_anos}
                onChange={handleChange}
                className="input"
                placeholder="Años director"
                required
              />
            </div>

            {/* Adecuaciones curriculares */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Adecuaciones curriculares</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿El estudiante tiene adecuaciones curriculares?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="adecuaciones_curriculares"
                  checked={formData.adecuaciones_curriculares}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Tipo NEAE */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Tipo de NEAE</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Seleccione el tipo de necesidad educativa especial asociada.
              </p>
              <select
                name="tipo_neae"
                value={formData.tipo_neae}
                onChange={handleChange}
                className="input"
              >
                <option value="TDAH">TDAH</option>
                <option value="TEA">TEA</option>
                <option value="Dislexia">Dislexia</option>
                <option value="Normal">Normal</option>
              </select>
            </div>

            {/* Violencia familiar */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Violencia familiar</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿El estudiante ha experimentado violencia familiar?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="violencia_familiar"
                  checked={formData.violencia_familiar}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Enfermedad grave familiar */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Enfermedad grave familiar</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿Hay enfermedad grave en la familia?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="enfermedad_grave_familiar"
                  checked={formData.enfermedad_grave_familiar}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Catástrofe familiar */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">Catástrofe familiar</label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿El estudiante ha vivido una catástrofe familiar?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="catastrofe_familiar"
                  checked={formData.catastrofe_familiar}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            {/* Resiliencia familiar */}
            <div className="mb-6 col-span-1">
              <label className="font-semibold">Resiliencia familiar</label>
              <p className="text-xs text-(--color-primary) mb-1">
                Nivel de resiliencia familiar (1 a 5).
              </p>
              <input
                name="resiliencia_familiar"
                type="number"
                value={formData.resiliencia_familiar}
                onChange={handleChange}
                className="input"
                placeholder="Resiliencia familiar"
                min={1}
                max={5}
                required
              />
            </div>

            {/* Conducta de riesgo observada */}
            <div className="mb-6 col-span-1 flex flex-col">
              <label className="font-semibold">
                Conducta de riesgo observada
              </label>
              <p className="text-xs text-(--color-primary) mb-1">
                ¿Se ha observado conducta de riesgo en el estudiante?
              </p>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="conducta_riesgo_observada"
                  checked={formData.conducta_riesgo_observada}
                  onChange={handleChange}
                />
                <span className="ml-2">Sí</span>
              </label>
            </div>

            <div className="col-span-full flex justify-end gap-2 mt-4">
              <button
                type="button"
                onClick={onClose}
                className="btn-secondary px-4 py-2 rounded"
              >
                Cancelar
              </button>
              <button
                type="submit"
                className="btn-primary text-white px-4 py-2 rounded"
              >
                Guardar
              </button>
            </div>
          </form>
        </DialogPanel>
      </div>
    </Dialog>
  );
};

export default StudentModal;
