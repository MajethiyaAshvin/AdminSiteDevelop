from django.conf.urls import url

from app import views

urlpatterns = [
    url('index', views.index, name="login"),
    url('register', views.register, name="register"),
    url('doLogin', views.doLogin, name="doLogin"),
    url('doRegister', views.doRegister, name="doRegister"),

]
