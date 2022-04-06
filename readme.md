# Welcome to pandemic Management System

The purpose of this project is to get the overview of

* how many people get affected in a certain pandemic
* In which state and strict it affected most

* how many volunteers(Doctors, Nurses..etc) are there to help
* Is there sufficient availablity of neccasery things

This project has a

- Admin
- State Admin
- District Admin
- Hospital Admin
- Doctor Admin

## Admin has the superuser power. He/She can create State, District, Hospital and Doctor

## State Admin has the power to create District, Hospital and Doctor

## District Admin has the power to create Hospital and Doctor

## Hospital Admin has the power to create Doctor and patients

## Doctor Admin has the power to create patients

The language that are used to create this project are Django

### Requirements are

|                     |
| ------------------- |
| Django              |
| Pymysql             |
| djangorestframework |

```Python3
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
