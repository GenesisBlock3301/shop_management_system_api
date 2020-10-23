import {listOfItem} from '../Actions/ActionType'


const initialState = {
    itemList: [
        {
            id:1,
            product_name: 'Washing Machine',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            id:2,
            product_name: 'Book',
            product_type: 'Stationar',
            stock: 4,
            price: 50,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            id:3,
            product_name: 'Keyboard',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            id:4,
            product_name: 'Washing Machine',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            id:5,
            product_name: 'Mobile',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            id:6,
            product_name: 'Laptop',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            id:7,
            product_name: 'Fan',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },

    ]
};

export const ItemReducer = (state = initialState, action) => {
    switch (action.type) {
        case listOfItem:
            return {
                ...state,
                itemList: state.itemList
            };
        default:
            return state
    }
};