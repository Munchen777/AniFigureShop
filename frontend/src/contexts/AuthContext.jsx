import axios from "axios";
import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import { ROOT_API } from "..";
import makeRequest from "../utils/functions";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  const [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );
  const [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwtDecode(localStorage.getItem("authTokens"))
      : null
  );
  const navigate = useNavigate();

  let loginUser = async (event) => {
    event.preventDefault();
    try {
      let response = await makeRequest(
      `${ROOT_API}/token/`,
      "POST",
      {
        email: event.target.username.value,
        password: event.target.password.value,
      },
    );

    let data = await response.data;

    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwtDecode(data.access));
      localStorage.setItem("authTokens", JSON.stringify(data));
      navigate("/");

    } else {
      alert("Something went wrong!");
    }

    } catch (error) {
        console.log(error)
    }
  };

  let registerUser = async (event) => {
    event.preventDefault();

    try {
      let response = await makeRequest(
        `${ROOT_API}/register/`,
        "POST",
        {
          email: event.target.email.value,
          password: event.target.password.value,
        }
      )
      console.log("Ответ:", response)

      if (response.status === 201) {
        navigate("/")
      }

    } catch (error) {
      console.log("Error while sending request to api/v1/register/ endpoint");
      console.log(error)
    }
  };

  let logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    navigate("/");
  };

  let refreshTokens = async () => {
    console.log("Обновляем токены ...")

    const authTokens = localStorage.getItem("authTokens");
    let refreshToken = JSON.parse(authTokens).refresh;

    const response = await axios({
      url: `${ROOT_API}/token/refresh/`,
      method: "POST",
      data: {
        "refresh": refreshToken
      },
    });

    let data = await response.data

    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwtDecode(data.access));
      localStorage.setItem("authTokens", JSON.stringify(data));
      console.log("Обновили токены")

    } else {
      logoutUser()
    }
  }

  let resetPassword = async (e) => {
    e.preventDefault();

    const email = e.target.email.value;
    console.log("Reset password")
    console.log(email)

    const response = await makeRequest(
      `${ROOT_API}/reset-password/`,
      "POST",
      {
        email: email,
      }
    )
    console.log("Ответ:", response)

    if (response.status === 200) {
      navigate("/reset-password-done")
    }
    else {
      alert("Something went wrong!")
    }
  }

  let contextData = {
    user: user,
    loginUser: loginUser,
    authTokens: authTokens,
    logoutUser: logoutUser,
    refreshTokens: refreshTokens,
    registerUser: registerUser,
    resetPassword: resetPassword,
  };

  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};
