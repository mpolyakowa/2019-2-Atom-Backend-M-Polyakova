from django.http import JsonResponse, HttpResponseNotAllowed

# Create your views here.

def chat_list (request): 
    if request.method == 'GET':
       return JsonResponse({'list-chats' : 'list-chats'})
    return HttpResponseNotAllowed({})

def messages_list (request, chat_id):
    if request.method == 'GET':
        return JsonResponse({chat_id: 'list_messages'})
    return HttpResponseNotAllowed({})


