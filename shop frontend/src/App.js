import React from 'react';
import logo from './logo.svg';
import './App.css';
import Nav from "./Components/Nav";
import SideBar from "./Components/SideBar";

function App() {
  return (
      <div className="container">
          <Nav/>
          <SideBar/>
      </div>
  );
}

export default App;
