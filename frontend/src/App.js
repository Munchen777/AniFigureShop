import { BrowserRouter, Routes, Route } from "react-router-dom";
import IndexPage from "./components/Main";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="" element={IndexPage} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
