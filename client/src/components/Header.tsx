interface HeaderProps {
  title: string;
  description: string;
  action: {
    name: string;
    onClick: () => void;
  };
}

const Header: React.FC<HeaderProps> = ({ title, description, action }) => {
  return (
      <div className="w-220 mx-10">
        <h1 className="text-3xl font-bold">{title}</h1>
        <div className="flex justify-between items-center gap-6">
          <p className="font-small font-bold text-(--color-primary)">{description}</p>
          <button className="btn-primary" onClick={action.onClick}>{action.name}</button>
        </div>
      </div>
  );
};

export default Header;
