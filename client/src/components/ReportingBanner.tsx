/**
 * Componente para mostrar un banner de reporte
 * @returns {JSX.Element}
 */
const ReportingBanner = () => {
  return (
    <div className="w-full max-w-4xl mx-10 bg-(--color-primary-light) rounded-lg p-5 mb-6">
      <h1 className="text-3xl text-black text-center font-bold">
        {30} Estudiantes añadidos
      </h1>
    </div>
  );
};

export default ReportingBanner;
