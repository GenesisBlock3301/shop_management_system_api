import {listOfItem} from '../Actions/ActionType'


const initialState ={
    itemList:[
        {
             product_name:'Washing Machine'
        },
        {
             product_name:'Rice Cooker'
        },
        {
             product_name:'Laptop',
        },
        {
             product_name:'Bulb'
        },
    ]
};

export const ItemReducer=(state=initialState,action)=>{
    switch (action.type) {
        case listOfItem: return {
            ...state,
            itemList: state.itemList
        };
        default:
            return state
    }
};