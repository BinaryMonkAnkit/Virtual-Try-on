
from django.urls import path
from . import views
# from .views import get_users,create_user,user_detail
from django.views.generic import TemplateView




urlpatterns = [
    # path('users/', get_users, name='get_users'),
    # path('users/create', create_user, name='create_user'),
    # path('users/<int:pk>', user_detail, name='user_detail'),
    
    #this group_name variable will go to views.py file and this comes from the url entered in the browser by user
    # path('', TemplateView.as_view(template_name='index.html')),

    path('', views.index, name= 'group'),
    path('upload_image/', views.upload_image, name='upload_image'),
    
    

]
