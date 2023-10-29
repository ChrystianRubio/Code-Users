from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name="login"),
    path('register/', views.create_user, name="create_user"),
    path('inside/', views.inside, name="inside"),
    path('update/', views.update_user, name="update_user"),
    path('delete/', views.del_user, name="del_user"),
]
