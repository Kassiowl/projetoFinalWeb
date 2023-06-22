
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


import CadastrarContaCorrente from "./static/cadastrarcontacorrente"
import NavbarComponent from "./static/navbar"
import LoginPage from './static/login';

import useToken from './login_token/useToken';
import CadastrarContaPessoa from './static/cadastrarcontapessoa';


function App() {
  const { token, setToken } = useToken();
  if(!token)
  {
    return <LoginPage setToken={setToken}/>
  }

  return (

    <div className="App bg-dark">
      <NavbarComponent />
      <BrowserRouter>
        <Routes>
           <Route path="/cadastrarcontacorrente" element={ <CadastrarContaCorrente /> } />
           <Route path="/cadastrarcontapessoa" element={ <CadastrarContaPessoa /> } />
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;