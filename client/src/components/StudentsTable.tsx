import { useState, useEffect } from "react";
import { useStudentsContext } from "@/hooks/useStudentsContext";
import StudentModal from "./StudentModal";
import type { StudentForm } from "@/interfaces/student-form";

/**
 * Componente tabla de estudiantes.
 * @description Este componente es la tabla de estudiantes que se muestra en la página de consultoría.
 * @returns {JSX.Element}
 */
const StudentsTable = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedStudent, setSelectedStudent] = useState<
    StudentForm | undefined
  >(undefined);
  const { students, submitUpdateStudent, loading } = useStudentsContext();

  // Nuevo: abrir el modal solo cuando selectedStudent cambia
  useEffect(() => {
    if (selectedStudent) {
      setIsOpen(true);
    }
  }, [selectedStudent]);

  const handleOpen = () => {
    setIsOpen(false);
    setSelectedStudent(undefined);
  };

  return (
    <div className="relative overflow-x-auto shadow-md sm:rounded-lg w-full max-w-4xl mt-6 mx-auto min-h-[50vh] max-h-[50vh]">
      <table className="min-w-[600px] w-full text-sm text-left rtl:text-right text-black">
        <thead className="text-xs text-white border border-(--color-primary) bg-(--color-primary)">
          <tr>
            <th scope="col" className="px-6 py-3">
              Nombre
            </th>
            <th scope="col" className="px-6 py-3">
              Curso
            </th>
            <th scope="col" className="px-6 py-3">
              Legajo
            </th>
            <th scope="col" className="px-6 py-3">
              Acción
            </th>
          </tr>
        </thead>
        <tbody>
          {loading ? (
            <tr>
              <td colSpan={4} className="text-center py-8">
                Cargando...
              </td>
            </tr>
          ) : students.length === 0 ? (
            <tr>
              <td colSpan={4} className="text-center py-8">
                No hay estudiantes.
              </td>
            </tr>
          ) : (
            students.map((student, index) => (
              <tr
                key={index}
                className="bg-white border border-(--color-primary)"
              >
                <th
                  scope="row"
                  className="px-6 py-4 font-bold text-black whitespace-nowrap"
                >
                  {student.nombre}
                </th>
                <td className="px-6 py-4">{`${student.grado}° ${student.seccion}`}</td>
                <td className="px-6 py-4 text-(--color-primary-dark)">
                  {student.legajo}
                </td>
                <td className="px-6 py-4">
                  <button
                    onClick={() => setSelectedStudent(student)}
                    className="font-medium text-(--color-primary) hover:underline"
                  >
                    Editar
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
      <StudentModal
        isOpen={isOpen}
        onClose={handleOpen}
        initialData={selectedStudent}
        onSubmit={submitUpdateStudent}
      />
    </div>
  );
};

export default StudentsTable;
