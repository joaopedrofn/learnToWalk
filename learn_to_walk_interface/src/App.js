import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Board from './Board';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      qTable: [],
      score: 0,
      status: 'playing',
      state: [
        [0,0,0,0,0],
        [0,-1,0,0,2],
        [0,-1,0,0,-2],
        [0,0,-1,0,0],
        [1,0,0,0,0],
    ]
    };
  }

  _train = async () => {
    const resp = await fetch('http://localhost:8080/train');
    const table = await resp.json();
    this.setState({qTable: await table});
  }

  _aiStep = async () => {
    const resp = await fetch('http://localhost:8080/ai_step');
    const result = await resp.json();
    let status = 'playing';
    if(result.done)
      if(result.state[1][4] === 1) status = 'Victory!';
      else status = 'Defeat!';
    this.setState({
      state: await result.state, 
      score: await result.rewards.reduce((total, n) => total+n ),
      status
    });
  }

  _reset = async () => {
    await fetch('http://localhost:8080/reset');
    this.setState({
      qTable: [],
      score: 0,
      status: 'playing',
      state: [
        [0,0,0,0,0],
        [0,-1,0,0,2],
        [0,-1,0,0,-2],
        [0,0,-1,0,0],
        [1,0,0,0,0],
    ]
    });
  }

  _renderTable = () => (
    <table className='qTable' >
      <thead>
          <tr>
            <th>State/Action</th>
            <th>UP</th>
            <th>DOWN</th>
            <th>LEFT</th>
            <th>RIGHT</th>
          </tr>
      </thead>
      <tbody>
          {
            this.state.qTable.map((actions, state) => {
              let tds = [];
              actions.map(v => {tds.push(<td>{v}</td>);});
              return (
                <tr>
                  <td>{state}</td>
                  {tds}
                </tr>
              )
            })
          }
      </tbody>
        </table>
  )

  _renderEndGame = () => (
    <div className='endGameMsg'>
      <h2>{this.state.status}</h2>
    </div>
  )

  render() {
    return (
      <div className="App">
        <h1>Learn to walk! Score: {this.state.score}</h1>
        <Board state={this.state.state} />
        {
          this.state.status === 'playing'
          ?(
            <div className='buttonRow' >
              <button
                className='button train'
                onClick={this._train} 
              >
                Train!
              </button>
              <button
                className='button step'
                onClick={this._aiStep}
              >
                AI, dance to me!
              </button>
            </div>
          )
          :this._renderEndGame()
        }
        <div className='buttonRow' >
          <button
            className='button'
            style={{margin: 'auto', backgroundColor: '#e17055', color: '#dfe6e9'}}
            onClick={this._reset} 
          >
            Reset
          </button>
        </div>
        {this.state.qTable.length>0?this._renderTable():null}
      </div>
    );
  }
}

export default App;
