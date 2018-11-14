import React from 'react';
import Cell from './Cell';
import './App.css';

const Board = (props) => {
    return(
        <div className='board' >
            {props.state.map(item => item.map(item2=><Cell value={item2} />))}
        </div>
    );
}

export default Board;