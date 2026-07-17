from django.shortcuts import render

def home(request):
    return render(request,'blog.html')

def blog(request):
    student_list= [
        {"name":"John","class":"10th"},
        {"name":"John","class":"9th"},
        {"name":"John","class":"8th"},
    ]
    return render(request,'blog.html',{'students':student_list})

# Create your views here.
