import { Route, Routes } from "react-router";
import HomePage from "@pages/HomePage";
import ProtectedRoute from "@/components/ProtectedRoute";
import LoginPage from "@/pages/LoginPage";

/**
 * Componente de rutas de la aplicación.
 */
const AppRoutes = () => {
  return (
    <Routes>
      <Route element={<ProtectedRoute />}>
        <Route path="/" element={<HomePage />}></Route>
      </Route>
      <Route path="iniciar" element={<LoginPage />} />
      <Route path="*" element={<LoginPage />} />
    </Routes>
  );
};

export default AppRoutes;
