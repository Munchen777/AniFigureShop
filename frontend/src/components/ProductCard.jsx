import { useContext } from "react";
import CartContext from "../contexts/CartContext";

const ProductCard = ({ product }) => {
  const { quantities, handleBuyClick, handleIncrement, handleDecrement } = useContext(CartContext);

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
        <div className="block-inline mx-1 sm:mx-2 max-h-16 overflow-auto">
          <span className="font-sans max-w  max-h-16 overflow-auto">{product.description}</span>
        </div>
        <div className="flex justify-around">
          <div>
            <span className="font-sans font-bold">{product.price} {product?.currency}</span>
          </div>
          <div>
            {!quantities[product.pk] ? (
              <button
                className="mt-8 inline-block rounded-full border border-zinc-700 px-12 py-3 text-sm font-medium text-stone-700 hover:bg-neutral-700 hover:text-white focus:outline-none focus:ring active:bg-slate-400"
                onClick={() => handleBuyClick(product)}
              >
                <span className="text-black font-sans">В корзину</span>
              </button>
            ) : (
              <div className="flex items-center space-x-3">
                <button
                  className="mt-8 inline-block rounded-full border border-zinc-700 px-6 py-3 text-sm font-medium text-stone-700 hover:bg-neutral-700 hover:text-white focus:outline-none focus:ring active:bg-slate-400"
                  onClick={() => handleDecrement(product)}
                >
                  <span className="text-black font-sans">-1</span>
                </button>
                <span className="font-sans font-bold">{quantities[product.pk]}</span>
                <button
                  className="mt-8 inline-block rounded-full border border-zinc-700 px-6 py-3 text-sm font-medium text-stone-700 hover:bg-neutral-700 hover:text-white focus:outline-none focus:ring active:bg-slate-400"
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
