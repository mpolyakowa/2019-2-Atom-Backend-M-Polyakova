from django.http import JsonResponse, HttpResponseNotAllowed,  HttpResponseBadRequest, HttpResponseNotFound
from .models import Chat, Message
from users.models import Member
import json
from django.shortcuts import render, get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

from django import forms

class create_chat_chat(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('topic', 'is_group_chat')

# class create_chat_member(forms.Form):
#     uid = forms.IntegerField(label='UserId')
#     def clean_uid(self):
#         data = self.cleaned_data['uid']
#         if not User.objects.filter(id=data):
#             raise forms.ValidationError("You have forgotten about Fred!")
#         return data

@login_required
def chat_list(request): 
    if request.method == 'GET':
        chat = Chat.objects.all()
        resp = [{c.id: c.topic} for c in chat]
        response = JsonResponse({"resp": resp})
        return response
    return HttpResponseNotAllowed({'err' : 'response not allowed'})

#@login_required
def messages_list (request, cid):
    if request.method == 'GET' or request.method == 'POST':
  #      if Member.objects.filter(chat_id=cid, user_id=request.user.id):
   #         print(request.user.id, "user")
    #        messages = Message.objects.filter(chat_id=cid) 
    #        read_messages(request, cid)
    #        container = [{message.user_id: message.content} for message in messages]
    #        return JsonResponse({"resp": container})
    #    return JsonResponse({"not a member": "user is not a member"})
         messages = Message.objects.filter(chat_id=cid)
         chat = get_object_or_404(Chat, id=cid)
         resp = [{message.content: message.added_at} for message in messages]
         return JsonResponse({"name": chat.topic, "data": resp})
    return HttpResponseNotAllowed({'err': 'resp not allowed'})

@login_required
def create_chat (request):
    if request.method == 'POST':
        form = create_chat_chat(request.POST)
        if form.is_valid():
            created_chat = form.save()
            Member.objects.create(chat_id=created_chat.id, user_id=request.user.id)
            return JsonResponse({created_chat.id: created_chat.topic})
        return HttpResponseBadRequest({"error_not_valid_form": "not valid form"})
    else:
        form = create_chat_chat()
    return render(request, 'create_chat.html', {'form': form})

class send_message_form(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['user']

@login_required
def send_message(request):
    if request.method == 'POST':
        form = send_message_form(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if not Member.objects.filter(chat_id=message.chat_id, user_id=request.user.id):
                return HttpResponseBadRequest({"not a member": "user is not a member"})
            message.user_id = request.user.id
            message = form.save()
            chat = Chat.objects.get(id=message.chat_id)
            chat.last_message = message.id
            chat.save()
            return JsonResponse({message.id: message.content})
        return HttpResponseBadRequest({"errors": form.errors}) #form errords
    else:
        form = send_message_form()
    return render(request, 'send_message.html', {'form': form})


@login_required
def read_messages(request, cid):
    chat = get_object_or_404(Chat, id=cid)
    message = Message.objects.filter(id=chat.last_message).first()
    if message:
        member = Member.objects.get(chat_id=cid, user_id=request.user.id)
        member.last_read_message = message
        member.save()
