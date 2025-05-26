import axios from "axios";

export const ApiInstance = axios.create({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  baseURL: (window as any).__ENV__?.VITE_API_URL,
  headers: { "Content-Type": "application/json" },
});
