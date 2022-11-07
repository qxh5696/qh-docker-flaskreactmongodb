import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  getData = async () => {
    const response = await axios.get('http://localhost:5001/api/get/');
    console.log(response);
    this.setState({
      data: response['data'],
    });
  }

  componentDidMount() {
    this.getData();
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <div>
            <h1>{this.state.data}</h1>
          </div>
        </header>
      </div>
    );
  }
}

export default App;