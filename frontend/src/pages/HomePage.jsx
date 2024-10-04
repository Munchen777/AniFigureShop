import Header from "../components/Header";
import MainPage from "../components/MainPage";
import Footer from "../components/Footer";


export default function HomePage(params) {
  return (
    <>
      <Header />
      <main className="bg-red-200">
        <MainPage />
      </main>
      <footer>
        <Footer />
      </footer>
    </>
  );
}
