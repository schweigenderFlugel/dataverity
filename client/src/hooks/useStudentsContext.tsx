import StudentsContext from "@/context/StudentsContext";
import { useContext } from "react";

export const useStudentsContext = () => {
  const context = useContext(StudentsContext);
  if (!context) {
    throw new Error("useStudentsContext debe usarse con StudentsProvider");
  }
  return context;
};
