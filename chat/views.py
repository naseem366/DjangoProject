from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request, 'admin_panel/index1.html',{})

def room(request, room_name):
    return render(request, 'admin_panel/room.html', {
        'room_name': room_name
    })