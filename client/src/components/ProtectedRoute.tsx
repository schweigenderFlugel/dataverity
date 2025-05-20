import { Navigate, Outlet } from "react-router";
import Loading from "@components/Loading";
import { useAuth } from "@clerk/clerk-react";

/**
 * Componente que protege las rutas
 * @returns {JSX.Element}
 * @description Componente que protege las rutas, si el usuario no está autenticado lo redirige a la página de inicio de sesión
 */
const ProtectedRoute = () => {
  const { isSignedIn, isLoaded } = useAuth();

  if (!isLoaded) return <Loading />;
  if (isSignedIn) return <Navigate to="/iniciar" />;

  return <Outlet />;
};

export default ProtectedRoute;
