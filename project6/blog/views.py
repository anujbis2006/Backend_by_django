from django.shortcuts import render
from datetime import datetime

def blog_detail(request):
   post = {
      'title':"My Second template post",
      'description':"Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.",
      'author':None,
      'created_at':datetime(2025,8,15,10,30,0),
      'comment_count':5,
      'tags':['django','python','web development'],
      'price':100.00,
      
   }
   return render(request,'blog/blog_detail.html',{"post":post, "number": 6})

# Create your views here.
