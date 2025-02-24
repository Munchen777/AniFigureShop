import { useCart } from "../contexts/CartContext";

const ProductCard = ({ product }) => {
  const { quantities, handleBuyClick, handleIncrement, handleDecrement } =
    useCart();

  return (
    <div key={product.pk} className="flex-col">
      <div className="bg-white shadow-lg hover:shadow-2xl transform hover:-translate-y-2 transition-all duration-300 rounded-lg p-4 h-full">
        <div className="flex items-center justify-center">
          <div className="w-full h-64 overflow-hidden">
            <img
              className="object-contain w-full h-48 rounded-md"
              src={
                product.images && product.images.length > 0
                  ? product.images[0].image
                  : "default_image_url"
              }
            ></img>
          </div>
        </div>
        <div className="block-inline mx-1 sm:mx-2">
          <h4 className="font-sans text-xl">{product.name}</h4>
        </div>
        <div className="block-inline mx-1 sm:mx-2">
          <span className="font-sans">{product.description}</span>
        </div>
        <div className="flex justify-around">
          <div>
            <span className="font-sans">{product.price} Рублей</span>
          </div>
          <div>
            {!quantities[product.pk] ? (
              <button
                className="relative px-6 py-3 font-bold text-white bg-gradient-to-r from-pink-500 to-yellow-500 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105 hover:from-yellow-500 hover:to-pink-500 hover:shadow-2xl"
                onClick={() => handleBuyClick(product)}
              >
                <span className="text-white font-sans">Купить</span>
              </button>
            ) : (
              <div className="flex items-center space-x-2">
                <button
                  className="bg-gray-300 hover:bg-gray-400 p-2 rounded-md"
                  onClick={() => handleDecrement(product)}
                >
                  <span className="text-black font-sans">-1</span>
                </button>
                <span className="font-sans">{quantities[product.pk]}</span>
                <button
                  className="bg-gray-300 hover:bg-gray-400 p-2 rounded-md"
                  onClick={() => handleIncrement(product)}
                >
                  <span className="text-black font-sans">+1</span>
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
