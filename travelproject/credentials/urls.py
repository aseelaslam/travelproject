from .import views

from django.urls import path,include

from travelproject import settings

urlpatterns = [

        path('register',views.register,name="register"),
        path('login',views.login_view,name="login"),
        path('logout',views.logout,name="logout")


   ]