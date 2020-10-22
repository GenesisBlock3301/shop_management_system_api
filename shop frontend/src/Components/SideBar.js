import React from 'react'
import {useSelector} from "react-redux";
import './sideBar.css'

const SideBar=(props)=>{
    const items = useSelector((state)=>state.ItemReducer.itemList);
    return(
        <div className="sidebar-list">
            <h2>List Of Item</h2>
            <ul>
                {
                    items.map(item=>{
                        return (
                            <li>{item.product_name}</li>
                        )
                    })
                }
            </ul>
        </div>
    )
};
export default SideBar;