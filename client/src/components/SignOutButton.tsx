import { useAuth } from "@clerk/clerk-react";

/**
 * Componente de botón de cierre de sesión.
 * @returns {JSX.Element}
 */
const SignOutButton = () => {
  const { signOut } = useAuth();

  return (
    <button
      onClick={() => signOut({ redirectUrl: "/home" })}
      className="btn-secondary"
    >
      Cerrar sesión
    </button>
  );
};

export default SignOutButton;
