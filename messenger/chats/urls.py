from chats.views import chat_list
from chats.views import messages_list
from django.urls import path

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<chat_id>/', messages_list, name='messages_list'),
]
