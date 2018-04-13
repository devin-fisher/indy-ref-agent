from sanic import Blueprint, Sanic
from sanic.response import json

message_route = Blueprint('Messages')

@message_route.route('/msg')
async def receive_message(request):
    return json({"hello": "world"})
