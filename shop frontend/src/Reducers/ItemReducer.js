import {listOfItem} from '../Actions/ActionType'


const initialState = {
    itemList: [
        {
            product_name: 'Washing Machine',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            product_name: 'Rice Cooker',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            product_name: 'Laptop',
            product_type: 'Electrical',
            stock: 4,
            price: 5000,
            description: "This is good product",
            image: './washing.jpg'
        },
        {
            product_name: 'Bulb',
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