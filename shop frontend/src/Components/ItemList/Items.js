import React from 'react'

const Items = ({items,loading}) => {
    if (loading){
        return <h2>Loading...</h2>
    }
    return (
        <div>
            {
                items.map((item) => {
                    return (
                        <div className="col-sm-3 item" key={item.id}>
                            <h2><a href={`/${item.id}`}>{item.product_name}</a></h2>
                            <small>{item.product_type}</small>
                            <p>Stock:{item.stock}</p>
                            <p>Price:{item.price}</p>
                            {/*<img src="{i}" alt="">*/}
                            <button type="submit">Add to Cart</button>
                        </div>
                    )
                })
            }
        </div>
    )
};
export default Items;