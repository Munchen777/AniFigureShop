import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import { useRequest } from "../utils/functions";
import { ROOT_API } from "../index";
import Banner from "./Banner";
import { NextArrow, PrevArrow } from "./SliderArrows";

const BannersComponent = () => {
  const [banners, setBanners] = useState([]);

  const { sendRequest } = useRequest();

  useEffect(() => {
    const getBanners = async () => {
      console.log("Debug: Выполняем запрос на /api/v1/get-banners/");
      try {
        let response = await sendRequest(
          `${ROOT_API}/get-banners/`,
          "GET"
        );
        setBanners(response.data.results);
        console.log(response.data.results);
      } catch (error) {
        console.log("Error while making request to /api/v1/get-banners/");
      }
    };

    getBanners();
  }, []);

  const settings = {
    dots: true,
    infinite: true ? banners.length > 1 : false,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000, // 4 seconds
    arrows: true,
    nextArrow: <NextArrow />,
    prevArrow: <PrevArrow />,
  };

  return (
    <div className="container mx-auto justify-center">
      <Slider {...settings}>
        {banners.map((banner) => (
          <Banner key={banner.pk} banner={banner} />
        ))}
      </Slider>
    </div>
  );
};

export default BannersComponent;
