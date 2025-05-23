import type { StudentForm } from "@/interfaces/student-form";
import { register } from "@/services/register.services";
import {
  createStudent,
  getStudentsList,
  updateStudent,
} from "@/services/students.services";
import { useAuth } from "@clerk/clerk-react";
import { createContext, useEffect, useState, type ReactNode } from "react";
import { toast } from "react-toastify";

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
  const withToken = async (action: (token: string) => Promise<void> | void) => {
    const token = await getToken();
    if (!token) {
      toast.error("No se pudo obtener el token");
      return;
    }
    await action(token);
  };

  const fetchStudents = () => {
    withToken(async (token) => {
      try {
        await register(token);
        const students = await getStudentsList(token);
        setStudents(students);
      } catch (error) {
        toast.error("Error al obtener la lista de estudiantes");
        console.log(error);
      }
    });
  };

  useEffect(()=> {
    fetchStudents();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const submitCreateStudent = (data: StudentForm) => {
    withToken(async (token) => {
      try {
        await createStudent(data, token);
        toast.success("Estudiante creado correctamente");
        fetchStudents(); // Aquí se actualiza la lista
      } catch (error) {
        toast.error("Error al crear el estudiante");
        console.log(error);
      }
    });
  };

  const submitUpdateStudent = (data: StudentForm) => {
    withToken(async (token) => {
      try {
        await updateStudent(data, token);
        toast.success("Estudiante editado correctamente");
        fetchStudents(); // Aquí también se actualiza la lista
      } catch (error) {
        toast.error("Error al editar el estudiante");
        console.log(error);
      }
    });
  };

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
