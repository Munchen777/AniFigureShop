import Header from "../components/Header";
import Footer from "../components/Footer";
import { ROOT_API } from "..";
import axios from "axios";
import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";


function Clock() {
  const [time, setTime] = useState(new Date())

  // Update the time every second
  useEffect(() => {
    const interval = setInterval(() => {
      setTime(new Date());
    }, 1000);

    // Clear the interval when the component unmounts
    return () => clearInterval(interval);
  }, []);

  // Extract the hours, minutes, and seconds from the current time
  const hours = time.getHours();
  const minutes = time.getMinutes();
  const seconds = time.getSeconds();

  // Format the time as a string
  const timeString = `${hours}:${minutes}:${seconds}`;

  return (
    <div>
      {/* Display the time string */}
      <h1>{timeString}</h1>
    </div>
  );
}


const rotateRefreshToken = async (url, method = "POST", data = {}, headers = {}) => {
  try {
    const response = await axios({
      url,
      method,
      data,
      headers,
      timeout: 20000
    });
    console.log(response)
    if (response.status === 200) {
      const newAccessToken = response.data.access;
      const newRefreshToken = response.data.refresh;

      // Сохраняем новые токены
      localStorage.setItem("access", newAccessToken);
      localStorage.setItem("refresh", newRefreshToken);
      // console.log("Установлены новые access и refresh токены: ", newAccessToken, newRefreshToken)
      return newAccessToken;
    }
  }
  catch (error) {
    // Если какая-то ошибка, то отправляем на Логин пэйдж
    console.log("Error while refreshing token:", error);
    return <Navigate to={ <LoginPage /> } />
  }
}


const makeRequest = async (url, method = "POST", data = {}, headers = {}) => {
  try {
    // Находим access token в localStorage
    const access_token = localStorage.getItem("access")
    console.log("Access token", access_token)
    // Если нашли токен, добавляем его в headers
    if (access_token) {
      headers = {
        ...headers,
        Authorization: `Bearer ${access_token}`
      }
    }
    // Делаем запрос
    const response = await axios({
      url,
      method,
      data,
      headers: headers,
      timeout: 20000
    });
    return response.data;
  // if get error check status code (perhaps token is invalid)
  } catch (error) {
    if (error.response && error.response.status === 401) {
      console.error("Token expired or invalid. Logging out...");
      // Удаляем access токен
      localStorage.removeItem("access");

      // Достаем текущий refresh токен
      const refresh_token = localStorage.getItem("refresh");
      console.log("refresh", refresh_token);

      try {
        if (refresh_token) {
          const newAccessToken = await rotateRefreshToken(`${ROOT_API}api/token/refresh/`, "POST", {
            "refresh": refresh_token
          });

          if (newAccessToken) {
            console.log("Получил новый access токен", newAccessToken)
            // return await makeRequest(url, method, data, headers); // Повторяем оригинальный запрос с новым токеном
            headers.Authorization = `Bearer ${newAccessToken}`
            const retryResponse = await axios({
              url,
              method,
              data,
              headers,
              timeout: 20000
            })
            // Возвращаем токены
            return retryResponse.data
          }
        }
      } catch (error) {
        console.log(error)
      }
    }
    throw error
    // console.error("Error while makeing post request:", error);
  }
};


export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isAuthenticated, setIsAuthentincated] = useState(false);

  useEffect(() => {
    const checkToken = async () => {
      const access_token = localStorage.getItem("access");

      if (access_token) {
        try {
          const result = await makeRequest(`${ROOT_API}api/login/`, "POST");

          if (result?.msg == "User is already authenticated") {
            setIsAuthentincated(true);
            console.log("User is authenticated. Message:", result.msg)

            if (result.token) {
              localStorage.setItem("access", result.token.access);
              localStorage.setItem("refresh", result.token.refresh);
              setIsAuthentincated(true);
            }
          }
          else { // Тест
            setIsAuthentincated(false)
          }
        } catch (error) {
          console.error("Error while making request:", error)
        }
      }
    };

    checkToken();
  }, [])

  const handleSubmit = async (event) => {
    event.preventDefault() // Предотвращаем перезагрузку страницы

    // Делаем запрос
    try {
      const result = await makeRequest(`${ROOT_API}api/login/`, "POST", {
        username,
        password,
      });

      if (result.msg) {
        setIsAuthentincated(true)
        console.log("User is authenticated. Message", result.msg)

        // Если пришли токены - сохраняем их в localStorage
        if (result.token) {
          localStorage.setItem("access", result.token.access);
          localStorage.setItem("refresh", result.token.refresh);
          setIsAuthentincated(true);
        }
      }
    } catch (error) {
      console.error("Error while making request:", error);
    }
  };

  return (
    <>
      <div className="flex justify-center items-center min-h-screen bg-gray-100">
        {isAuthenticated ? (
          // Пользователь аутентифицирован
          <>
            <Clock />
            <p>You're already logged in</p>
          </>
        ): (
          <form
          className="bg-white p-6 rounded-lg shadow-lg w-full max-w-sm"
          onSubmit={handleSubmit}
          method="post"
          >
            <div className="mb-4">
              <input
                type="text"
                value={username}
                name="username"
                placeholder="Email / Username"
                onChange={(event) => setUsername(event.target.value)}
              ></input>
            </div>

            <div className="mb-4">
              <input
                type="password"
                value={password}
                name="password"
                placeholder="Password"
                onChange={(event) => setPassword(event.target.value)}
              ></input>
            </div>

            <div>
              <button
              className="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600"
              type="submit"
              value={"Login"}
              onClick={ handleSubmit }
              >
                Login
              </button>
            </div>
          </form>
        )}
      </div>
    </>
  );
}
