import Hero from "@/components/Hero";
import NavBar from "@/components/NavBar";

/**
 * Página inicial de la aplicación.
 * @returns {JSX.element}
 */
const HomePage = () => {
  return (
    <div className="font-poppins">
      <NavBar />
      <Hero />
    </div>
  );
};

export default HomePage;
