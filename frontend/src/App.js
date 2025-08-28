import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CatalogComponent from "./components/Catalog";
import HomePage from "./pages/HomePage";
import PrivateRoute from "./pages/PrivateRoute";
import { AuthProvider } from "./contexts/AuthContext";
import { CartProvider } from "./contexts/CartContext";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import ResetPasswordDone from "./components/ResetPasswordDone";
import ResetPasswordSuccess from "./components/ResetPasswordSuccess";
import ResetPassword from "./components/ResetPassword";
import PasswordResetForm from "./components/PasswordResetForm";

export default function App() {
  return (
    <Router>
      <AuthProvider>
        <CartProvider>
          <Routes>
            <Route path="/" element={<HomePage />} />

            <Route element={<PrivateRoute />}>
              <Route
                path="/reset-password-done"
                element={<ResetPasswordDone />}
              />
              <Route
                path="/reset-password-success"
                element={<ResetPasswordSuccess />}
              />
              <Route
                path="/api/v1/reset-password-confirm/:uidb64/:token/"
                element={<PasswordResetForm />}
              />
            </Route>

            <Route path="/reset-password" element={<ResetPassword />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/catalog" element={<CatalogComponent />} />
          </Routes>
        </CartProvider>
      </AuthProvider>
    </Router>
  );
}
