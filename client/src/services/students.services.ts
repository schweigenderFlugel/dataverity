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
  console.log(data.id_estudiante)
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
        responseType: 'blob',
      }
    );
    const text = await response.data.text();

    const rows = text.split('\n').filter((row: string) => row.trim() !== '');
    const headers = rows[0].split(',');

    const json = rows.slice(1).map((row: string) => {
      const values = row.split(',');
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      return headers.reduce((acc: any, header: string, idx: any) => {
        acc[header.trim()] = values[idx]?.trim();
        return acc;
      }, {} as Record<string, string>);
    });
    return json
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
}

export { createStudent, updateStudent, getStudentsList, getStudentsListToCsv, generateReport };
