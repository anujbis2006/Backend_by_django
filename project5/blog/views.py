from django.shortcuts import render
from datetime import datetime


class user:
    def __init__(self,username,age):
        self.username=username
        self.age=age


def home(request):
    context = {
        'name': 'Anuj',
        'age': 20,
        'skill': ['python', 'django', 'javascript'],
        'user':user('Anuj',20),
        'blog':{
            'title':'Django project',
            'content':'<b>Welcome to my blog!</b>',
            'author':{
                'name':'Anuj',
            },
            'created_at':datetime(2025,8,15,10,30,0),

        },
        'empty':'None',
    }
    return render(request,'blog/home.html',context)
# Create your views here.
