"""room_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room_manager_app.views import NewRoom, home, RoomList, room_delete, RoomModify, RoomReserve, room_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', NewRoom.as_view()),
    path('home/', home),
    path('room/list/', RoomList.as_view()),
    path('room/delete/<int:id>/', room_delete),
    path('room/modify/<int:id>/', RoomModify.as_view()),
    path('room/reserve/<int:id>/', RoomReserve.as_view()),
    path('room/<int:id>/', room_details)
]
