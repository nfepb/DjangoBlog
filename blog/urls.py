from . import views
from django.urls import path


urlpatterns = [
    # Because using class based views, need to add "as_view"
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
