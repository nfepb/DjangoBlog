from . import views
from django.urls import path


urlpatterns = [
    # Because using class based views, need to add "as_view"
    path('', views.PostList.as_view(), name='home'),
    # 'slug' keyword matches 'slug' parameter in get method from
    # PostDetail class in blog/views.py.
    # This is how they are linked
    #  1st slug is a path converter, 2nd is keyword name. 2nd could be anything
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]
