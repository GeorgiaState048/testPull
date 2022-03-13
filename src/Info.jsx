/* eslint-disable */
import {
  useState, React, useRef,
} from 'react';


export function Comment(props) {
  return (
    <div>
      Comment: {props.comment}
    </div>
  );
}

export function Rating(props) {
  return (
    <div>
      Rating: {props.ratings}
    </div>
  );
}

export function MovieId(props) {
  return (
    <div>
      Movie_ID: {props.movieId}
    </div>
  );
}
