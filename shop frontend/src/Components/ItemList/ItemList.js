import React, {useState, useEffect} from 'react'
import './itemList.css'
import {useSelector} from "react-redux";
import Items from "./Items";
import Pagination from "./Pagination";

const ItemListApp = () => {
    const ItemsList = useSelector((state) => state.ItemReducer.itemList);
    const [items, setItems] = useState([]);
    const [loading, setLoading] = useState(false);
    const [currentPage,setCurrentPage] = useState(1);
    const [itemPerPage] = useState(2);

    useEffect(()=>{
        const fetchItem = () =>{
            setLoading(true);
            // const res = ItemsList;
            setItems(ItemsList);
            setLoading(false);
        };
        fetchItem();
    },[]);
    // console.log(items)
    //Get current post
    const indexOfLastItem = currentPage*itemPerPage;
    const indexOfFirstItem = indexOfLastItem - itemPerPage;
    const currentItems = items.slice(indexOfFirstItem,indexOfLastItem);

    //Change page Number
    const paginate = (pageNumber)=>setCurrentPage(pageNumber);
    return (
        <div className="content-part">
            <div className="row">
                <Items items={currentItems} loading={loading}/>
            </div>
             <Pagination itemPerPage={itemPerPage} totalItems={items.length} paginate={paginate}/>
        </div>
    )
};
export default ItemListApp;