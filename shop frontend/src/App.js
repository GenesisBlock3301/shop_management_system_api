import React from 'react';
import './App.css';
import Nav from "./Components/Nav";
import SideBar from "./Components/SideBar";
import ItemListApp from "./Components/ItemList/ItemList";
import ItemDetail from "./Components/ItemList/ItemDetail";
import Home from "./Home";
import {Route, Switch, NavLink} from 'react-router-dom';

function App() {
    return (
       <div>
           <Nav/>
           <Switch>
               <Route to='/' component={Home}/>
           </Switch>
       </div>

    );
}

export default App;
