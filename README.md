# Blog App 
Blog App is a web app made using Python Django framework. As the name suggests it is a Blog app.
Users are allowed to make various blog posts and they can also comment on posts.

# Usage Guide
First create a Python 3 virtual environment.
Bash:
```
virtualenv -p /usr/bin/python3 virtualenv_name
```
Windows CMD:
```
virtualenv virtualenv_name
```

Activate the virtual environment as follows.
Bash:
```
source virtualenv_name/bin/activate
```
Windows CMD:
```
virtualenv_name\Scripts\activate
```

Now install the required packages.
Bash / Windows CMD:
```
pip install -r requirements.txt
```

Now set up environment variables:
* EMAIL_HOST_USER : Your Email ID
* EMAIL_HOST_PASSWORD : Your Email ID Password (Check your Email provider docs for more details.)
* SECRET_KEY : A long random characters string

Now cd into the project folder and first make migrations
Bash / Windows:
```
python manage.py makemigrations
```

Now apply those migrations
Bash / Windows:
```
python manage.py migrate
```

Finally, host it on your localhost
Bash / Windows:
```
python manage.py runserver
```

Go to your browser and type http://localhost:8000 and the project is live 🎉🥳

# Note
This is my first attempt at a fullstack application. So there will be some inconsistencies here and there.
So if there is anything that isn't right, raise an issue and let me know. I am here to learn 😊

### Thank You!