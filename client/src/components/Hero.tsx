import SignInButton from "./SignInButton";

/**
 * Componente Hero para la página principal.
 * @returns {JSX.Element}
 */
const Hero = () => {
  return (
    <section className="bg-[url('/src/assets/bg-home.svg')] bg-cover bg-center min-h-screen relative isolate px-6 pt-14 lg:pt-0 lg:px-4">
      <div className="mx-auto max-w-2xl py-32 sm:py-48 lg:py-50">
        <div className="text-center">
          <h1 className="text-5xl font-bold tracking-tight text-balance text-(--color-black) sm:text-5xl">
            Inteligencia artificial al servicio de la educación
          </h1>
          <p className="mt-6 font-medium text-pretty text-(--color-primary) sm:text-xl/8">
            Analizamos factores críticos del entorno escolar y social para
            impulsar decisiones estratégicas basadas en evidencia confiable.
          </p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <button className="btn-primary">Solicitar Demo</button>
            <SignInButton hero />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
