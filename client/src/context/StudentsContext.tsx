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
  loading: boolean;
}

const StudentsContext = createContext<StudentsContextType | undefined>(
  undefined
);

export const StudentsProvider = ({ children }: { children: ReactNode }) => {
  const [students, setStudents] = useState<StudentForm[] | []>([]);
  const [loading, setLoading] = useState<boolean>(false); // <-- Estado loading
  const { getToken } = useAuth();

  // Función auxiliar para obtener el token y ejecutar una acción
  const withToken = async (action: (token: string) => Promise<void> | void) => {
    const token = await getToken();
    if (!token) {
      return;
    }
    await action(token);
  };

  const fetchStudents = () => {
    setLoading(true);
    withToken(async (token) => {
      try {
        await register(token);
        const students = await getStudentsList(token);
        setStudents(students);
      } catch (error) {
        toast.error("Error al obtener la lista de estudiantes");
        console.log(error);
      } finally {
        setLoading(false);
      }
    });
  };

  const submitCreateStudent = (data: StudentForm) => {
    withToken(async (token) => {
      try {
        await createStudent(data, token);
        toast.success("Estudiante creado correctamente");
      } catch (error) {
        toast.error("Error al crear el estudiante");
        console.log(error);
      } finally {
        fetchStudents();
      }
    });
  };

  const submitUpdateStudent = (data: StudentForm) => {
    withToken(async (token) => {
      try {
        await updateStudent(data, token);
        toast.success("Estudiante editado correctamente");
      } catch (error) {
        toast.error("Error al editar el estudiante");
        console.log(error);
      } finally {
        fetchStudents();
      }
    });
  };

  useEffect(() => {
    fetchStudents();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <StudentsContext.Provider
      value={{
        students,
        fetchStudents,
        submitCreateStudent,
        submitUpdateStudent,
        loading,
      }}
    >
      {children}
    </StudentsContext.Provider>
  );
};

export default StudentsContext;
