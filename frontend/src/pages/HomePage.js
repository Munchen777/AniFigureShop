import Header from "../components/Header";
import MainPage from "../components/MainPage";
import Footer from "../components/Footer";


export default function HomePage(params) {
  return (
    <>
      <Header />
      <main>
        <MainPage />
      </main>
      <footer>
        <Footer />
      </footer>
    </>
  );
}
