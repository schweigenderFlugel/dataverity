import ChartContainer from "@/components/ChartContainer";
import Header from "@/components/Header";
import ReportingBanner from "@/components/ReportingBanner";
import { useAuth } from "@clerk/clerk-react";
import { generateReport } from "@/services/students.services";
import { useState } from "react";
import type { Reports } from "@/interfaces/reports";

/**
 * Página de Reportería
 * @returns {JSX.Element}
 */
const ReportingPage = () => {
  const [reports, setReports] = useState<Reports[]>([])
  const { getToken } = useAuth()

  const getReport = (e: React.MouseEvent<HTMLButtonElement>) => {
      e.preventDefault()
      getToken().then(async (token) => {
        if (!token) {
          console.error("No se pudo obtener el token");
          return;
        }
        const reports = await generateReport(token) as unknown as [];
        setReports(reports as unknown as Reports[])
      });
    }

  return (
    <div className="flex flex-col justify-start items-center h-screen pt-20 px-5 overflow-x-hidden">
      <ReportingBanner />
      <Header
        title="Análisis con IA"
        description="Genera aquí el reporte del análisis de IA basado en los datos de los estudiantes."
        action={{
          name: "Generar reporte",
          onClick: getReport,
        }}
      />
      <ChartContainer reports={reports} />
    </div>
  );
};

export default ReportingPage;
