import { ApiInstance } from "@/api/api";
import type { StudentForm } from "@/interfaces/student-form";

const createStudent = async (data: StudentForm, token: string) => {
  try {
    const response = await ApiInstance.post(
      `${import.meta.env.VITE_API_URL}/api/consultancy`,
      data,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    console.log("Respuesta del backend:", response.data);
    return response.data;
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
};

export { createStudent };
