import { Route, Routes } from "react-router";
import HomePage from "@pages/HomePage";
import ProtectedRoute from "@/components/ProtectedRoute";
import ConsultancyPage from "@/pages/ConsultancyPage";
import ReportingPage from "@/pages/ReportingPage";
import { useEffect } from "react";
import { useNavigate } from "react-router";
import { useUser } from "@clerk/clerk-react";

/**
 * Componente de rutas de la aplicación.
 */
const AppRoutes = () => {
  const { isSignedIn } = useUser();
  const navigate = useNavigate();

  useEffect(() => {
    if (isSignedIn) {
      navigate("/", { replace: true });
    }
  }, [isSignedIn, navigate]);

  return (
    <Routes>
      <Route element={<ProtectedRoute />}>
        <Route path="/" element={<ConsultancyPage />} />
        <Route path="reporte" element={<ReportingPage />} />
      </Route>
      <Route path="home" element={<HomePage />} />
      <Route path="*" element={<HomePage />} />
    </Routes>
  );
};

export default AppRoutes;
