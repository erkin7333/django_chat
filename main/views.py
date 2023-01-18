from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.contrib import messages

def home(request):
    return render(request, 'layout.html')


def frontpage(request):
    request.title = 'Welcome | Chat'
    return render(request, 'main/front_page.html')

@login_required
# Chat Xonalarinii olish
def xonalar(request):
    request.title = "Xonalar"
    rooms = Room.objects.all()
    return render(request, 'main/rooms.html', {'rooms': rooms})


# Har bit chat xonaga qo'shilish
@login_required
def xona(request, slug):
# request.title = "Xona"
    room = Room.objects.get(slug=slug)
    messag = Message.objects.filter(room=room)[0:20]
    messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz.")
    return render(request, 'main/room.html', {'room': room, 'messages': messag})