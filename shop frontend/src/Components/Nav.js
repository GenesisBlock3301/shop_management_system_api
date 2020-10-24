import React from 'react'
import './Nav.css'
import {NavLink} from 'react-router-dom';


const Nav = () => {
    return (

        <div>
            <div className="nav-menu">
                <ul>
                    <li><a href=""> LOGO</a></li>
                    <li><NavLink exact to='/'>Home</NavLink></li>
                    <li><a href="">About</a></li>
                    <li><a href="">Contact</a></li>
                    <li><a href="">Login</a></li>
                </ul>
            </div>
        </div>
    )
};
export default Nav