const Banner = ({ banner }) => {
  return <img
  className="lg:rounded-2xl"
  src={banner.content}
  style={{ width: "100%", height: "auto", borderRadius: "8px" }}
  >
  </img>;
};

export default Banner;
