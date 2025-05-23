import { ApiInstance } from "@/api/api";
import type { StudentForm } from "@/interfaces/student-form";

const createStudent = async (data: StudentForm, token: string) => {
  try {
    const response = await ApiInstance.post(
      "/consultancy",
      data,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
};

const updateStudent = async (data: StudentForm, token: string) => {
  try {
    const response = await ApiInstance.put(
      `/consultancy/${data.id_estudiante}`,
      data,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
};

const getStudentsList = async (token: string) => {
  try {
    const response = await ApiInstance.get(
      "/consultancy/list",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
}

const getStudentsListToCsv = async (token: string) => {
  try {
    const response = await ApiInstance.get(
      "/consultancy/list-to-csv",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        responseType: 'blob',
      }
    );

    const blob = new Blob([response.data], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'estudiantes.csv';
    document.body.appendChild(a);
    a.click();
    a.remove();
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
}

const generateReport = async (token: string) => {
  try {
    const response = await ApiInstance.get(
      "/consultancy/recommendations",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
}

export { createStudent, updateStudent, getStudentsList, getStudentsListToCsv, generateReport };
