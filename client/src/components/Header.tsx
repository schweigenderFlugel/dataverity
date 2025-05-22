interface HeaderProps {
  title: string;
  description: string;
  action: {
    name: string;
    onClick: () => void;
  };
}

/**
 * Componente Header
 * @description Este componente es el header de la página de consultoría y reportería.
 * @param {title} string - Titulo del header
 * @param {description} string - Descripción del header
 * @param {action} object - Objeto que contiene el nombre y la función a ejecutar al hacer click
 * @param {action.name} string - Nombre de la acción
 * @param {action.onClick} function - Función a ejecutar al hacer click
 * @returns
 */
const Header: React.FC<HeaderProps> = ({ title, description, action }) => {
  return (
    <div className="w-full max-w-4xl mx-10">
      <h1 className="text-3xl font-bold">{title}</h1>
      <div className="flex justify-between items-center gap-6">
        <p className="font-small font-bold text-(--color-primary)">
          {description}
        </p>
        <button className="btn-primary" onClick={action.onClick}>
          {action.name}
        </button>
      </div>
    </div>
  );
};

export default Header;
