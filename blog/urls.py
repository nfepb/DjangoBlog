from . import views
from django.urls import path


urlpatterns = [
    # Because using class based views, need to add "as_view"
    path('', views.PostList.as_view(), name='home')
]
