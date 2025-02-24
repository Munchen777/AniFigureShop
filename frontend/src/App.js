import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import PrivateRoute from "./pages/PrivateRoute";
import { AuthProvider } from "./contexts/AuthContext";
import { CartProvider } from "./contexts/CartContext";
import LoginForm from "./components/LoginForm";
import RegisterForm from "./pages/RegisterForm";
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
              {/* Другие защищенные маршруты можно добавлять внутри PrivateRoute */}
            </Route>

            <Route path="/login" element={<LoginForm />} />
            <Route path="/register" element={<RegisterForm />} />
            <Route path="/reset-password-success" element={<ResetPasswordSuccess />} />
            <Route path="/reset-password" element={<ResetPassword />} />
            <Route path="/users/api/v1/reset-password-confirm/:uidb64/:token/" element={<PasswordResetForm />} />

          </Routes>
        </CartProvider>
      </AuthProvider>
    </Router>
  );
}
