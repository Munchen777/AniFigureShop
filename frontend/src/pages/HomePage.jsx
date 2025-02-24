import Header from "../components/Header";
import MainPage from "../components/MainPage";
import Footer from "../components/Footer";
import { AuthProvider } from "../contexts/AuthContext";
import Hero from "../components/Hero";

export default function HomePage(params) {
  return (
    <>
      <AuthProvider>
        <Header />
        <Hero />
        {/* <main>
          <MainPage />
        </main> */}
        <Footer />
      </AuthProvider>
    </>
  );
}
