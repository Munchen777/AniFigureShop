import { ProductsComponent } from "./MainPage";
import Header from "./Header";
import Footer from "./Footer";

export default function CatalogComponent() {
  return (
    <>
      <Header />
      <main>
        <ProductsComponent />
      </main>
      <Footer />
    </>
  );
}
