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


// class App extends Component {
//   render() {
//     return (
//       <>
//         <Header></Header>
//         <main>
//           <MainPage></MainPage>
//         </main>
//         <footer>
//           <Footer></Footer>
//         </footer>
//       </>
//     )
//   }
// }

// function App() {

//   const [products, setProducts] = useState([])
//   const [isLoading, setisLoading] = useState(true)

//   useEffect(() => {
//     fetchData()
//   }, [])

//   const fetchData = async () => {
//     try {
//       const response = await axios.get(`${ROOT_API}/api/products`)
//       setProducts(response.data)
//       setisLoading(false)
//     } catch (error) {
//       console.log(error)
//     }
//   }

//   return (
//     <>
//       <Header></Header>
//       <main>
//         <MainPage></MainPage>
//       </main>
//       <footer>
//         <Footer></Footer>
//       </footer>
//     </>
//   )
// }

// export default App;
