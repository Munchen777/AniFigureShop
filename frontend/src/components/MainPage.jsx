import { Component, useEffect, useState, useContext } from "react";
import { ROOT_API } from "../index";
import ProductCard from "./ProductCard";
import { useRequest } from "../utils/functions";
import { useCart } from "../contexts/CartContext";

const ProductsComponent = () => {
  const { sendRequest } = useRequest();
  const { fetchCart } = useCart();

  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Запрос на получение списка продуктов
        const productsResponse = await sendRequest(`${ROOT_API}/api/products/`, "GET");
        console.log("Ответ от эндпоинта /api/products/", productsResponse)
        setProducts(productsResponse.data.results);

        await fetchCart();

      } catch (error) {
        console.log(
          "Error while making POST Request to /api/products/ endpoint",
          error
        );
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container mx-auto">
      <div className="grid grid-cols-1 justify-evenly sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-6">
        {Array.isArray(products) &&
          products.map((product) => (
            <ProductCard key={product.pk} product={product} />
          ))}
      </div>
    </div>
  );
};

class MainPage extends Component {
  render() {
    return (
      <ProductsComponent />
    );
  }
}

export default MainPage;
