
Project:
 This project is about creating a basic api that returns a serialized response of data about all the Users and there login time.

Requirements:

  1. Python 3.6.5
  2. Django==3.0.7
  3. djangorestframework==3.11.0
  
Setup:

  1. Create a virtual environment and install django in it. 
     Command:
     create virtual env - virtualenv <environment name>
  2. Activate the environment.
     Command:- <environment name>\Scripts\activate 
  3. Install django and djangorestframework
     Django installation:- pip install django
     Restframework:- pip install djangorestframework 
  4. Create a django project.
     Command:- django-admin startproject <project name>
  5. Create an app.
     Command:- python manage.py startapp <app name>
  6. Create super user to create and modify data manually through admin interface.
     Command:- python manage.py createsuperuser
     This will ask you to enter login name and password.
  7. Create models,urls,serializers.
  8. When code is ready run migrations and run the server.
     Migration commands:
        1. python manage.py makemigratios
        2. python manage.py migrate
     Runserver:
        python manage.py runserver
     
  
Explanation:

 Models Used:
  1. User - Consists of three field named as "id"(unique id), "real_name"(name of the employee), "tz"(timezone in which they work)
  2. ActivityPeriod - Consists of four field named as "id"(unique id),"start_time","end_time" and "user"(foreign key refering the User)
  
 Flow of code:
  1. When the url is hit django automatically checks for the url patterns available in the "urls.py" and encounters the "home/"
     options available and hence gets directed to the UserActivityViewSet.
     path('home/',views.UserActivityViewSet.as_view())   
     
   2. The UserActivityClass checks for the method being called and directs it to the GET,POST,PUT,DELETE functions.
   
   3. Here the GET method is called which takes all the Users objects available in the database and passes it to the UserActivitySerializer.
      
   4. The UserActivitySerializer serializes the required data, which in turn is sent as a response to the url.  
 
 
 Request: http://127.0.0.1:8000/home/ 
 
 Response :
 
    {
    "members": [
        {
            "id": 1,
            "real_name": "Vidhu Priya",
            "tz": "India/Kolkata",
            "activity_period": [
                {
                    "start_time": "Jun 04 2020 06:00AM",
                    "end_time": "Jun 04 2020 06:30AM"
                }
            ]
        },
        {
            "id": 2,
            "real_name": "Aditi Rao",
            "tz": "America/LosAngeles",
            "activity_period": [
                {
                    "start_time": "Jun 05 2020 06:00AM",
                    "end_time": "Jun 05 2020 18:00PM"
                }
            ]
        },
        {
            "id": 3,
            "real_name": "Ankit",
            "tz": "America/LosAgeles",
            "activity_period": [
                {
                    "start_time": "Jun 16 2020 06:00AM",
                    "end_time": "Jun 17 2020 18:00PM"
                }
            ]
        },
        {
            "id": 4,
            "real_name": "Rahul",
            "tz": "America/LosAgeles",
            "activity_period": [
                {
                    "start_time": "Jun 03 2020 06:00AM",
                    "end_time": "Jun 03 2020 18:00PM"
                }
            ]
        }
    ]
}
   
   
   
  
  
 
 
  
