from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('new_page',views.newpage,name='newpage'),
    path('detailfill',views.detailfill,name='detailfill'),
    path('lastpage',views.lastpage,name='lastpage'),
    # path('formfill/',views.formfill,name='detailfill'),


]