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

What are at least 3 technical issues you encountered with your project milestone? How did you fix them?
    1. One of the issues I was trying to figure out how to edit the comments. I was very confused at first because I was able to create the text boxes for all of my comments, but when I typed in them, it would type in the text boxes for the other comments at the same time. When I looked into it more, I realized that putting my input box in the component for Comments gave me this problem, so I had to move it the map function for comments. This allowed me to type in each box without affecting the other ones.
    
    2. Another issue I had was with trying to access the data that I was inputting for the comments. At first, I was setting the 'theComment' state variable to whatever I typed in for a new comment, however, this meant that 'theComment' would only be equal to that comment, and not the other ones that were there. Since the 'theComment' is a list, I just made the input comment replace the comment that I wanted to replace. Since the map function can keep track of which iteration I am on, I was able to easily do that.

    3. The third issue that I had was when I wanted show a message that said wether or not the comments that I edited were saved. I wanted to use a simple alert() message but I quickly found out that alert() did not exist in the context that I wanted to use so I had to come up with another way. What I did was create a state variable called 'message' that I set to 'message not saved' and this message would be displayed below the reviews as soon as the page is loaded. Once I click 'Save Data' and the new info is posted to the server, I would change it to 'message saved' and the message below the reviews would automatically change.
    
What was the hardest part of the project for you, across all milestones? What is the most useful thing you learned, across all milestones?
    The hardest part of the project for me across all milestones was definitely the third milestone. I didn't have much experience with javascript before this so it was a little difficult to pick up on for me. The most important thing I learned was to start early. I started kind of late on my third milestone so I was a lot more stressed than I should have been. I also probably wasn't able to fully digest all of the content that I was using for this milestone since I was trying to go through it so fast.  