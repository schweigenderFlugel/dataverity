import "./App.css";
import { BrowserRouter } from "react-router";
import AppRoutes from "./router/routes";

/**
 * Componente principal de la aplicación
 * @returns {JSX.Element}
 */
function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;
