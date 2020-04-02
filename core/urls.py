from django.urls import path
from .views import Register,Login,MyMessage,MyPost
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home,name='home'),
    path('Login/', Login.as_view(), name="Login"),
    path('Register/', Register.as_view(), name="Register"),
    path('Logout/', views.Logout, name="Logout"),
    path('Contact/',MyMessage.as_view(),name="Contact"),
    path('News/',views.News,name="News"),
    path('Profile/',views.Profile,name="Profile"),
    path('Post/',MyPost.as_view(),name="Post"),
]