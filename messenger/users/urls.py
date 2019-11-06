from django.urls import path
from users.views import users_list
from users.views import profile

urlpatterns = [
    path('', users_list, name='users_list'),
    path('<user_id>/', profile, name='profile'),
]
