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
  const [theUser, setUser] = useState('');
  const [message, setMessage] = useState('Click \'Save Data\' to save your reviews!');
  const inputRef = useRef(null);
  useEffect(() => {
    const getData = async () => {
      const response = await fetch('/comments_and_ratings');
      const data = await response.json();
      console.log(data);
      const comments = data[0];
      const ratings = data[1];
      const movieId = data[2];
      const name = data[3];
      setComment(comments.Comments);
      setRating(ratings.Ratings);
      setMovieId(movieId.Movie_ID);
      setUser(name.Name);
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

  // replaces comments or ratings
  function replaceComment(currComment, index) {
    theComment.splice(index, 1, currComment);
  }
  function replaceRating(currRating, index) {
    theRating.splice(index, 1, currRating);
  }

  // deletes specific comment
  function deleteComment(index) {
    theComment.splice(index, 1, 'You deleted this review');
    const newComments = [...theComment];
    setComment(newComments);
    inputRef.current.value = ' ';
  }

  // map function used to create display all comments and ratings
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
  const link = `/homepage/${theUser}`; // link to go back to the previous page
  function handleClick() {
    const newData = { theComment, theRating };
    fetch('/comments_and_ratings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newData),
    }).then(() => {
      setMessage('Your reviews have been saved! Refresh the page!');
    });
    const newComments = [...theComment];
    setComment(newComments);
    inputRef.current.value = ' ';
  }
  return (
    <body>
      <h1 className="color">Edit or Delete your comments and ratings!</h1>
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
      <div className="color">
        {message}
      </div>
      <div className="up">
        <button onClick={handleClick}>Save Data</button>
      </div>
      <a href={link}>Click Here to Leave more Comments!</a>
    </body>
  );
}

export default App;
