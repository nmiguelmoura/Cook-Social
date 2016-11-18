#Social Cooks [Link](http://socialcooks.org/)

This repository holds the code to [Social Cooks](http://socialcooks.org/) website.
The website allows you to share your recipes with other users, comment and vote.

##Features
- The code runs in Google App Engine with Python.
- Responsive design
- Intuitive platform
- Allows post of different kinds of info and images
- Uses mailgun to deliver messages
- Hashes salted passwords for security purposes
- Uses cookies to store login info
- Share recipes in facebook and twitter

##Atention
Create a secret.py file in www/prefabs to allow getting secret hash code, smtp login and password.

##Where to get
[Social Cooks](http://socialcooks.org/)

##Project install on local development server
- Create a new Cloud Platform Console project or retrieve the project ID of an existing project from the Google Cloud Platform Console.
- Install the gcloud tool and initialize the Google Cloud SDK. Follow Google Cloud Quickstart Guide for Python App Engine Standard Environment to install Google Cloud in your system. [Link](https://cloud.google.com/appengine/docs/python/quickstart)
- Download the project to your system.
- Through terminal or command line tools, navigate to /www project folder.
- Run command `dev_appserver.py app.yaml`.
- On your brwoser open `localhost:8080`.



