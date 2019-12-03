from django.urls import path
from users.views import users_list, profile, users_chat_list, search_user, contacts, create_user

urlpatterns = [
    path('', users_list, name='users_list'),
    path('profile/<user_id>/', profile, name='profile'),
    path('chats/', users_chat_list, name='users_chat_list'),
    path('search/<nick>/', search_user, name='search_user'),
    path('contacts/', contacts, name='contacts'),
    path('create/', create_user, name='create_user'),
]
