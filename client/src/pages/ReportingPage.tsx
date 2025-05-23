import ChartContainer from "@/components/ChartContainer";
import Header from "@/components/Header";
import ReportingBanner from "@/components/ReportingBanner";
import { getStudentsList } from "@/services/students.services";
import { useAuth } from "@clerk/clerk-react";
import { useEffect, useState } from "react";

/**
 * Página de Reportería
 * @returns {JSX.Element}
 */
const ReportingPage = () => {
  const [students, setStudents] = useState<[]>([])
  const { getToken } = useAuth();

  useEffect(()=> {
    getToken().then((token) => {
      if (!token) {
        console.error("No se pudo obtener el token");
        return;
      }
  
      getStudentsList(token).then((students) => {
        setStudents(students)
      })
    });
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])
  return (
    <div className="flex flex-col justify-start items-center h-screen pt-20 px-5 overflow-x-hidden">
      <ReportingBanner students={students} />
      <Header
        title="Análisis con IA"
        description="Genera aquí el reporte del análisis de IA basado en los datos de los estudiantes."
        action={{
          name: "Generar reporte",
          onClick: () => {
            console.log("Generar reporte");
          },
        }}
      />
      <ChartContainer />
    </div>
  );
};

export default ReportingPage;
