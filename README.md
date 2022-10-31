# Read Me

# Just Tri It

![Am I Responsive]()

Just Tri It is a xxx

# User Stories

- As a user, I want to be able to xxx
- As an admin I want to be able to xxx

# UX

The aim of the site is to be as minimal as possible so that attention is focused on the database content.

The website utilises Materialize CSS to responsively react to different screen sizes so that the user can view content on multiple devices.

## Colour Scheme

The colour scheme below was generated by [coolors](https://coolors.co/).

## Typography

# Initial Visual ERD

![Initial ERD](documentation/testing/just-tri-it-initial-erd.png)

# Final Visual ERD

![Final Visual ERD]()

# Wireframes

## Initial Wireframes

![Initial Wireframe A](documentation/wireframes/just-tri-it-initial-wireframe-a.jpg)

![Initial Wireframe B](documentation/wireframes/just-tri-it-initial-wireframe-b.jpg)

# Features

## Existing Features

### Navbar

### Footer

### Favicon

![Favicon]()

## Features Left to Implement

# Technologies Used

- [Git](https://www.atlassian.com/git) - used for version control.
- [GitHub](https://github.com/) - used to secure my code online.
- [Gitpod](https://www.gitpod.io/) - used as the cloud-based IDE.
- [GitHub Projects](https://github.com/sniclasj/atletico-crud/projects/1) - used to track project progress [here](https://github.com/sniclasj/atletico-crud/projects/1).
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - used to create the Python web application.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - used as an extension to Flask to simplify use of SQLAlchemy.
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) - used to handle SQLAlchemy database migrations for the Flask application.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) - used as the Python distribution containing tools for working with MongoDB.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - used to bridge Flask and PyMongo.
- [SQLAlchemy](https://www.sqlalchemy.org/) - used for the relational database provider.
- [MongoDB](https://www.mongodb.com/) - used as the non-relational database provider.
- [Heroku](https://id.heroku.com/login) - used to deploy the site.
- [amiresponsive](http://ami.responsivedesign.is/#) - used for the mockup image.
- [Materialize CSS](https://materializecss.com/) - used to create the layout and structure of the website.
- [HTML](https://en.wikipedia.org/wiki/HTML) - used to write the code for the website.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - used to write the code for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - used to initialize Materialize CSS scripts.
- [CSS](https://en.wikipedia.org/wiki/CSS) - used to style the website.
- [Error Handling](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/) - used to create custom error handling pages for error code 404 and 500.

# Testing

To view all testing documentation, please refer to [TESTING.md](TESTING.md).

# Deployment

The live deployed application can be found at [atletico-crud](https://just-tri-it.herokuapp.com/).

## Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.

![Heroku App Set-Up](documentation/deployment/atletico-crud-heroku-initial-steps.jpg)

- From the new app *Settings*, click *Reveal Config Vars*, and set the following key/value pairs:
  - `IP` 0.0.0.0
  - `PORT` 5000

  - `DATABASE_URL` (this comes from the _Resources_ tab, you can get your own Postgres Database using the Free Hobby Tier)
    - Click on the _Resources_ tab.
    - Search for Postgres in the 'Add-ons' search bar.
    - Select Heroku Postgres as shown in the screenshot below.

![Heroku Postgres Add-On](documentation/deployment/atletico-crud-heroku-postgres-add-on.png)

  - `SECRET_KEY` (this can be any random secret key)

The below screenshot shows the completed config vars page on Heroku with sensitive information in the value boxes redacted.

![Set Config Vars](documentation/deployment/atletico-crud-heroku-config-vars-update.png)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

![Freeze requirements.txt](documentation/deployment/atletico-crud-heroku-freeze-requirements.png)

The Procfile can be created with the following command: `echo web: python app.py > Procfile`

![Create Procfile](documentation/deployment/atletico-crud-heroku-procfile.png)

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either:
- Connect Heroku and GitHub.

![Connect Heroku and GitHub ](documentation/deployment/atletico-crud-heroku-connect-to-github.png)

- Then select "Automatic Deployment" from the Heroku app.

![Enable Auto Deployment](documentation/deployment/atletico-crud-heroku-enable-auto-deploys.png)

- Click the _Deploy Branch_ button.

![App Successfully Deployed](documentation/deployment/atletico-crud-heroku-successfully-deployed-app.png)

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

## Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/sniclasj/atletico-crud.git`

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`.

Create an `env.py` file, and add the following environment variables:

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("MONGO_URI", "insert your own MongoDB URI key here")
os.environ.setdefault("MONGO_DBNAME", "insert your own MongoDB DB Name key here")
os.environ.setdefault("DATABASE_URL", "from your Hobby Tier on the Resources tab from Heroku")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")
```

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/sniclasj/atletico-crud)

## Difference Between Local App and Heroku Deployed App

# Credits

## Content

## Media


## Acknowledgements
I would like to thank my Code Institute mentor Tim Nelson for his support during the course of this project.

I would also like to thank the Code Institute tutor team for the assistance provided during the course of this project.

# Bug
Succesfully check out, click link to go back to listings, go to check out again but get:

InvalidOperation at /checkout/
[<class 'decimal.InvalidOperation'>]
Request Method:	POST
Request URL:	http://localhost:8000/checkout/
Django Version:	3.2.15
Exception Type:	InvalidOperation
Exception Value:	
[<class 'decimal.InvalidOperation'>]
Exception Location:	/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py, line 235, in format_number
Python Executable:	/home/gitpod/.pyenv/versions/3.8.11/bin/python3
Python Version:	3.8.11
Python Path:	
['/workspace/just-tri-it',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python38.zip',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/lib-dynload',
 '/workspace/.pip-modules/lib/python3.8/site-packages',
 '/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/site-packages']
Server time:	Sat, 15 Oct 2022 14:30:04 +0000