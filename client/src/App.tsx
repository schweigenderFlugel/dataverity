import "./App.css";
import { BrowserRouter } from "react-router";
import AppRoutes from "./router/routes";
import { StudentsProvider } from "./context/StudentsContext";
import { ToastContainer } from "react-toastify";

/**
 * Componente principal de la aplicación
 * @returns {JSX.Element}
 */
function App() {
  return (
    <BrowserRouter>
      <StudentsProvider>
        <AppRoutes />
        <ToastContainer />
      </StudentsProvider>
    </BrowserRouter>
  );
}

export default App;
