/* eslint-disable linebreak-style */
/* eslint-disable react/button-has-type */
/* eslint-disable react/jsx-one-expression-per-line */
import './App.css';
import {
  useEffect, useState, React, useRef,
} from 'react';
import {
  Comment, Rating, MovieId,
} from './Info';
// import { FunFact } from './FunFact';

function App() {
  const [theComment, setComment] = useState([]);
  const [theRating, setRating] = useState([]);
  const [theMovieId, setMovieId] = useState([]);
  const inputRef = useRef(null);
  // const [inputComment, setInputComment] = useState('');
  useEffect(() => {
    const getData = async () => {
      const response = await fetch('/comments_and_ratings');
      const data = await response.json();
      const comments = data[0];
      const ratings = data[1];
      const movieId = data[2];
      setComment(comments.Comments);
      setRating(ratings.Ratings);
      setMovieId(movieId.Movie_ID);
    };
    getData();
  }, []);

  function renderComments(i) {
    return <Comment comment={theComment[i]} />;
  }
  function renderRatings(i) {
    return <Rating ratings={theRating[i]} />;
  }
  function renderMovieIds(i) {
    return <MovieId movieId={theMovieId[i]} />;
  }

  function replaceComment(currComment, index) {
    theComment.splice(index, 1, currComment);
  }

  function deleteComment(index) {
    theComment.splice(index, 1, 'You have no comment here!');
    const newComments = [...theComment];
    setComment(newComments);
    inputRef.current.value = ' ';
  }

  const myComments = theComment.map((currElement, index) => (
    <h1>
      <input type="text" ref={inputRef} onChange={(e) => replaceComment(e.target.value, index)} />
      {renderComments(index)}
      <button onClick={() => deleteComment(index)}>Delete Comment</button>
    </h1>
  ));
  const myRatings = theRating.map((currElement, index) => (
    <h1>
      {renderRatings(index)}
    </h1>
  ));
  const myMovieIds = theMovieId.map((currElement, index) => (
    <h1>
      {renderMovieIds(index)}
    </h1>
  ));
  function handleClick() {
    // const val = theComment;
    const newData = { theComment, theRating };
    fetch('/comments_and_ratings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newData),
    }).then(() => {
      console.log('new comments posted');
    });
    const newComments = [...theComment];
    setComment(newComments);
    inputRef.current.value = ' ';
  }
  return (
    <div>
      {
        myRatings
      }
      {
        myMovieIds
      }
      {
        myComments
      }
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}

export default App;
