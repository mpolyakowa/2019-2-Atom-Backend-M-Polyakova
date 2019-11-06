from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def users_list (request):
    if request.method == 'GET':
        return JsonResponse({'users_list': 'list'})
    response.status_code = 403
    return response

def profile (request, user_id):
    if request.method == 'GET':
        return JsonResponse({user_id: 'profile'})
    response.status_code = 404
    return response 

def renderHTML (request):
    if request.method == 'GET':
        return render(request, 'start_page.html')
    response.status_code = 404
    return response
