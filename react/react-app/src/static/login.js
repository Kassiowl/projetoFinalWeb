import React, { useState } from "react";
import PropTypes from 'prop-types';




async function loginUser(credentials) {
  return fetch('http://localhost:8000/logar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
 }

function LoginBox( {  setToken  } )
{
  
  const [email, setEmail] = useState();
  const [senha, setPassword] = useState();

  const [errorMessage, setErrorMessage] = useState()

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const token = await loginUser({
        email,
        senha
      });
      setToken(token);
    }
    catch(error)
    {
      setErrorMessage("username or password is incorrect")
    }
  }
    return(
            <form style={{width: '35rem'}} onSubmit={handleSubmit}>
                <h3 className="fw-normal mb-3 pb-3" style={{letterSpacing: '1px'}}>Log in</h3>
                <div className="form-outline mb-4">
                <input type="username" id="username" className="form-control form-control-lg" onChange={ e => setEmail(e.target.value)}/>
                <label className="form-label" htmlFor="form2Example18">e-mail</label>
                </div>
                <div className="form-outline mb-4">
                <input type="password" id="password" className="form-control form-control-lg" onChange={ e => setPassword(e.target.value)}/>
                <label className="form-label" htmlFor="form2Example28">password</label>
                <input type="checkbox" id="rememberme" className="ms-4 form-check-input"/>
                <label for="rememberme" className="form-label ms-1">Remember me</label>
                </div>
                <div className="pt-1 mb-4">
                <button className="btn btn-success btn-lg btn-block" type="submit">Login</button>
                </div>
                <p >Don't have an account? <a href="#!" className="link-success">Registre-se</a></p>  
                <p className="text-danger">{    errorMessage   }</p>
            </form>
    )
     

}

export default function LoginPage( { setToken } )
{
   return(
        <LoginBox setToken= {   setToken  }/>
    );

}


LoginBox.propTypes = {
  setToken: PropTypes.func.isRequired
};