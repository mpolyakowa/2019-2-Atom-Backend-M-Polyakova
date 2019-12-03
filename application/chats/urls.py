from django.urls import path
from chats.views import chat_list, messages_list, create_chat, send_message

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('get/<cid>/', messages_list, name='messages_list'),
    path('create/', create_chat, name='create_chat'),
    path('send/', send_message, name='send_message'),
]
