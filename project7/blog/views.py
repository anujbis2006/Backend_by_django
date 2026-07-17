from django.shortcuts import render
from datetime import datetime
def blog_list(request):
    blogs = [
        
            {'title':'Django basics','is_featured':True,'author':'Anuj Biswas'},
            {'title':'Django advanced','is_featured':False,'author':''},
            {'title':'Django rest framework','is_featured':True,'author':'sourav'},
            
    ]
    context = {
        'blogs':blogs,
        'today':datetime.now(),
        'html_code':'<h1>Welcome to Django</h1>',
    }
    return render(request,'blog/blog_list.html',context)
# Create your views here.
