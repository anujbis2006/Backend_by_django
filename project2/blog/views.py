from django.shortcuts import render
from django.http import HttpResponse

def post_details(request,post_id):
    return HttpResponse(f"<h1>Post Details for Post ID: {post_id}</h1>")
def user_provide(request,username):
    return HttpResponse(f"<h1>User Profile for Username: {username}</h1>")
# def article_by_year(request,year,month):
#     return HttpResponse(f"<h1>Articles for Year: {year}, Month: {month}</h1>")
# Create your views here.

def article_by_year(request,**kwargs):
   
    return HttpResponse(f"<h1>Articles for Year:{kwargs}")
