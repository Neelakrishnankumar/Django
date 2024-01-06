from bike_app import views
from django.urls import path

app_name = 'bike_app'

urlpatterns = [
  path('register/',views.register,name='register'),
  path('user_login/',views.user_login,name='user_login'),
 # path('other/',views.other,name='other'),
]



