import Header from "@/components/Header";
import StudentsTable from "@/components/StudentsTable";

/**
 * Pagina de estudiantes
 * @description Esta página es la que se muestra al usuario cuando inicia sesión.
 * @returns {JSX.Element}
 */
const StudentsPage = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen overflow-x-hidden pt-20 px-5">
      <Header
        title="Estudiantes"
        description="Añade aquí los estudiantes para que la IA procece sus datos."
        action={{
          name: "Añadir estudiante",
          onClick: () => {
            console.log("Añadir Estudiante");
          },
        }}
      />
      <StudentsTable />
    </div>
  );
};

export default StudentsPage;
