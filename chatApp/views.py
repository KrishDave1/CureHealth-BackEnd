from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def lobby(request):
    room_name = request.query_params.get('room_name')
    return JsonResponse({
        'status' : 200,
        'message' : f"You have entered the {room_name} chat room."
    })

