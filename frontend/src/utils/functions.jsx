import axios, { spread } from "axios";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";

export default async function makeRequest (url, method = "POST", data = {}, headers = {}) {
  try {
    const response = await axios({
      url,
      method,
      data,
      headers: headers,
      timeout: 20000,
    });

    return response

  } catch (error) {
    throw error
  }
};

export const useRequest = () => {
  const { authTokens, logoutUser, refreshTokens } = useContext(AuthContext);
  const navigate = useNavigate();

  const sendRequest = async (url, method = "POST", data = {}, headers = {}) => {

    const getAuthHeaders = () => {
      const currentTokens = JSON.parse(localStorage.getItem("authTokens"));
      return currentTokens
      ? { ...headers, Authorization: `Bearer ${currentTokens.access}` }
      : headers;
    };

    try {
      const authHeaders = getAuthHeaders();
      return await makeRequest(url, method, data, authHeaders);

    } catch (error) {
      if (error.response.status === 401 && refreshTokens) {
        console.log("Access токен истек. Пробуем обновить ...")
  
        try {
          await refreshTokens()
  
          const updatedHeaders = getAuthHeaders();
          console.log("updatedHeaders", updatedHeaders)

          return await makeRequest(url, method, data, updatedHeaders)
  
        } catch (error) {
          console.error("Ошибка обновления токенов:", error);
  
          if (error.response.status === 401) {
            console.log("Статус-код 401 Unauthorized. Выполняется разлогин пользователя")
            logoutUser()
            navigate("/login")
          }
          throw error;
        }

      } else {
        console.error("Ошибка выполнения запроса:", error);
        throw error;
      }
    }
  }
  return { sendRequest }
}
