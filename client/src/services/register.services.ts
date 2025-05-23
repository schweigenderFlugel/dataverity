import { ApiInstance } from "@/api/api";

const register = async (token: string) => {
  try {
    const response = await ApiInstance.get("/auth", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (err) {
    console.error("Error:", err);
    throw err;
  }
};

export { register };
