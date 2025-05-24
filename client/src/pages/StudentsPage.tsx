import { useState } from "react";
import Header from "@/components/Header";
import StudentsTable from "@/components/StudentsTable";
import StudentModal from "@/components/StudentModal";
import { useStudentsContext } from "@/hooks/useStudentsContext";

/**
 * Pagina de estudiantes
 * @description Esta página es la que se muestra al usuario cuando inicia sesión.
 * @returns {JSX.Element}
 */
const StudentsPage = () => {
  const [isOpen, setIsOpen] = useState(false);
  const { submitCreateStudent } = useStudentsContext();

  const handleOpen = () => {
    setIsOpen((prev) => !prev);
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
      <StudentModal
        isOpen={isOpen}
        onClose={handleOpen}
        onSubmit={submitCreateStudent}
      />
    </div>
  );
};

export default StudentsPage;
