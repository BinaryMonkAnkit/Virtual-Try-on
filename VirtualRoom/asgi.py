
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
# api2 consumer routing 
from VTR import routing 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VirtualRoom.settings')

print("ASGI server is running")


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':URLRouter(routing.websocket_urlpatterns)
    
})


 # asgi.py in your_project_name
# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VirtualRoom.settings')

# print("ASGI is running")

# application = get_asgi_application()
