/**
 * Componente contenedor para el gráfico.
 * @description Este componente es el contenedor del gráfico que se muestra en la página de reportería. Aquí se pueden mostrar los gráficos generados por la IA.
 * @returns {JSX.Element}
 */
const ChartContainer = () => {
  return (
    <div className="w-full max-w-4xl mx-10 h-[60vh] bg-white border border-(--color-primary) rounded-lg my-6">
      <div className="flex items-center justify-end p-2">
        <div className="max-w-max bg-(--color-secondary) rounded-lg p-2">
          <a
            href={"url del link de descarga"}
            className="flex items-center text-xs font-bold"
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
          </a>
        </div>
      </div>
    </div>
  );
};

export default ChartContainer;
