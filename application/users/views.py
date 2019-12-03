from django.http import JsonResponse, HttpResponseNotAllowed,  HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from .models import User
from chats.models import Chat
import json
from django.contrib.auth.decorators import login_required
from django import forms

# Create your views here.

@login_required
def users_list (request):
    if request.method == 'GET':
        users = User.objects.all()
        resp = [{u.id: u.username} for u in users]
        return JsonResponse({"resp": resp})
    return HttpResponseNotAllowed({'err' : 'response not allowed'})

@login_required
def profile (request, user_id):
    if request.method == 'GET':
        user = User.objects.filter(id = user_id)
        resp = [{u.id: [u.username, u.nick]} for u in user]
        return JsonResponse({"resp": resp})
    return HttpResponseNotAllowed({'err' : 'response not allowed'}) 

@login_required
def contacts(request):
    if request.method == 'GET':
        user = User.objects.get(id = request.user.id)
        resp = [{'username': [c.username for c in User.objects.filter(id = contact)]} for contact in user.contacts]
        return JsonResponse({"resp": resp})
    return HttpResponseNotAllowed({'err' : 'response not allowed'})
            
@login_required
def renderHTML (request):
    if request.method == 'GET':
        return render(request, 'start_page.html')
    return HttpResponseNotAllowed({'err' : 'response not allowed'})

@login_required
def users_chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.filter(member__user_id=request.user.id)
        resp = [{c.id: c.topic} for c in chats]
        return JsonResponse({"resp": resp})
    return HttpResponseNotAllowed({'err' : 'response not allowed'})

@login_required
def search_user(request, nick):
    if request.method == 'GET':
        users = User.objects.filter(username__contains=nick)
        resp = [{'user_id': u.id, 'username': u.username, 'nick': u.nick} for u in users]
        return JsonResponse({'data': resp})
    else:
        return HttpResponseNotAllowed({'err' : 'response not allowed'})

class create_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

def create_user(request):
    if request.method == 'POST':
        form = create_user_form(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({"resp": user.username})
        return HttpResponseBadRequest({"error_not_valid_form": "not valid form"})
    else:
        form = create_user_form()
    return render(request, 'create_user.html', {'form': form})
