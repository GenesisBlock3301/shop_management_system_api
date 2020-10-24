import React from 'react';
import './App.css';
import Nav from "./Components/Nav";
import SideBar from "./Components/SideBar";
import ItemListApp from "./Components/ItemList/ItemList";

function Home() {
    return (
        <div className="Wrapper">
            <div className='body'>
                <SideBar/>
                <ItemListApp/>
                {/*<ItemDetail/>*/}
            </div>
        </div>

    );
}

export default Home;