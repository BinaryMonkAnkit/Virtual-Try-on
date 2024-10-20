from django.urls import path
from . import consumers
from django.urls import re_path

websocket_urlpatterns = [
    # here the groupName values are equal to the value of groupName variable in index.html, its coming from there and it goes to the consumers.py for joining this groupName or creating one.
    # re_path(r'ws/sc/&', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi()),

]

