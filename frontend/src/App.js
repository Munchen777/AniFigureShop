import React, { Component, Fragment, useEffect } from "react";
import Header from './components/Header'
import MainPage from './components/MainPage'
import Footer from "./components/Footer";
import ReactDom from 'react-dom/client'
import './App.css';
import {
  BrowserRouter,
  Route,
  Routes,
  createBrowserRouter,
  Link
  } from 'react-router-dom'
import { Container } from "@mui/material";
import axios from "axios";
import LoginPage from './pages/LoginPage'
import HomePage from "./pages/HomePage";
import PrivateRoute from "./pages/PrivateRoute";


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <HomePage /> } />
        <Route path="/login" element={ <LoginPage /> } />
      </Routes>
    </BrowserRouter>
    // <Router>
    //   <Routes>
    //     <PrivateRoute component={ HomePage } path="/"></PrivateRoute>
    //     <Route component={ LoginPage } path="/login"></Route>  
    //   </Routes>
    // </Router>
    // <>
    //   <Header />
    //   <main>
    //     <MainPage />
    //   </main>
    //   <footer>
    //     <Footer />
    //   </footer>
    // </>
  )
}
