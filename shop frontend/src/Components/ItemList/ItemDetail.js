import React from 'react';
import {useSelector} from "react-redux";


const ItemDetail=()=>{
    const Item = useSelector((state) => state.ItemReducer.itemList);
    return(
        <div>
            <div>
                <h1>{Item.product_name}</h1>
                {/*<img src="" alt=""/>*/}
                <p>{Item.description}</p>
            </div>

        </div>
    )
};
export default ItemDetail