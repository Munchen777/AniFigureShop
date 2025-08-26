export default function Hero() {
  return (
    <>
      <section className="mx-auto container bg-zinc-200 py-20 mt-10 rounded-2xl drop-shadow-2xl">
        <div className="container mx-auto px-6 text-center lg:text-left">
          <h1 className="text-4xl font-bold text-black sm:text-5xl lg:text-6xl">
            Интернет-магазин
          </h1>
          <p className="mt-4 text-lg text-gray-800 font-semibold sm:max-w-xl lg:max-w-2xl">
            Приветствуем вас в нашем магазине! У нас вы найдете "море" электроники по приятным ценам.
          </p>
        </div>
      </section>
      <div className="mx-auto lg:mt-14 h-10 sm:mt-6 md:mt-9 sm:my-4 my-3">
        <svg
          id="patternId"
          width="100%"
          height="100%"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <pattern
              id="a"
              patternUnits="userSpaceOnUse"
              width="78.141"
              height="46"
              patternTransform="scale(4) rotate(135)"
            >
              <rect
                x="0"
                y="0"
                width="100%"
                height="100%"
                fill="hsla(0,0%,20.8%,1)"
              />
              <path
                d="M69.212 40H46.118L34.57 20 46.118 0h23.094l11.547 20zM57.665 60H34.57L23.023 40 34.57 20h23.095l11.547 20zm0-40H34.57L23.023 0 34.57-20h23.095L69.212 0zM34.57 60H11.476L-.07 40l11.547-20h23.095l11.547 20zm0-40H11.476L-.07 0l11.547-20h23.095L46.118 0zM23.023 40H-.07l-11.547-20L-.07 0h23.094L34.57 20z"
                transform="translate(4.5,0)"
                stroke-width="1"
                stroke="hsla(0,0%,85.1%,1)"
                fill="none"
              />
            </pattern>
          </defs>
          <rect
            width="800%"
            height="800%"
            transform="translate(-488,-180)"
            fill="url(#a)"
          />
        </svg>
      </div>
    </>
  );
}
