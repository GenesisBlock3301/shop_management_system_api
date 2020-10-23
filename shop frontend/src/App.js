import React from 'react';
import './App.css';
import Nav from "./Components/Nav";
import SideBar from "./Components/SideBar";
import ItemListApp from "./Components/ItemList/ItemList";

function App() {
    return (
        <div className="Wrapper">

            <Nav/>
            <div className='body'>
                <SideBar/>
                <ItemListApp/>
            </div>
        </div>

    );
}

export default App;
