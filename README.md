What are at least 3 technical issues you encountered with your project? How did you fix them? 
    1. When I wanted to use the movie data from my 'get_movie_data()' function, I was planning on using a global variable so that I could use that value in another function. Instead of doing this, I returned a list of data from the 'get_movie_data()' function so that I could access each part of the return value however I wanted to. 

    2. I wanted to use the original Spider-Man movie from 2002, but the tmdb movie title for this film is 'Spider-Man'. However, the actual link for this movie is 'Spider-Man (2002 film), so to fix this, I pulled the year the movie was made from the tmdb API and added it to the movie title when I searched for it with mediawiki.

    3. 

What are known problems (still existing), if any, with your project? 

What would you do to improve your project in the future? 
