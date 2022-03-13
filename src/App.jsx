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
  const [message, setMessage] = useState('The message has not been saved yet!');
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
  function replaceRating(currRating, index) {
    theRating.splice(index, 1, currRating);
  }

  function deleteComment(index) {
    theComment.splice(index, 1, 'You deleted this review');
    const newComments = [...theComment];
    setComment(newComments);
    inputRef.current.value = ' ';
  }

  // function deleteRating(index) {
  //   theRating.splice(index, 1, 'You deleted this review');
  //   const newRatings = [...theRating];
  //   setRating(newRatings);
  //   inputRef.current.value = ' ';
  // }

  const myComments = theComment.map((currElement, index) => (
    <p className="rowC">
      {renderComments(index)}
      <textarea rows="1" cols="20" ref={inputRef} onChange={(e) => replaceComment(e.target.value, index)} />
      <button onClick={() => deleteComment(index)}>Delete Comment</button>
    </p>
  ));
  const myRatings = theRating.map((currElement, index) => (
    <p className="rowC">
      {renderRatings(index)}
      <textarea rows="1" cols="10" ref={inputRef} onChange={(e) => replaceRating(e.target.value, index)} />
    </p>
  ));
  const myMovieIds = theMovieId.map((currElement, index) => (
    <p className="rowC">
      {renderMovieIds(index)}
    </p>
  ));
  function messageSaved() {
    setMessage('Your message has been saved!');
  }
  function handleClick() {
    // const val = theComment;
    const newData = { theComment, theRating };
    fetch('/comments_and_ratings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newData),
    }).then(() => {
      messageSaved();
    });
    const newComments = [...theComment];
    setComment(newComments);
    inputRef.current.value = ' ';
  }
  return (
    <body>
      <h1>Edit or Delete your comments and ratings!</h1>
      <div className="rowC color">
        <div>
          {
              myMovieIds
          }
        </div>
        <div>
          {
              myRatings
          }
        </div>
        <div>
          {
              myComments
          }
        </div>
      </div>
      {message}
      <div className="up">
        <button onClick={handleClick}>Save Data</button>
      </div>
    </body>
  );
}

export default App;
