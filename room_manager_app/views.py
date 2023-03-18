from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import Room, Reservation
import datetime


def home(request):
    return render(request, "index.html")

class NewRoom(View):
    def get(self, request):
        return render(request, "add_new_room.html")
    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        if request.POST.get('is_projector') == "1":
            is_projector = True
        else:
            is_projector = False
        if not name:
            return HttpResponse('Wprowadź poprawną nazwę sali')
        if Room.objects.filter(name=name):
            return HttpResponse('Podana nazwa sali już istnieje')
        Room.objects.create(name=name, capacity=capacity, is_projector=is_projector)
        message = f"Pomyślnie dodano salę o nazwie '{name}'"
        return render(request, "add_new_room.html", {"message": message})


class RoomList(View):
    def get(self, request):
        rooms = Room.objects.all()
        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.reservation_set.all()]
            room.reserved = datetime.date.today() in reservation_dates
        return render(request, "room_list.html", {"rooms": rooms})
    def post(self, request):
        pass


def room_delete(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect("/room/list/")


class RoomModify(View):
    def get(self, request, id):
        room = Room.objects.get(id=id)
        return render(request, "room_modify.html", {"room_id": id, "room": room})
    def post(self, request, id):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        if request.POST.get('is_projector') == "1":
            is_projector = True
        else:
            is_projector = False
        if not name:
            return HttpResponse('Wprowadź poprawną nazwę sali')
        r = Room.objects.get(id=id)
        r.name = name
        r.capacity = capacity
        r.is_projector = is_projector
        r.save()
        return redirect('/room/list/')


class RoomReserve(View):
    def get(self, request, id):
        today = datetime.date.today()
        return render(request, 'room_reserve.html', {"today": today})
    def post(self, request, id):
        room_id = id
        comment = request.POST.get('comment')
        date = request.POST.get('date')
        today = datetime.datetime.today()
        date_conv = datetime.datetime.strptime(date, '%Y-%m-%d')
        if Reservation.objects.filter(date=date, room_id=Room.objects.get(id=room_id)):
            return HttpResponse('Sala jest zajętaw wybranym terminie!')
        else:
            if date_conv >= today:
                Reservation.objects.create(date=date, room_id=Room.objects.get(id=room_id), comment=comment)
                return redirect('/room/list/')
            else:
                return HttpResponse('Podano niepoprawną datę!')


def room_details(request, id):
    room = Room.objects.get(id=id)
    reservations = Reservation.objects.filter(room_id=id).order_by('date')
    return render(request, "room_details.html", {"room": room, "reservations": reservations})


