from django.urls import path
from . import views

urlpatterns=[
    path("register",views.Register.as_view(),name="Register"),
    path("login",views.Login_page.as_view(),name="Login"),
    path("",views.Home.as_view(),name="Home"),
    path("new",views.New_Register.as_view(),name="New"),
    path("add-book",views.Add_Book.as_view(),name="Add_Book"),
    path("get-book",views.Get_Book.as_view(),name="Get_Book"),

]