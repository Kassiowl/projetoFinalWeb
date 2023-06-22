
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


import CadastrarContaCorrente from "./static/cadastrarcontacorrente"
import NavbarComponent from "./static/navbar"
import LoginPage from './static/login';

import useToken from './login_token/useToken';


function App() {
  const { token, setToken } = useToken();
  if(!token)
  {
    return <LoginPage setToken={setToken}/>
  }

  return (

    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<NavbarComponent />}></Route>
           <Route path="/cadastrarcontacorrente" element={ <CadastrarContaCorrente /> } />
        </Routes>
      </BrowserRouter>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;