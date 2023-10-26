from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name="login"),
    path('register/', views.create_user, name="create_user"),
    path('inside/', views.del_user, name="del_user"),
]
