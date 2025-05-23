import type { StudentForm } from "@/interfaces/student-form";
import { register } from "@/services/register.services";
import {
  createStudent,
  getStudentsList,
  updateStudent,
} from "@/services/students.services";
import { useAuth } from "@clerk/clerk-react";
import { createContext, useEffect, useState, type ReactNode } from "react";

interface StudentsContextType {
  students: StudentForm[] | [];
  fetchStudents: () => void;
  submitCreateStudent: (data: StudentForm) => void;
  submitUpdateStudent: (data: StudentForm) => void;
}

const StudentsContext = createContext<StudentsContextType | undefined>(
  undefined
);

export const StudentsProvider = ({ children }: { children: ReactNode }) => {
  const [students, setStudents] = useState<StudentForm[] | []>([]);
  const { getToken } = useAuth();

  // Función auxiliar para obtener el token y ejecutar una acción
  const withToken = async (action: (token: string) => void) => {
    const token = await getToken();
    if (!token) {
      console.error("No se pudo obtener el token");
      return;
    }
    action(token);
  };

  const fetchStudents = () => {
    withToken((token) => {
      register(token).then(() => {
        getStudentsList(token).then((students) => {
          setStudents(students);
        });
      });
    });
  };

  const submitCreateStudent = (data: StudentForm) => {
    withToken((token) => {
      createStudent(data, token);
    });
  };

  const submitUpdateStudent = (data: StudentForm) => {
    withToken((token) => {
      updateStudent(data, token);
    });
  };

  useEffect(() => {
    fetchStudents()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <StudentsContext.Provider
      value={{
        students,
        fetchStudents,
        submitCreateStudent,
        submitUpdateStudent,
      }}
    >
      {children}
    </StudentsContext.Provider>
  );
};

export default StudentsContext;
