import React from 'react';
import './App.css';

const Cell = (props) => {
    let kind = [];
    kind[1] = 'char';
    kind[0] = 'cell';
    kind[-1] = 'wall';
    kind[2] = 'goal';
    kind[-2] = 'doom';
    return(
        <div className={kind[props.value]} />
    );
}

export default Cell;