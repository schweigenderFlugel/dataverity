const OurServicePage = () => {
  return (
    <div className="flex flex-col justify-start items-center py-20 px-5 overflow-x-hidden">
      <div className="w-full max-w-4xl mx-10 bg-(--color-primary-light) rounded-lg p-5 mb-6">
        <h1 className="text-lg text-black text-center font-bold mb-3">
          ¿Necesitas visualizar tus datos de forma clara, profesional y
          efectiva?
        </h1>
        <p>
          Te presentamos nuestro servicio de generación de gráficas interactivas
          con <strong>Power Bi</strong>, ideal para convertir tus datos en
          decisiones inteligentes
        </p>
      </div>
      <iframe
        src="https://drive.google.com/file/d/1qMayW4YO0Zg7J5DCsERRA6ccgRqSWv0E/preview"
        width="640"
        height="480"
        allow="autoplay"
      ></iframe>
    </div>
  );
};

export default OurServicePage;
