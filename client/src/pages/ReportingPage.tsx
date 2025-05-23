import ChartContainer from "@/components/ChartContainer";
import Header from "@/components/Header";
import ReportingBanner from "@/components/ReportingBanner";

/**
 * Página de Reportería
 * @returns {JSX.Element}
 */
const ReportingPage = () => {

  return (
    <div className="flex flex-col justify-start items-center h-screen pt-20 px-5 overflow-x-hidden">
      <ReportingBanner />
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
