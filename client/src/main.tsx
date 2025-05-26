import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import { ClerkProvider } from "@clerk/clerk-react";
import { esES } from "./locales/clerk/es.ts";

// Importar la clave pública de Clerk desde las variables de entorno
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const PUBLISHABLE_KEY = (window as any).__ENV__?.VITE_CLERK_PUBLISHABLE_KEY;

if (!PUBLISHABLE_KEY) {
  throw new Error("Add your Clerk Publishable Key to the .env file");
}

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ClerkProvider
      publishableKey={PUBLISHABLE_KEY}
      afterSignOutUrl="/"
      localization={esES}
    >
      <App />
    </ClerkProvider>
  </StrictMode>
);
