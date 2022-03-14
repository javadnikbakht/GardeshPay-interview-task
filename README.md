# GardeshPay-interview-task

This project allows:

- Register Users
- Login Users
- Follow another users
- Unfollow another Users
- Post tweets
- Like Tweets
- Unlike Tweets

All API request after login require JWT access token, you can get this token in the next end-point:

```shell
http://localhost:8000/api/auth/token/
```

#### Regular django project

Inside directory `GardeshPay-interview-task` execute:

```shell
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

You can see the project documentation in:

```shell
http://localhost:8000/swagger/
```