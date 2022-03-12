/* eslint-disable */
import {
  useState, React, useRef,
} from 'react';


export function Comment(props) {
  return (
    <div>
      {props.comment}
    </div>
  );
}

export function Rating(props) {
  return (
    <div>
      {props.ratings} <button>Delete Rating</button>
    </div>
  );
}

export function MovieId(props) {
  return (
    <div>
      {props.movieId}
    </div>
  );
}
