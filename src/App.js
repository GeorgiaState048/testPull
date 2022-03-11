import './App.css';
import {useEffect, useState} from 'react';
import React from 'react';
import {FunFact} from './FunFact';

function App() {
  const [fun_fact, setNewFact] = useState(null);
  useEffect(() => {
    fetch('/comments_and_ratings')
      .then(res => res.json())
      .then(data => setNewFact(data));
    }
  )
    
  return (
    <div>
      <ul>
        <FunFact fact = {fun_fact}/>
      </ul>
    </div>
  );
}

export default App;
