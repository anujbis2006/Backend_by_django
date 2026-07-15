from django.urls import path,re_path
from . import views

urlpatterns = [
    path('post/<int:post_id>/',views.post_details,name='post_details'),
    path('user/<str:username>/',views.user_provide,name='user_provide'),
    path('<int:year>/<int:month>/<int:day>/',views.article_by_year,name='article_by_date'
         ),
    path('article/<int:year>/<int:month>/',views.article_by_year,name='article_by_year'),

    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year,name='article_by_year'),
]