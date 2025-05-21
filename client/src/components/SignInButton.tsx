import { useClerk } from "@clerk/clerk-react";

/**
 * Componente de botón de inicio de sesión.
 * @description Este componente es un botón que al hacer clic abre el modal de inicio de sesión de Clerk.
 * @returns {JSX.Element}
 */
const SignInButton = () => {
  const clerk = useClerk();

  return (
    <button
      onClick={() => clerk.openSignIn({ fallbackRedirectUrl: "/consultoria" })}
      className="btn-primary"
    >
      Inicia gratis
    </button>
  );
};

export default SignInButton;
