import type { Reports } from "@/interfaces/reports";
import { getStudentsListToCsv } from "@/services/students.services";
import { useAuth } from "@clerk/clerk-react";

/**
 * Componente contenedor para el gráfico.
 * @description Este componente es el contenedor del gráfico que se muestra en la página de reportería. Aquí se pueden mostrar los gráficos generados por la IA.
 * @returns {JSX.Element}
 */
const ChartContainer = ({ reports }: { reports: Reports[] }) => {
  const { getToken } = useAuth();

  const downloadCsv = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault()
    getToken().then((token) => {
      if (!token) {
        console.error("No se pudo obtener el token");
        return;
      }
      getStudentsListToCsv(token)
    });
  }
  return (
    <div className="w-full max-w-4xl mx-10 bg-white border border-(--color-primary) rounded-lg my-6 overflow-y-scroll">
      <button
        onClick={downloadCsv}
        className="flex items-center text-xs font-bold cursor-pointer"
      >
        Descarga el archivo CSV
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="currentColor"
          className="size-6"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
          />
        </svg>
      </button>
      <div className="flex items-center justify-end p-2">
        <div className="max-w-max bg-(--color-secondary) rounded-lg p-2 space-y-2">
          {reports.map((report, index) => (
            <div key={index}>
              <p className="font-bold text-2xl">{report.nombre}</p>
              <p className="font-bold text-[16px]">{report.grado}° {report.seccion}</p>
              <div className="font-bold text-[16px]">Recomendaciones:</div>
              <ul>
              {report.recomendaciones.split("|").map((recommendation, index) => (
                <li key={index}>{recommendation}</li>
              ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ChartContainer;
