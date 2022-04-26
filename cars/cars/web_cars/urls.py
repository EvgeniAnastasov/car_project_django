from django.urls import path

from cars.web_cars.views import show_index, \
    DeleteCarView, like_car, CarAddView, car_details, EditCarView, car_photo

urlpatterns = (

    path('', show_index, name='show index'),

    path('car/add/', CarAddView.as_view(), name='add car'),
    path('car/details/<int:pk>/', car_details, name='car details'),
    path('car/edit/<int:pk>', EditCarView.as_view(), name='car edit'),
    path('car/delete/<int:pk>', DeleteCarView.as_view(), name='car delete'),

    path('car/like/<int:pk>/', like_car, name='like car'),
    path('car/photos/<int:pk>', car_photo, name='car photos')

)
