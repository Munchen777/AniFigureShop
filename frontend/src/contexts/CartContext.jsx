import { createContext, useState, useEffect, useContext } from "react";
import { ROOT_API } from "..";
import AuthContext from "../contexts/AuthContext";
import { useRequest } from "../utils/functions";

const CartContext = createContext();

export default CartContext;

export const CartProvider = ({ children }) => {
  const { authTokens } = useContext(AuthContext);
  const { sendRequest } = useRequest();

  const [quantities, setQuantities] = useState({});
  const totalCount = Object.values(quantities).reduce((sum, qty) => sum + qty, 0);

  const handlePurchase = async (product, updatedQuantity) => {
    try {
      const response = await sendRequest(`${ROOT_API}/cart/update/`, "POST", {
        product: product,
        quantity: updatedQuantity,
      });
      console.log("Cart's been updated:", response);
    } catch (error) {
      console.log(
        "Error while making POST Request to cart/update endpoint",
        error
      );
    }
  };

  const handleBuyClick = async (product) => {
    setQuantities((prevQuantities) => {
      const updatedQuantity = (prevQuantities[product.pk] || 0) + 1;
      handlePurchase(product, updatedQuantity);
      return { ...prevQuantities, [product.pk]: updatedQuantity };
    });
  };

  const handleIncrement = async (product) => {
    setQuantities((prevQuantities) => {
      const updatedQuantity = (prevQuantities[product.pk] || 0) + 1;
      handlePurchase(product, updatedQuantity);
      return { ...prevQuantities, [product.pk]: updatedQuantity };
    });
  };

  const handleDecrement = async (product) => {
    setQuantities((prevQuantities) => {
      const updatedQuantity =
        (prevQuantities[product.pk] || 0) > 1
          ? prevQuantities[product.pk] - 1
          : 0;
      handlePurchase(product, updatedQuantity);
      return { ...prevQuantities, [product.pk]: updatedQuantity };
    });
  };

  const fetchCart = async () => {
    const headers = authTokens
      ? { Authorization: `Bearer ${authTokens.access}` }
      : {};
    try {
      // Запрос на получение корзины
      const cartResponse = await sendRequest(
        `${ROOT_API}/cart/get/`,
        "GET",
        {},
        headers
      );

      // Преобразование корзины в объект quantities
      const cartItems = cartResponse.data.cart;
      const initialQuantities = {};

      cartItems.forEach((item) => {
        if (item.product && item.product.pk) {
          initialQuantities[item.product.pk] = item.quantity;
        }
      });

      setQuantities(initialQuantities);
    } catch (error) {
      console.log("Error while fetching cart from /cart/get endpoint", error);
    }
  };

  let contextData = {
    quantities: quantities,
    totalCount: totalCount,
    handleBuyClick: handleBuyClick,
    handleIncrement: handleIncrement,
    handleDecrement: handleDecrement,
    fetchCart: fetchCart,
  };

  return (
    <CartContext.Provider value={contextData}>{children}</CartContext.Provider>
  );
};
