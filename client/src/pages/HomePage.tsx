import Hero from "@/components/Hero";
import { useAuth } from "@clerk/clerk-react";
import { Navigate } from "react-router";

/**
 * Página inicial de la aplicación.
 * @returns {JSX.element}
 */
const HomePage = () => {
  const { isSignedIn } = useAuth();

  if (isSignedIn) return <Navigate to="/consultoria" />;

  return <Hero />;
};

export default HomePage;
