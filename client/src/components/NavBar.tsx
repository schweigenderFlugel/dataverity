import { useState } from "react";
import { Dialog, DialogPanel } from "@headlessui/react";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";
import logo from "@assets/dataverity-logo.svg";
import SignOutButton from "./SignOutButton";
import SignInButton from "./SignInButton";
import { useUser } from "@clerk/clerk-react";
import { NavLink } from "react-router";

/**
 * Componente de barra de navegación.
 * @returns {JSX.element}
 */
const NavBar = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const { isSignedIn } = useUser();

  const navigation = isSignedIn
    ? [
        { name: "Estudiantes", href: "/estudiantes" },
        { name: "Reportes", href: "/reportes" },
      ]
    : [
        { name: "Soluciones", href: "#" },
        { name: "Producto", href: "#" },
        { name: "Precios", href: "#" },
        { name: "Nosotros", href: "#" },
      ];

  return (
    <header className="absolute inset-x-0 top-0 z-50">
      <nav
        aria-label="Global"
        className="flex items-center justify-between p-6 lg:px-8"
      >
        <div className="flex items-center lg:flex-1 gap-x-8">
          <a href="#" className="-m-1.5 p-1.5">
            <span className="sr-only">Logo</span>
            <img alt="logo" src={logo} className="h-8 w-auto" />
          </a>
          <div className="hidden lg:flex lg:gap-x-12">
            {navigation.map((item) => (
              <NavLink
                key={item.name}
                to={item.href}
                className="text-sm/6 font-bold text-(--color-primary) hover:text-(--color-primary-dark)"
              >
                {item.name}
              </NavLink>
            ))}
          </div>
        </div>
        <div className="flex lg:hidden">
          <button
            type="button"
            onClick={() => setMobileMenuOpen(true)}
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          >
            <span className="sr-only">Abrir menú principal</span>
            <Bars3Icon aria-hidden="true" className="size-6" />
          </button>
        </div>
        <div className="hidden lg:flex lg:flex-1 lg:justify-end">
          {isSignedIn ? <SignOutButton /> : <SignInButton />}
        </div>
      </nav>
      <Dialog
        open={mobileMenuOpen}
        onClose={setMobileMenuOpen}
        className="lg:hidden"
      >
        <div className="fixed inset-0 z-50" />
        <DialogPanel className="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
          <div className="flex items-center justify-between">
            <a href="#" className="-m-1.5 p-1.5">
              <span className="sr-only">Logo</span>
              <img alt="logo" src={logo} className="h-8 w-auto" />
            </a>
            <button
              type="button"
              onClick={() => setMobileMenuOpen(false)}
              className="-m-2.5 rounded-md p-2.5 text-gray-700"
            >
              <span className="sr-only">Cerrar menú</span>
              <XMarkIcon aria-hidden="true" className="size-6" />
            </button>
          </div>
          <div className="mt-6 flow-root">
            <div className="-my-6 divide-y divide-gray-500/10">
              <div className="space-y-2 py-6">
                {navigation.map((item) => (
                  <NavLink
                    key={item.name}
                    to={item.href}
                    className="-mx-3 block rounded-lg px-3 py-2 text-base/7 font-bold text-(--color-primary) hover:bg-(--color-primary-light)"
                  >
                    {item.name}
                  </NavLink>
                ))}
              </div>
              <div className="py-6">
                {isSignedIn ? <SignOutButton /> : <SignInButton />}
              </div>
            </div>
          </div>
        </DialogPanel>
      </Dialog>
    </header>
  );
};

export default NavBar;
