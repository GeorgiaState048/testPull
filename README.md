Heroku Deployment URL: https://boiling-brushlands-22550.herokuapp.com/

Setup Instructions(for windows users only): 
open terminal and run the following commands: 
    pip install requests 
    pip install python-dotenv 
    pip install flask 
    pip install flask_login
    pip install flask_wtf
    pip install wtforms
    pip install heroku
These commands will download the following python libraries: 
    requests: Used to send HTTP requests to an API 
    python-dotenv: Used to access a variable from a .env file, such as an API key. flask: framework for web application 
    flask_login: Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
    flask_wtf: Integrates flask with WTForms, which is a forms validation and rendering library for Python web development
    wtforms: forms validation and rendering library for Python web development
    heroku: software to create and access databases

To use the TMDB API you must create an account at https://www.themoviedb.org/?language=en-US. Once you create your API key, create a .env file in the same directory as app.py and tmdb_wiki.py. Inside this file, insert: TMDB_KEY="your api key". The MediaWiki API does not require an API Key. Next you need to create a database to store the user's information, comments, and ratings. To do this, first create an Heroku account. Then in terminal run the following commands:
    heroku login -i : follow the prompts to sign in to your Heroku account
    heroku create : creates heroku project 
    heroku addons:create heroku-postgresql:hobby-dev -a your-app-name : creates database in your heroku project. 
    heroku configure: Returns a DATABASE_URL. Inside your .env file, insert: DATABSE_URL="your DATABSE_URL". IF THE URL STARTS WITH postgres:, replace that with postgresql:
After downloading all the mentioned libraries and completing the previous steps, the app will be ready to run!

What are at least 2 technical issues you encountered with your project? How did you fix them? 
    1. When I first started creating the forms to input the data, I made each piece of data have its own submit button. This meant that when I left a comment and pressed submit, the page would refresh to another movie and the user would not have been able to put a rating for the correct movie. To fix this, I put two input text elements before the input submit element. This way, the user is able to type in their comments and rating for the movie and just press one submit button which adds the rating and the comment to the database.

    2. In the beginning of the project, I had created a database for the ratings and a database for the comments because I thought it would be easier to understand. However, when I wanted to display my data, it was difficult to figure out which comments and ratings corresponded with each other. To fix this, I put all of my required data in one database. This made it much easier to see which comments corresponded with the correct ratings and movie_ids. It also meant that I didn't have to worry about too many different databases, which can sometimes be confusing.
    
How did your experience working on this milestone differ from what you pictured while working through the planning process? What was unexpectedly hard? Was anything unexpectedly easy?
    I felt that this milestone was a little easier than I thought it would be. Databases have always kind of initmidated me, so I thought it would be a little harder but that portion of the milestone was a lot easier than I thought. The hardest part was figuring out how to implement the Login function. I thought i just needed to check if a username was in a database, but it was more complicated than that. My biggest help with this part of the project came from this video: https://www.youtube.com/watch?v=71EU8gnZqZQ