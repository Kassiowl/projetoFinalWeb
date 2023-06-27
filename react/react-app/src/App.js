
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


import CadastrarContaCorrente from "./static/cadastrarcontacorrente"
import NavbarComponent from "./static/navbar"
import LoginPage from './static/login';

import useToken from './login_token/useToken';
import CadastrarContaPessoa from './static/cadastrarcontapessoa';
import CadastrarContaUsuario from "./static/cadastrarcontausuario"
import Depositar from './static/depositar';
import ConsultarSaldoContaCorrente from './static/consultarsaldocontacorrente';
import RealizarTransferencia from './static/realizar_transferencia';
import ConsultarHistorico from "./static/consultarhistorico";

function App() {
  const { token, setToken } = useToken();
  if (!token) {
    return (
      <div className="bg-white">
        <BrowserRouter>
          <Routes>
            <Route path="/cadastrarcontausuario" element={<CadastrarContaUsuario />} />
            <Route path="/" element={<LoginPage setToken={setToken} />} />
          </Routes>
        </BrowserRouter>
      </div>
    );
  }

  return (
    <div className="App bg-dark">
      <NavbarComponent />
      <BrowserRouter>
        <Routes>
           <Route path="/cadastrarcontacorrente" element={ <CadastrarContaCorrente /> } />
           <Route path="/cadastrarcontapessoa" element={ <CadastrarContaPessoa /> } />
           <Route path="/depositar" element={ <Depositar /> } />
           <Route path="/consultarsaldo" element={ <ConsultarSaldoContaCorrente /> } />
           <Route path="/realizartransferencia" element={ <RealizarTransferencia/> } />
           <Route path="/consultarhistorico" element={ <ConsultarHistorico/> } />
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;