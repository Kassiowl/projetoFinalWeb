
import logo from './logo.svg';
import './App.css';
import NavbarComponent from "./static/navbar"
import 'bootstrap/dist/css/bootstrap.min.css';
import CadastrarContaCorrente from "./static/cadastrarcontacorrente"
import { BrowserRouter, Route, Routes } from 'react-router-dom';
function App() {
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