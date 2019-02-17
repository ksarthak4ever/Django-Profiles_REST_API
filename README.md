# Django-Profiles_REST_API
This is a REST API providing basic functionality for managing user profiles and feeds.

## Some of the features of this API are :~

* Created a custom user model for django admin using which one can login using their email and password instead of username and password.

* hello-viewset is used to test basic APIviews and testing different http methods.

* One can register a user to the api and login to that user by loggin in and getting the token(as token authentication is used) and using ModHeader or any other chrome extension to authenticate user login.

* After logging in a user can see feeds by all the users and can create/update/delete his own feeds.

## How to setup and run this api

* Set up a virtual environment and install django and the libraries used in this project from the requirements.txt file using:~ `pip install -r requirements.txt`

* After running the server using `python manage.py runserver` go to the `http://127.0.0.1:8000/api/` ti test the functionalities of the api.

## Some Blogs i wrote while creating this API

* [RESTful API](https://medium.com/@ksarthak4ever/restful-api-1a49417729a8)
