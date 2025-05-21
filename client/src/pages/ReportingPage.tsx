import Header from "@/components/Header";

/**
 * Página de Reportería
 * @returns {JSX.Element}
 */
const ReportingPage = () => {
  return (
    <div className="flex justify-center items-center h-screen">
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
    </div>
  );
};

export default ReportingPage;
