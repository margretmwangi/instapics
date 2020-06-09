from django.urls import path,include

from.views import(
    PostListView,
    PostCreateView,
    like_post,
)
app_name = 'insta'
 
urlpatterns =[
    # local: http://127.0.0.1:8000/
    path('post/',PostListView.as_view(),name="post"),
    path('new/' , PostCreateView.as_view(),name="create"),
    path('like/', like_post, name='like-post'),
 
]