import React from "react";
import "./Register.css";

const Register = () => {
  return (
    <div className="register-container">
      <h2>Sign Up</h2>

      <input type="text" placeholder="Username" />
      <input type="text" placeholder="First Name" />
      <input type="text" placeholder="Last Name" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />

      <button>Register</button>
    </div>
  );
};

export default Register;
