import { Route, Routes, Navigate } from "react-router";
import MainLayout from "@/layouts/MainLayout";
import HomePage from "@pages/HomePage";
import ProtectedRoute from "@/components/ProtectedRoute";
import ConsultancyPage from "@/pages/ConsultancyPage";
import ReportingPage from "@/pages/ReportingPage";
import LoadingPage from "@/pages/LoadingPage";
import NotFoundPage from "@/pages/NotFoundPage";
import { useAuth } from "@clerk/clerk-react";

/**
 * Componente de rutas de la aplicación.
 */
const AppRoutes = () => {
  const { isLoaded } = useAuth();

  if (!isLoaded) return <LoadingPage />;

  return (
    <Routes>
      <Route path="/" element={<MainLayout />}>
        <Route element={<ProtectedRoute />}>
          {/* Redirección automática al loguearse */}
          <Route index element={<Navigate to="/consultoria" replace />} />
          <Route path="consultoria" element={<ConsultancyPage />} />
          <Route path="reportes" element={<ReportingPage />} />
        </Route>
        <Route path="home" element={<HomePage />} />
      </Route>
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
};

export default AppRoutes;
