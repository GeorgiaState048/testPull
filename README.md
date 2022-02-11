Heroku Link: https://serene-caverns-03709.herokuapp.com/

Setup Instructions(for windows users only):
    open terminal and run the following commands:
        pip install requests
        pip install python-dotenv
        pip install flask
    These commands will download the following python libraries:
        requests: Used to send HTTP requests to an API
        python-dotenv: Used to access a variable from a .env file, such as an API key. 
        flask: framework for web application
     To use the TMDB API you must create an account at https://www.themoviedb.org/?language=en-US. Once you create your API key, create a .env file in the same directory as app.py and tmdb_wiki.py. Inside this file, insert: TMDB_KEY="your api key". The MediaWiki API does not require an API Key, so after this, the app will be ready to run!

Detailed description of 2+ technical issues and how you solved it (your process, what you searched, what resources you used)
    1. When I wanted to use the individual pieces of movie data (title, release date, genre, etc.) from my 'get_movie_data()' function, I used global variables so that I could assign them to the values I got from the function. When I did this, I could not put those variables in index() function in app.py, which meant that I could not access the correct information. To get around this, I returned a list of data from the 'get_movie_data()' that contained the title, release date, etc. so that I could access each part of the return value as a list element in the index() function in the app.py file. 

    2. I wanted to use the original Spider-Man movie from 2002, but the tmdb movie title for this film is 'Spider-Man'. When I search for the movie title using mediawiki, there were too many articles related to Spider-Man so I knew had to make my search string more precise. To do this, I pulled the year each movie was released from the tmdb API and added it to the movie title when I searched for it with mediawiki. So now, the search for Spider-Man would actually be 'Spider-Man 2002'.

Detailed description of 2+ known problems and how you would address them if you had more time. If none exist, what additional features might you implement, and how?
    1. In my second technical issue, I added the release year to the movie title to make the mediawiki search more precise. However, for the movie Spider-Man: No Way Home, searching for 'Spider-Man: No Way Home 2021', gives me an internal server error because there were no results. However, if I searched 'Spider-Man: No Way Home', I would find what I was looking for. This basically means that while my mediawiki search method works for most movies, there are some that it doesn't work for. The error that I got was an index error for my json_response[3][0] value because the json_response was empty. If I had more time, I would set up a check to see if the json_response in the wiki_page() function is empty or not, and if it is, I would do another search without the year. 

    2. A feature that I would have liked to implement is a welcome screen that asks the user to input a genre of movies that they would like to see. Then my program would create a list of all of the movie_ids with that genre and then show a random movie on each reload. To do this, I would create a function called get_movies_by_genre() in the tmdb_wiki.py file, where the return value would be a list of movie ids that have a specific genre. I would use this return value in the index() function in app.py, and then the rest of my program would be the same. So now, after every refresh a new movie of a specific genre is shown. 
    
