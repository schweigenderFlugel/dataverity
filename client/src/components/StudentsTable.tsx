const students = [
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
  {
    name: "John Doe",
    grade: "3° A",
    id: "67543817873",
  },
];

/**
 * Componente tabla de estudiantes.
 * @description Este componente es la tabla de estudiantes que se muestra en la página de consultoría.
 * @returns {JSX.Element}
 */
const StudentsTable = () => {
  return (
    <div className="relative overflow-x-auto shadow-md sm:rounded-lg w-full max-w-4xl mt-6 mx-auto max-h-[50vh]">
      <table className="min-w-[600px] w-full text-sm text-left rtl:text-right text-black">
        <thead className="text-xs text-white border border-(--color-primary) bg-(--color-primary)">
          <tr>
            <th scope="col" className="px-6 py-3">
              Nombre
            </th>
            <th scope="col" className="px-6 py-3">
              Curso
            </th>
            <th scope="col" className="px-6 py-3">
              ID
            </th>
            <th scope="col" className="px-6 py-3">
              Acción
            </th>
          </tr>
        </thead>
        <tbody>
          {students.map((student, index) => (
            <tr
              key={index}
              className="bg-white border border-(--color-primary)"
            >
              <th
                scope="row"
                className="px-6 py-4 font-bold text-black whitespace-nowrap"
              >
                {student.name}
              </th>
              <td className="px-6 py-4">{student.grade}</td>
              <td className="px-6 py-4 text-(--color-primary-dark)">
                {student.id}
              </td>
              <td className="px-6 py-4">
                <a
                  href="#"
                  className="font-medium text-(--color-primary) hover:underline"
                >
                  Editar
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StudentsTable;
