# Implementation of REST API 

This is a simple REST API Framework project using Django for creating and managing Users using API endpoints.

## Features
- Create User
- View User list
- User authentication
- update User
- Delete User
- Created by field
- Browsable API
- serializers function
- Editing User

## Softwares used
- Python
- Django
- Django REST Framework
- SQL

## Installation
Clone the repository:
'''
git clone https://github.com/singhnav0309-creator/Project.git
'''

Move into the project folder:
'''
cd Project
'''

Install dependencies:
'''
pip install -r requirements.txt
'''

Make migrations:
'''
python manage.py makemigrations
'''

Run migrations:
'''
python manage.py migrate
'''

Start server:
'''
python manage.py runserver
'''

## API Endpoints

### Admin Administration
'''
GET/admin/
'''

### Get All Posts
'''
GET/Users/
'''

### Create post
'''
POST/Users/
'''

### Get single post
'''
GET/Users/<id>/
'''

### Update post
'''
PUT/Users<id>/
'''

### Delete post
'''
DELETE/Users/<id>/

## Example Response
'''
{
   "usernsme": "abc",
   "Password": "#########",
   "email": "abc@gmail.com",
   "bio": "About me",
   "date_joined": Date and time
}
'''
## Author
Navjot Singh
