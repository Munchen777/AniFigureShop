To start app you should start front and back at the same time.

Start frontend:
  - cd frontend
  - npm start

Start backend:
  - cd anifigure
  - python manage.py runserver

Then visit: http://localhost:3000/

To test JWT Auth you should to create user. The simple way is to create superuser.

In terminal backend run:
  - python manage.py createsuperuser

Great! Now you can go: http://localhost:3000/login/
