import React from "react";
import axios from "axios";

const baseURL = "http://localhost:8000/todos";

type Todo = {
  id: string;
  title: string;
  description: string;
  completed: boolean;
};

type PostBody = {
  title: string;
  description: string;
  completed: boolean;
};

const App = () => {
  const [todos, setTodos] = React.useState<Todo[]>([]);
  const [postBody, setPostBody] = React.useState<PostBody>({
    title: "",
    description: "",
    completed: false,
  });

  const getTodos = async () => {
    const response = await axios.get(baseURL);
    setTodos(response.data);
  };

  const postTodo = async () => {
    await axios.post(baseURL, postBody).then((response) => {
      setTodos([...todos, response.data]);
    });
  };

  const putTodo = async (todo: Todo) => {
    await axios
      .put(`${baseURL}/${todo.id}`, {
        ...todo,
        completed: !todo.completed,
      })
      .then((response) => {
        setTodos(
          todos.map((todo) =>
            todo.id === response.data.id ? response.data : todo
          )
        );
      });
  };

  const deleteTodo = async (todo: Todo) => {
    await axios.delete(`${baseURL}/${todo.id}`).then((response) => {
      setTodos(todos.filter((todo) => todo.id !== response.data.id));
    });
  };

  const handleChanges = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPostBody({ ...postBody, [e.target.name]: e.target.value });
  };

  React.useEffect(() => {
    getTodos();
  }, []);

  return (
    <div>
      <h1>Todo List</h1>
      <input
        name="title"
        value={postBody.title}
        onChange={handleChanges}
      /> <br />
      <input
        name="description"
        value={postBody.description}
        onChange={handleChanges}
      />{" "}
      <br />
      <button onClick={postTodo}>Submit</button>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => putTodo(todo)}
            />
            <span style={{ paddingRight: "2rem" }}>{todo.title}</span>
            <span style={{ paddingRight: "2rem" }}>{todo.description}</span>
            <button onClick={() => deleteTodo(todo)}>delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
