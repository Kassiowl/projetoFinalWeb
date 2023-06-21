import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function NavbarComponent() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary" data-bs-theme="dark">
      <Container>
        <Navbar.Brand href="#home">Home</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Cadastrar conta corrente</Nav.Link>
            <Nav.Link href="#link">Cadastrar conta pessoa</Nav.Link>
            <Nav.Link href="#link">Cadastrar conta usuario</Nav.Link>
            <Nav.Link href="#link">Consultar historico</Nav.Link>
            <Nav.Link href="#link">consultar saldo conta corrente</Nav.Link>
            <Nav.Link href="#link">Depositar</Nav.Link>
            <Nav.Link href="#link">Realizar transferencia</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavbarComponent;