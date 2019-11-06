from django.http import JsonResponse

# Create your views here.

def chat_list (request): 
    if request.method == 'GET':
       return JsonResponse({'list-chats' : 'list-chats'})
    response.status_code = 404
    return response

def messages_list (request, chat_id):
    if request.method == 'GET':
        return JsonResponse({chat_id: 'list_messages'})
    response.status_code = 404
    return response


