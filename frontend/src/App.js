import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import MainPage from './components/MainPage';
import LoginPage from './components/LoginPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={ <MainPage /> }></Route>
        <Route path='/login' element={ <LoginPage /> }></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
