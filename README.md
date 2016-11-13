#Social Cook [Link](http://social-cook.appspot.com/)

This repository holds the code to Social Cook website.
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
Update www/prefabs/secret.py with a secret pass and smtp login info.

##Where to get
[Social Cook](http://social-cook.appspot.com/)

##Project install on local development server
- Create a new Cloud Platform Console project or retrieve the project ID of an existing project from the Google Cloud Platform Console.
- Install the gcloud tool and initialize the Google Cloud SDK. Follow Google Cloud Quickstart Guide for Python App Engine Standard Environment to install Google Cloud in your system. [Link](https://cloud.google.com/appengine/docs/python/quickstart)
- Download the project to your system.
- Through terminal or command line tools, navigate to /www project folder.
- Run command `dev_appserver.py app.yaml`.
- On your brwoser open `localhost:8080`.



