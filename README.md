# Flight Reservation API

<a href="https://www.python.org/"><img src="https://user-images.githubusercontent.com/94041207/199492900-766b0685-56b1-42fc-8510-a221f05de673.png" alt="python" height="30" data-canonical-src="https://www.python.org/static/img/python-logo.png" style="max-width: 100%;">   </a>
<a href="https://www.djangoproject.com/"><img src="https://user-images.githubusercontent.com/94041207/199492944-09e06dfc-a246-48e5-9dea-08c57195fcbd.png" alt="django" height="30" data-canonical-src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" style="max-width: 100%;"></a>
<a href="https://www.django-rest-framework.org/"><img src="https://user-images.githubusercontent.com/94041207/199345513-1a3bd338-9d8a-44a4-b3c4-e64b2ac7eed4.png" alt="django rest framework" height="30" style="max-width: 100%;"></a>
<a href="https://www.sqlite.org/index.html"><img src="https://user-images.githubusercontent.com/94041207/199492996-de5eaa34-dc69-463a-a31d-8fc3a3dc7694.png" alt="SQLite" height="30" style="max-width: 100%;"></a>
<a href="https://www.postgresql.org/"><img src="https://user-images.githubusercontent.com/94041207/199492963-9315ee83-5be9-43b3-aa14-ebdd9a869aea.png" alt="PostgreSQL" height="30" style="max-width: 100%;"></a>
<a href="https://www.heroku.com/"> <img src="https://user-images.githubusercontent.com/94041207/199493654-70c90e3b-24e6-43ab-b700-b73977c6187c.png" alt="heroku" height="30" data-canonical-src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" style="max-width: 100%;"> </a>
<a href="https://postman.com" rel="nofollow"> <img src="https://user-images.githubusercontent.com/94041207/199493662-5b0ab606-1e40-4aee-919e-f8bae4e65794.png" alt="postman" height="30" data-canonical-src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" style="max-width: 100%;"> </a>

## Preview of the project on Postman:

![flight_API](https://user-images.githubusercontent.com/94041207/187237806-6144a7d0-cf64-4a23-9f27-f6d370dea5dd.gif)

## Description 

In this project, I aimed to develope an application with the following features:
* Register, login, logout operations can be done.
* Admin users can see all flights, including previous and future ones. They can see flights with their reservation information. 
* Ordinary users can only see next flights from now on without reservation information. 
* While admin user can read, create, update or delete a flight, anonymous or authenticated user just can see flights
* Admin users can see all reservations. 
* Authenticated users can only see the reservations they have made 
* Authenticated users can create, update and delete reservations. (Both PUT and PATCH can be done)

## What is in the project?   

* Whole project was made by using <img src="https://user-images.githubusercontent.com/94041207/182887053-c5c9c8cf-9182-48a6-aa02-800ee0e5e24f.png"  alt="django rest framework" height="30">
* In developoment process database is <img src="https://logos-download.com/wp-content/uploads/2018/09/SQLite_Logo-450x193.png"  alt="sqlite" height="30">
* In production process database is <img src="https://icon-library.com/images/postgresql-icon/postgresql-icon-13.jpg"  alt="postgresql" height="30"> 
* Backend part was deployed to <img src="https://user-images.githubusercontent.com/94041207/182912844-075185f7-3c3f-4d77-9f49-740dbdadd14d.png"  alt="heroku" height="30"> 
* **dj rest auth** package was used for login, logout and authentication. However register view and serializer were hard coded.
* **Concrete views** were used as views. 
* **Nested serializers** were used. 
* **Token authentication** was used for authentication.
* **Custom permissions** were used for authorization/permission. 
* **form validation** was done 
* **Swagger**, **redoc**, **debug toolbar** were used. And debug was made true for other users to check easily. 
* **Some methods were overridden** to create custom functionalities.

## If you want to check out the project with Postman (strongly advised 😎):

* For admin user **username: <u>admin</u>** and **password: <u>admin</u>**
* If you can use swagger use https://django-flight-reservation-api.herokuapp.com/swagger/
* If you can use swagger use https://django-flight-reservation-api.herokuapp.com/redoc/

## If you do not want to use swagger or redoc you can check the project with Postman as below

### To register a user
Send request with POST method to the url https://django-flight-reservation-api.herokuapp.com/users/register/  like this:
```python
{
"username": "string",
"email": "user@example.com",
"first_name": "string",
"last_name": "string",
"password": "string",
"password2": "string"
}
```
username, email, password and password2 are required 
### To login or logout 
To make login send request with POST method to the url https://django-flight-reservation-api.herokuapp.com/users/auth/login/ like this:

```python
{
"username": "string",
"email": "user@example.com",
"password": "string",
}
```
username and password are required 
To make logout sent request with POST method to the url https://django-flight-reservation-api.herokuapp.com/users/auth/logout/
### To see all flights 
Send request with GET method to the url https://django-flight-reservation-api.herokuapp.com/flight/flights/
If you make this request as admin user (to get Token username:admin and password:admin) you can see past and future flights with their reservations. If you make this request as anonymous or authenticated user you can see just futuru flights without reservation information
### To see a specific flights 
Send request with GET method to the url https://django-flight-reservation-api.herokuapp.com/flight/flights/{flight_id}
### To create a new flight
Send request **as admin user** (to get Token username:admin and password:admin)with POST method to the url https://django-flight-reservation-api.herokuapp.com/flight/flights/ like this
```python
{
"flight_number": "string",
"operation_airlines": "string",
"departure_city": "string",
"arrival_city": "string",
"date_of_departure": "2019-08-24",
"etd": "string"
}
```
### To update a flight 
Send request **as admin user** (to get Token username:admin and password:admin)with PUT or PATCH method to the url https://django-flight-reservation-api.herokuapp.com/flight/flights/{flight_id}/ like this
```python
{
"flight_number": "string",
"operation_airlines": "string",
"departure_city": "string",
"arrival_city": "string",
"date_of_departure": "2019-08-24",
"etd": "string"
}
```
### To delete a flight 
Send request **as admin user** (to get Token username:admin and password:admin)with DELETE method to the url https://django-flight-reservation-api.herokuapp.com/flight/flights/{flight_id}/ 
### To see reservations 
Send request with GET method to the url https://django-flight-reservation-api.herokuapp.com/flight/resv/
If you make this request as admin user (to get Token username:admin and password:admin) you can see all reservations. If you make this request as authenticated user you can see the reservations they have made
### To create reservation
You must be authenticated by login and using token key. Then send request with POST method to the url https://django-flight-reservation-api.herokuapp.com/flight/resv/ like this
```python
{
"flight_id": 0,
"user_id": 0,
"passenger": [
    {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "phone_number": 12345678
    }
  ]
}
```
To create multiple reservations you must add another reservation information dictionary passenger list above
### To update a reservation
You must be authenticated by login and using token key. Then send request with PUT or PATCH method to the url https://django-flight-reservation-api.herokuapp.com/flight/resv/{reservation_id}/ like this

```python
{
"flight_id": 0,
"user_id": 0,
"passenger": [
    {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "phone_number": 12345678
    }
  ]
}
```
Authenticated users can update only the reservations they have made
### To delete a reservation 
You must be authenticated by login and using token key. Then send request with DELETE method to the url https://django-flight-reservation-api.herokuapp.com/flight/resv/{reservation_id}/
Authenticated users can delete only the reservations they have made

# After this explanation if you give a star it will be awesome 🎊🎉⭐

