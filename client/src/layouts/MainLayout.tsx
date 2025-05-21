import NavBar from "@/components/NavBar";
import { Outlet } from "react-router";

const MainLayout = () => {
  return (
    <div className="bg-(--color-secondary) min-h-screen">
      <NavBar />
      <Outlet />
    </div>
  );
};

export default MainLayout;
