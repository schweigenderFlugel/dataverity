import "./App.css";
import { BrowserRouter } from "react-router";
import AppRoutes from "./router/routes";

function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;
