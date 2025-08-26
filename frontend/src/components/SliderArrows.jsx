import React from "react";

export function NextArrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={`${className} flex items-center justify-center rounded-full shadow-md transition-colors duration-200 cursor-pointer z-10`}
      style={{ ...style, display: "flex", background: "black" }}
      onClick={onClick}
    >
    </div>
  );
}

export function PrevArrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={`${className} flex items-center justify-center rounded-full shadow-md transition-colors duration-200 cursor-pointer z-10`}
      style={{ ...style, display: "flex", background: "black" }}
      onClick={onClick}
    >
    </div>
  );
}
