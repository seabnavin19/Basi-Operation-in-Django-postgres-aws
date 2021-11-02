from django.urls import path
from . import views

urlpatterns = [
    # path("",home)
    path("",views.home,name="home"),
    path("sell/<str:pk>/",views.sell,name="sell"),
    path("create/",views.CreateSell,name="create"),
    path("update/<str:pk>/",views.UpdatePost,name="update"),
    path("delete/<str:pk>/",views.DeletePost,name="delete"),
    path("createuser/",views.CreateUser,name="creatUser"),
    path("login/",views.LoginUser,name="loginUser"),
    path("logout/",views.LogoutUser,name="logout"),
    path("user/",views.Userpage,name="user"),

]