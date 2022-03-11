import './App.css';
import { useEffect, useState, React } from 'react';
// import { FunFact } from './FunFact';
// import { FunFact } from './FunFact';

function App() {
  const [funFact, setNewFact] = useState([]);
  useEffect(() => {
    const getData = async () => {
      console.log('fetch called');
      const response = await fetch('/comments_and_ratings');
      const data = await response.json();
      console.log('fetch finished');
      console.log(data.items);
      setNewFact(data.items);
    };
    getData();
  }, []);
  // <FunFact fact={funFact.map((data) => <div>{data.Fun}</div>)} />
  return (
    <div>
      {
        funFact.map((rating) => <h2>{rating}</h2>)
      }
    </div>
  );
}

export default App;
