import axios from "axios";
import React, { useState } from "react";
import { ROOT_API } from "..";
import 'bootstrap/dist/css/bootstrap.min.css'

const getCSRF = async () => {
  const response = await makeRequest(`${ROOT_API}csrf_cookie/`, "GET", {},
    {
      withCredentials: true
    }
  )
}

const makeRequest = async (url, method = "POST", data = {}, headers = {}) => {
  try {
    const response = await axios({
      url,
      method,
      data,
      headers: headers,
      timeout: 20000,
    });
    console.log(response);
  } catch (error) {
    console.log("Ошибка при отправке запроса");
  }
};

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const headers = {
      "X-CSRFToken": await getCSRF()
    }

    try {
      const result = await makeRequest(`${ROOT_API}api/login/`, "POST", {
        username,
        password,
      },
      headers
    );
      console.log(result.data);
    } catch (error) {
      console.log("Ошибка при отправке запроса:", error);
    }
  };

  return (
    <div className="container-fluid center position-absolute">
      <form method="post">
        <div className="mb-3 position-relative">
          <input
            type="text"
            value={username}
            name="username"
            placeholder="Email / Username"
            onChange={(event) => setUsername(event.target.value)}
            className="form-control"
          ></input>
        </div>

        <div className="mb-3 position-relative">
          <input
            type="password"
            value={password}
            name="password"
            placeholder="Password"
            onChange={(event) => setPassword(event.target.value)}
            className="form-control"
          ></input>
        </div>

        <div>
          <button className="btn btn-primary" type="submit" value={"Login"} onClick={handleSubmit}>
            Login
          </button>
        </div>
      </form>
    </div>
  );
}
