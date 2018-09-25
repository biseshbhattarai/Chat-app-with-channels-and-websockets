from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

@login_required
def index(request):
    return render(request, 'chatapp/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chatapp/chatroom.html', {
        'room_name_json' : mark_safe(json.dumps(room_name))
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            save = form.save(commit=False)
            password = form.cleaned_data['password']
            save.set_password(password)
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'chatapp/register.html', {'form':form})