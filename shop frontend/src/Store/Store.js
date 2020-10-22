import {createStore} from 'redux'
import rootReducer from '../Reducers'

const initialState = {};

export const store = createStore(
    rootReducer,
    initialState,

);
