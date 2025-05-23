import { useState } from "react";
import Header from "@/components/Header";
import StudentsTable from "@/components/StudentsTable";
import StudentModal from "@/components/StudentModal";
import { createStudent } from "@/services/students.services";
import { useAuth } from "@clerk/clerk-react";
import type { StudentForm } from "@/interfaces/student-form";

/**
 * Pagina de estudiantes
 * @description Esta página es la que se muestra al usuario cuando inicia sesión.
 * @returns {JSX.Element}
 */
const StudentsPage = () => {
  const [isOpen, setIsOpen] = useState(false);
  const { getToken } = useAuth();

  const handleOpen = () => {
    setIsOpen((prev) => !prev);
  };

  const onSubmit = async (data: StudentForm) => {
    getToken().then((token) => {
      if (!token) {
        console.error("No se pudo obtener el token");
        return;
      }
      createStudent(data, token);
    });
  };

  return (
    <div className="flex flex-col justify-center items-center h-screen overflow-x-hidden pt-20 px-5">
      <Header
        title="Estudiantes"
        description="Añade aquí los estudiantes para que la IA procece sus datos."
        action={{
          name: "Añadir estudiante",
          onClick: handleOpen,
        }}
      />
      <StudentsTable />
      <StudentModal isOpen={isOpen} onClose={handleOpen} onSubmit={onSubmit} />
    </div>
  );
};

export default StudentsPage;
