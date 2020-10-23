import React, {useState, useEffect} from 'react'
import './itemList.css'
import {useSelector} from "react-redux";

const ItemListApp = () => {
    const ItemsList = useSelector((state) => state.ItemReducer.itemList);
    const [items, setItems] = useState([]);
    const [loading, setLoading] = useState(false);
    const [currentPage,setCurrentPage] = useState(1);
    const [postPerPage,setPostPerPage] = useState(4);

    useEffect(()=>{
        const fetchItem = async () =>{
            setLoading(true);
            const res = ItemsList;
            setItems(res);
            setLoading(false);
        }
        fetchItem();
    },[]);
    console.log(items)
    
    return (
        <div className="content-part">
            <div className="row">
                {
                    ItemsList.map((item,key )=> {
                        return (
                            <div className="col-sm-3 item">
                                <h2>{item.product_name}</h2>
                                <small>{item.product_type}</small>
                                <p>Stock:{item.stock}</p>
                                <p>Price:{item.price}</p>
                                <button type="submit">Add to Cart</button>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
};
export default ItemListApp;