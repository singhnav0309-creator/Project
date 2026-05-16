# Implementation of REST API 

This is a simple REST API Framework project using Django for creating and managing posts using API endpoints.

## Features
- Create posts
- View post list
- User authentication
- update posts
- Delete posts
- Created by field
- Browsable API
- Filters function
- permissions function
- serializers function
- Editing posts

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
GET/posts/
'''

### Create post
'''
POST/posts/
'''

### Get single post
'''
GET/posts/<id>/
'''

### Update post
'''
PUT/posts<id>/
'''

### Delete post
'''
DELETE/posts/<id>/

## Example Response
'''
{
   "id": 1,
   "title": "My First Post",
   "content": "Hello Django REST Framework",
   "created_on": "Date and time",
   "created_by": 1
}
'''
## Author
Navjot Singh
