An Uncomfortable Confession:

This is embarrassing, but I misunderstood the gist of this challenge. I took "you can use anything" to mean any tech stack. This was completely my misunderstanding, and I feel really silly about this in retrospect. Since I’ve also been learning GoLang for work, I did the bulk of my studying/preparation for this in Node/Express because I am already familiar with it.

So full disclosure, I’ve used just about the entirety of Google to put together this project in Python/Flask (and to learn both on the fly over the last 18 hours). I completely understand if what I’ve completed means I won’t move forward as a candidate, but I've learned SO MUCH and I’m grateful to have had this chance to challenge myself with a new language and framework!

Outline of Process:

Backend: (Have to run app using Run Python button in VSCode due to an issue with my vscode environment)

Learned to set up local dev environment and dependencies using Conda. This part was probably the most difficult because I had no prior knowledge of this.

Getting the environment to work with VSCode and Mac:

https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos

https://docs.python-guide.org/dev/virtualenvs/

https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment

Turning CSV file into sqlite database:

https://www.fullstackpython.com/blog/export-pandas-dataframes-sqlite-sqlalchemy.html

The sqlite database will be created when the app starts. I realize in a production context, this would be bad news, but implemented it this way for fresh data every time the app starts.

Cleaning up column names in dataframe using pandas:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html

Examples I used to create endpoints in Flask:

https://pythonbasics.org/flask-sqlite/ -- I started with this, using templates and simple HTML just to show the database was loaded correctly and I could access the data in a UI

https://github.com/PrettyPrinted/flask-movie-api/blob/master/api/views.py

I had trouble with the Update/Delete calls until I realized Index was a key word and needed backticks.

Frontend: (cd client > npm start)

I reused some code from a React project I created while learning more about UseContext and UseReducer. I learned the basics of this from a Udemy course on the MERN stack by Brad Traversy (css file stolen from that course & edited).

I refactored the components to work with the movies data, still using a useReducer/useContext to maintain state. Originally I did this as an exercise to manage state without prop drilling and to avoid Redux.

Previously the Add Movie Form used placeholders instead of labels, but I'm really interested in Web Accessibility and have learned that using placeholders instead of labels makes use with a screenreader frustrating.

I updated the filtering component to include Search and Clear buttons. Previously, the filter dynamically updated and called the filtering method onchange, but because of the large set of data, this caused pretty bad performance issues. Without changing the api side to handle the filtering, this was the next best option.

I added a pagination component to handle the large quantity of data in the UI using this example:

https://medium.com/@imranhsayed/simple-react-js-pagination-using-react-hooks-e58463ed191

ToDos Left:

- 2 remaining bugs (noted by TODOs in app.py) - adding a unique ID when creating, and Delete not working for Index numbers greater than 9(??)
- Unit / Integration tests (Sometimes I like to use TDD but didn't want to use time to learn it in Python for this, and code coverage is important to me)
- Refactoring so data handling is less clunky (use Models instead)

- Filter by all columns
- Snackbar with confirmation and error messages
- More dynamic UI to accomodate large blocks of text
- Deploy stack to Heroku or using Docker/Blue Ocean

Quick Demo screen recording of the app running locally:
https://www.youtube.com/watch?v=4gdXFmip0N0

Thanks so much for this opportunity! It was a great learning experience.
