from django.urls import path

from cars.accounts.views import login_user, logout_user, RegisterView, ProfileDetailsView

from .signals import *

urlpatterns = (

    path('login/', login_user, name='log in user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout/', logout_user, name='log out user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),

)
