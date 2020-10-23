import React from 'react'

const Pagination = ({itemPerPage, totalItems,paginate}) => {
    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(totalItems / itemPerPage); i++) {
        pageNumbers.push(i);
    }
    return (
        <div>
            <nav>
                <ul className="pagination">
                    {
                        pageNumbers.map(number => {
                            return (
                                <li key={number} className="page-item">
                                    <a onClick={()=>paginate(number)} href="#" className='page-link'>{number}</a>
                                </li>
                            )
                        })
                    }
                </ul>
            </nav>
        </div>
    )
};
export default Pagination